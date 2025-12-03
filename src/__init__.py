"""
KcMF - Knowledge-compliant Framework for Schema and Entity Matching
"""

__version__ = "1.0.0"
__author__ = "KcMF Team"

from .llm_interface import LLMInterface, create_llm, LLMProvider
from .schema_matching import SchemaMatching, create_schema_matcher
from .entity_matching import EntityMatching, create_entity_matcher

__all__ = [
    "LLMInterface",
    "create_llm",
    "LLMProvider",
    "SchemaMatching",
    "create_schema_matcher",
    "EntityMatching",
    "create_entity_matcher",
]
