# KcMF: Knowledge-compliant Framework Implementation Guide

## Overview

This project provides a practical implementation of the KcMF (Knowledge-compliant Framework for Schema and Entity Matching with Fine-tuning-free LLMs) framework, designed to help users integrate this technology into their database systems for production use.

KcMF is a framework that leverages Large Language Models (LLMs) for schema matching and entity matching without requiring fine-tuning, making it accessible and cost-effective for industrial applications.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- API access to an LLM provider (OpenAI, Qwen, etc.)
- Basic understanding of databases and data integration

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd demo

# Install dependencies
pip install -r requirements.txt

# Configure your LLM API keys
cp config/llm_config.yaml.example config/llm_config.yaml
# Edit config/llm_config.yaml with your API credentials
```

### Basic Usage

#### Schema Matching

```python
from src.schema_matching import SchemaMatching
from src.llm_interface import LLMInterface

# Initialize LLM interface
llm = LLMInterface(provider="openai", api_key="your-key")

# Create schema matcher
matcher = SchemaMatching(llm)

# Match two database schemas
result = matcher.match(schema_a, schema_b)
print(result)
```

#### Entity Matching

```python
from src.entity_matching import EntityMatching

# Create entity matcher
matcher = EntityMatching(llm)

# Match two entities
result = matcher.match(entity_a, entity_b)
print(f"Match: {result['is_match']}, Confidence: {result['confidence']}")
```

## Core Concepts

### 1. Schema Matching
Identifies corresponding attributes and structures across different data sources.

### 2. Entity Matching
Identifies records representing the same real-world entity across different sources.

### 3. Knowledge Compliance
Uses domain knowledge and constraints to improve matching quality and ensure business rule compliance.

## Project Structure

```
demo/
├── README.md                          # English documentation (this file)
├── README_CN.md                       # Chinese documentation
├── config/                            # Configuration files
├── src/                               # Source code
├── examples/                          # Example scripts
├── data/                              # Sample data
├── workflows/                         # Dify workflows
└── tests/                             # Test cases
```

## Documentation

- [中文文档](README_CN.md) - Comprehensive Chinese documentation
- [API Reference](docs/API.md) - API documentation
- [Tutorial](docs/TUTORIAL.md) - Step-by-step tutorial

## Features

- ✅ Zero fine-tuning required
- ✅ Multiple LLM provider support
- ✅ Batch processing capabilities
- ✅ Database integration (MySQL, PostgreSQL, MongoDB)
- ✅ Dify workflow templates
- ✅ Production-ready examples

## Use Cases

1. **Data Governance**: Integrate data from multiple enterprise systems
2. **Master Data Management (MDM)**: Build enterprise-level master data systems
3. **Knowledge Graph Construction**: Build knowledge graphs from multi-source data

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License

## Contact

For questions and support, please open an issue on GitHub.