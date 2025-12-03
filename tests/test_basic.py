"""
Basic tests for KcMF framework
Run with: pytest tests/test_basic.py
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import create_llm, LLMProvider
from src.schema_matching import SchemaMatching
from src.entity_matching import EntityMatching


class TestLLMInterface:
    """Test LLM interface creation and configuration"""
    
    def test_create_llm_openai(self):
        """Test creating OpenAI LLM interface"""
        llm = create_llm(provider="openai", api_key="test-key", model="gpt-4")
        assert llm.provider == "openai"
        assert llm.model == "gpt-4"
        assert llm.api_key == "test-key"
    
    def test_create_llm_qwen(self):
        """Test creating Qwen LLM interface"""
        llm = create_llm(provider="qwen", api_key="test-key")
        assert llm.provider == "qwen"
        assert llm.model == "qwen-plus"
    
    def test_llm_provider_enum(self):
        """Test LLM provider enum"""
        assert LLMProvider.OPENAI.value == "openai"
        assert LLMProvider.QWEN.value == "qwen"
        assert LLMProvider.GLM.value == "glm"


class TestSchemaMatching:
    """Test schema matching functionality"""
    
    def test_schema_matcher_creation(self):
        """Test creating schema matcher"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = SchemaMatching(llm, similarity_threshold=0.7)
        assert matcher.similarity_threshold == 0.7
        assert matcher.llm is not None
    
    def test_extract_columns_simple(self):
        """Test extracting columns from simple schema"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = SchemaMatching(llm)
        
        schema = {
            "table": "users",
            "columns": ["id", "name", "email"]
        }
        
        columns = matcher._extract_columns(schema)
        assert len(columns) == 3
        assert columns[0]["name"] == "id"
        assert columns[0]["table"] == "users"
    
    def test_extract_columns_detailed(self):
        """Test extracting columns with detailed info"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = SchemaMatching(llm)
        
        schema = {
            "table": "products",
            "columns": [
                {"name": "product_id", "type": "INT", "description": "Product ID"},
                {"name": "price", "type": "DECIMAL", "description": "Product price"}
            ]
        }
        
        columns = matcher._extract_columns(schema)
        assert len(columns) == 2
        assert columns[0]["type"] == "INT"
        assert columns[1]["description"] == "Product price"
    
    def test_add_knowledge(self):
        """Test adding domain knowledge"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = SchemaMatching(llm)
        
        rules = {"synonyms": {"customer": ["client", "user"]}}
        matcher.add_knowledge("ecommerce", rules)
        
        assert "ecommerce" in matcher.knowledge_base
        assert matcher.knowledge_base["ecommerce"] == rules


class TestEntityMatching:
    """Test entity matching functionality"""
    
    def test_entity_matcher_creation(self):
        """Test creating entity matcher"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = EntityMatching(llm, match_threshold=0.8)
        assert matcher.match_threshold == 0.8
        assert matcher.llm is not None
    
    def test_merge_entities_union(self):
        """Test merging entities with union strategy"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = EntityMatching(llm)
        
        entities = [
            {"name": "Apple", "location": "Cupertino"},
            {"name": "Apple Inc.", "founded": "1976"}
        ]
        
        merged = matcher.merge_entities(entities, strategy="union")
        assert "name" in merged
        assert "location" in merged
        assert "founded" in merged
    
    def test_merge_entities_intersection(self):
        """Test merging entities with intersection strategy"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = EntityMatching(llm)
        
        entities = [
            {"name": "Apple", "location": "Cupertino"},
            {"name": "Apple", "location": "Cupertino", "extra": "data"}
        ]
        
        merged = matcher.merge_entities(entities, strategy="intersection")
        assert "name" in merged
        assert "location" in merged
        assert merged["name"] == "Apple"
    
    def test_add_knowledge(self):
        """Test adding domain knowledge"""
        llm = create_llm(provider="openai", api_key="test-key")
        matcher = EntityMatching(llm)
        
        rules = {"key_attributes": ["name", "location"]}
        matcher.add_knowledge("companies", rules)
        
        assert "companies" in matcher.knowledge_base


class TestDataLoading:
    """Test loading sample data"""
    
    def test_load_sample_schemas(self):
        """Test loading sample schema files"""
        import json
        
        schema_a_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_schema_a.json')
        schema_b_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_schema_b.json')
        
        with open(schema_a_path, 'r') as f:
            schema_a = json.load(f)
        
        with open(schema_b_path, 'r') as f:
            schema_b = json.load(f)
        
        assert "table" in schema_a
        assert "columns" in schema_a
        assert len(schema_a["columns"]) > 0
        
        assert "table" in schema_b
        assert "columns" in schema_b
        assert len(schema_b["columns"]) > 0
    
    def test_load_sample_entities(self):
        """Test loading sample entity data"""
        import json
        
        entities_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_entities.json')
        
        with open(entities_path, 'r') as f:
            entities = json.load(f)
        
        assert isinstance(entities, list)
        assert len(entities) > 0
        assert "name" in entities[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
