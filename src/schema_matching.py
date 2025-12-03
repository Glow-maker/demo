"""
Schema Matching Module
Implements schema matching using LLMs without fine-tuning
"""

from typing import Dict, List, Optional, Tuple, Any
import json

try:
    from .llm_interface import LLMInterface
except ImportError:
    from llm_interface import LLMInterface


class SchemaMatching:
    """
    Schema matching using knowledge-compliant LLM approach
    """
    
    def __init__(
        self,
        llm: LLMInterface,
        similarity_threshold: float = 0.7,
        use_knowledge_base: bool = False
    ):
        """
        Initialize schema matcher
        
        Args:
            llm: LLM interface instance
            similarity_threshold: Minimum similarity score for matching (0-1)
            use_knowledge_base: Whether to use domain knowledge base
        """
        self.llm = llm
        self.similarity_threshold = similarity_threshold
        self.use_knowledge_base = use_knowledge_base
        self.knowledge_base = {}
    
    def match(
        self,
        schema_a: Dict[str, Any],
        schema_b: Dict[str, Any],
        context: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Match two database schemas
        
        Args:
            schema_a: First schema (dict with table and columns info)
            schema_b: Second schema
            context: Additional context or domain knowledge
            
        Returns:
            List of matches with confidence scores
        """
        matches = []
        
        # Extract columns from both schemas
        cols_a = self._extract_columns(schema_a)
        cols_b = self._extract_columns(schema_b)
        
        # Match each column from schema A to schema B
        for col_a in cols_a:
            best_match = self._find_best_match(col_a, cols_b, context)
            if best_match and best_match['confidence'] >= self.similarity_threshold:
                matches.append({
                    'source_column': col_a,
                    'target_column': best_match['column'],
                    'confidence': best_match['confidence'],
                    'reasoning': best_match['reasoning']
                })
        
        return matches
    
    def _extract_columns(self, schema: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract column information from schema"""
        columns = []
        
        if isinstance(schema.get('columns'), list):
            # Simple list of column names
            for col in schema['columns']:
                if isinstance(col, str):
                    columns.append({
                        'name': col,
                        'table': schema.get('table', 'unknown'),
                        'type': None,
                        'description': None
                    })
                elif isinstance(col, dict):
                    columns.append({
                        'name': col.get('name', ''),
                        'table': schema.get('table', 'unknown'),
                        'type': col.get('type'),
                        'description': col.get('description')
                    })
        
        return columns
    
    def _find_best_match(
        self,
        column: Dict[str, Any],
        candidate_columns: List[Dict[str, Any]],
        context: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Find the best matching column using LLM
        
        Args:
            column: Source column to match
            candidate_columns: List of candidate columns
            context: Additional context
            
        Returns:
            Best match with confidence score
        """
        # Prepare prompt for LLM
        system_prompt = """You are a database schema matching expert. Your task is to find the best matching column from a set of candidates for a given source column.

Consider:
1. Column name similarity (semantic, not just lexical)
2. Data type compatibility
3. Description and semantic meaning
4. Domain knowledge and context

Return your response as JSON with this format:
{
    "best_match": "column_name",
    "confidence": 0.95,
    "reasoning": "Explanation of why this is the best match"
}

If no good match exists, return confidence 0."""
        
        # Build column descriptions
        source_desc = f"Source column: '{column['name']}'"
        if column.get('type'):
            source_desc += f" (type: {column['type']})"
        if column.get('description'):
            source_desc += f" - {column['description']}"
        
        candidates_desc = "\nCandidate columns:\n"
        for i, candidate in enumerate(candidate_columns, 1):
            candidates_desc += f"{i}. '{candidate['name']}'"
            if candidate.get('type'):
                candidates_desc += f" (type: {candidate['type']})"
            if candidate.get('description'):
                candidates_desc += f" - {candidate['description']}"
            candidates_desc += "\n"
        
        context_desc = ""
        if context:
            context_desc = f"\nAdditional context: {context}\n"
        
        prompt = f"{source_desc}\n{candidates_desc}{context_desc}\nFind the best matching column."
        
        try:
            # Get LLM response
            response = self.llm.generate_with_json(prompt, system_prompt)
            
            # Find the matching column object
            best_match_name = response.get('best_match')
            if best_match_name:
                for candidate in candidate_columns:
                    if candidate['name'] == best_match_name:
                        return {
                            'column': candidate,
                            'confidence': response.get('confidence', 0.0),
                            'reasoning': response.get('reasoning', 'No reasoning provided')
                        }
            
            return None
            
        except Exception as e:
            print(f"Error in LLM matching: {e}")
            return None
    
    def match_batch(
        self,
        schema_pairs: List[Tuple[Dict[str, Any], Dict[str, Any]]],
        context: Optional[str] = None
    ) -> List[List[Dict[str, Any]]]:
        """
        Match multiple schema pairs in batch
        
        Args:
            schema_pairs: List of (schema_a, schema_b) tuples
            context: Additional context
            
        Returns:
            List of match results for each pair
        """
        results = []
        for schema_a, schema_b in schema_pairs:
            matches = self.match(schema_a, schema_b, context)
            results.append(matches)
        return results
    
    def add_knowledge(self, domain: str, rules: Dict[str, Any]):
        """
        Add domain knowledge for better matching
        
        Args:
            domain: Domain name (e.g., 'finance', 'healthcare')
            rules: Domain-specific matching rules and knowledge
        """
        self.knowledge_base[domain] = rules
    
    def explain_match(self, match: Dict[str, Any]) -> str:
        """
        Generate detailed explanation for a match
        
        Args:
            match: Match result dictionary
            
        Returns:
            Human-readable explanation
        """
        source = match['source_column']['name']
        target = match['target_column']['name']
        confidence = match['confidence']
        reasoning = match['reasoning']
        
        explanation = f"""
Schema Match Explanation:
------------------------
Source Column: {source}
Target Column: {target}
Confidence: {confidence:.2%}

Reasoning:
{reasoning}
"""
        return explanation


def create_schema_matcher(
    llm: LLMInterface,
    similarity_threshold: float = 0.7
) -> SchemaMatching:
    """
    Convenience function to create a schema matcher
    
    Args:
        llm: LLM interface instance
        similarity_threshold: Minimum similarity threshold
        
    Returns:
        SchemaMatching instance
    """
    return SchemaMatching(llm, similarity_threshold)
