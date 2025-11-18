#!/usr/bin/env python3
"""
RAG Distillation Batch Processing Script

This script processes questions and source chunks through Dify's RAG workflow
to generate high-quality Q&A pairs for training data.

Usage:
    python rag_distillation.py --input data.jsonl --output results.jsonl

Input format (JSONL - one JSON object per line):
    {"query": "问题文本", "source_chunk": "原始文本片段"}

Output format (JSONL):
    {
        "query": "问题",
        "source_chunk": "原始chunk",
        "answer": "生成的答案",
        "quality_score": 85.5,
        "quality_level": "excellent",
        "distill_rag": [...],
        "timestamp": "2024-01-01T00:00:00"
    }
"""

import os
import sys
import json
import time
import argparse
import logging
from typing import Dict, List, Optional
from datetime import datetime
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DifyRAGDistiller:
    """Handles batch processing of RAG distillation through Dify API"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.dify.ai/v1"):
        """
        Initialize the distiller
        
        Args:
            api_key: Dify API key (from DIFY_KEY environment variable)
            base_url: Base URL for Dify API
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def process_single(self, query: str, source_chunk: str, 
                      user_id: str = "batch_user") -> Optional[Dict]:
        """
        Process a single query-chunk pair through the workflow
        
        Args:
            query: The question to process
            source_chunk: The source text chunk
            user_id: User identifier for the API call
            
        Returns:
            Dictionary with the processed results or None on error
        """
        endpoint = f"{self.base_url}/workflows/run"
        
        payload = {
            "inputs": {
                "query": query,
                "source_chunk": source_chunk
            },
            "response_mode": "blocking",
            "user": user_id
        }
        
        try:
            logger.info(f"Processing query: {query[:50]}...")
            response = requests.post(
                endpoint,
                headers=self.headers,
                json=payload,
                timeout=300  # 5 minutes timeout
            )
            response.raise_for_status()
            
            result = response.json()
            
            # Extract the outputs from Dify workflow
            if "data" in result and "outputs" in result["data"]:
                outputs = result["data"]["outputs"]
                return {
                    "query": query,
                    "source_chunk": source_chunk,
                    "answer": outputs.get("text", ""),
                    "quality_score": outputs.get("quality_score", 0),
                    "quality_level": outputs.get("quality_level", "unknown"),
                    "quality_details": outputs.get("quality_details", ""),
                    "query_is_valid": outputs.get("query_is_valid", ""),
                    "query_class_name": outputs.get("query_class_name", ""),
                    "first_rag_answer": outputs.get("first_rag_answer", ""),
                    "distill_rag": outputs.get("distill_rag", []),
                    "timestamp": datetime.now().isoformat(),
                    "status": "success"
                }
            else:
                logger.error(f"Unexpected response format: {result}")
                return None
                
        except requests.exceptions.Timeout:
            logger.error(f"Timeout processing query: {query[:50]}...")
            return {
                "query": query,
                "source_chunk": source_chunk,
                "error": "timeout",
                "status": "failed",
                "timestamp": datetime.now().isoformat()
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error processing query: {e}")
            return {
                "query": query,
                "source_chunk": source_chunk,
                "error": str(e),
                "status": "failed",
                "timestamp": datetime.now().isoformat()
            }
    
    def process_batch(self, input_file: str, output_file: str, 
                     delay: float = 1.0, resume: bool = True) -> Dict:
        """
        Process a batch of query-chunk pairs
        
        Args:
            input_file: Path to input JSONL file
            output_file: Path to output JSONL file
            delay: Delay in seconds between requests
            resume: Whether to resume from existing output file
            
        Returns:
            Statistics dictionary
        """
        # Load already processed queries if resuming
        processed_queries = set()
        if resume and os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        item = json.loads(line)
                        processed_queries.add(item.get("query", ""))
                    except json.JSONDecodeError:
                        continue
            logger.info(f"Resuming: {len(processed_queries)} items already processed")
        
        # Process input file
        stats = {
            "total": 0,
            "processed": 0,
            "success": 0,
            "failed": 0,
            "skipped": len(processed_queries)
        }
        
        mode = 'a' if resume else 'w'
        
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, mode, encoding='utf-8') as outfile:
            
            for line_num, line in enumerate(infile, 1):
                try:
                    item = json.loads(line.strip())
                    query = item.get("query", "")
                    source_chunk = item.get("source_chunk", "")
                    
                    if not query:
                        logger.warning(f"Line {line_num}: Empty query, skipping")
                        continue
                    
                    stats["total"] += 1
                    
                    # Skip if already processed
                    if query in processed_queries:
                        logger.info(f"Line {line_num}: Already processed, skipping")
                        continue
                    
                    # Process the item
                    result = self.process_single(query, source_chunk)
                    
                    if result:
                        stats["processed"] += 1
                        if result.get("status") == "success":
                            stats["success"] += 1
                        else:
                            stats["failed"] += 1
                        
                        # Write result immediately (streaming output)
                        outfile.write(json.dumps(result, ensure_ascii=False) + '\n')
                        outfile.flush()
                        
                        logger.info(
                            f"Line {line_num}: {result.get('status', 'unknown')} - "
                            f"Quality: {result.get('quality_score', 'N/A')}"
                        )
                    else:
                        stats["failed"] += 1
                        logger.error(f"Line {line_num}: Failed to process")
                    
                    # Rate limiting
                    if delay > 0:
                        time.sleep(delay)
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Line {line_num}: Invalid JSON - {e}")
                    stats["failed"] += 1
                except Exception as e:
                    logger.error(f"Line {line_num}: Unexpected error - {e}")
                    stats["failed"] += 1
        
        return stats


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Batch process RAG distillation through Dify workflow'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Input JSONL file with query and source_chunk fields'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output JSONL file for results'
    )
    parser.add_argument(
        '--delay', '-d',
        type=float,
        default=1.0,
        help='Delay between requests in seconds (default: 1.0)'
    )
    parser.add_argument(
        '--api-key',
        help='Dify API key (default: from DIFY_KEY environment variable)'
    )
    parser.add_argument(
        '--base-url',
        default='https://api.dify.ai/v1',
        help='Dify API base URL (default: https://api.dify.ai/v1)'
    )
    parser.add_argument(
        '--no-resume',
        action='store_true',
        help='Do not resume from existing output file'
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.environ.get('DIFY_KEY')
    if not api_key:
        logger.error(
            "API key not found. Please set DIFY_KEY environment variable "
            "or use --api-key option"
        )
        sys.exit(1)
    
    # Validate input file
    if not os.path.exists(args.input):
        logger.error(f"Input file not found: {args.input}")
        sys.exit(1)
    
    # Initialize distiller
    distiller = DifyRAGDistiller(api_key, args.base_url)
    
    # Process batch
    logger.info(f"Starting batch processing...")
    logger.info(f"Input: {args.input}")
    logger.info(f"Output: {args.output}")
    logger.info(f"Delay: {args.delay}s")
    
    start_time = time.time()
    stats = distiller.process_batch(
        args.input,
        args.output,
        delay=args.delay,
        resume=not args.no_resume
    )
    elapsed_time = time.time() - start_time
    
    # Print statistics
    logger.info("=" * 60)
    logger.info("Processing complete!")
    logger.info(f"Total items in input: {stats['total']}")
    logger.info(f"Already processed (skipped): {stats['skipped']}")
    logger.info(f"Newly processed: {stats['processed']}")
    logger.info(f"  - Success: {stats['success']}")
    logger.info(f"  - Failed: {stats['failed']}")
    logger.info(f"Elapsed time: {elapsed_time:.2f} seconds")
    if stats['processed'] > 0:
        logger.info(f"Average time per item: {elapsed_time / stats['processed']:.2f} seconds")
    logger.info("=" * 60)


if __name__ == '__main__':
    main()
