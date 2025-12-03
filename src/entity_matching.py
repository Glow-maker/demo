"""
Entity Matching Module
Implements entity matching using LLMs without fine-tuning
"""

from typing import Dict, List, Optional, Any
import json

try:
    from .llm_interface import LLMInterface
except ImportError:
    from llm_interface import LLMInterface


class EntityMatching:
    """
    Entity matching using knowledge-compliant LLM approach
    """
    
    def __init__(
        self,
        llm: LLMInterface,
        match_threshold: float = 0.8,
        use_knowledge_base: bool = False
    ):
        """
        Initialize entity matcher
        
        Args:
            llm: LLM interface instance
            match_threshold: Minimum confidence score for considering entities as match
            use_knowledge_base: Whether to use domain knowledge base
        """
        self.llm = llm
        self.match_threshold = match_threshold
        self.use_knowledge_base = use_knowledge_base
        self.knowledge_base = {}
    
    def match(
        self,
        entity_a: Dict[str, Any],
        entity_b: Dict[str, Any],
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Determine if two entities represent the same real-world object
        
        Args:
            entity_a: First entity (dict with attributes)
            entity_b: Second entity
            context: Additional context or domain knowledge
            
        Returns:
            Match result with confidence score and reasoning
        """
        system_prompt = """You are an entity matching expert. Your task is to determine if two entities represent the same real-world object.

Consider:
1. Name similarity (including synonyms, abbreviations, translations)
2. Attribute consistency (location, type, identifiers, etc.)
3. Contextual information
4. Domain-specific knowledge

Return your response as JSON with this format:
{
    "is_match": true/false,
    "confidence": 0.95,
    "reasoning": "Detailed explanation of the matching decision",
    "matched_attributes": ["attribute1", "attribute2"],
    "conflicting_attributes": ["attribute3"]
}"""
        
        # Build entity descriptions
        entity_a_desc = "Entity A:\n" + json.dumps(entity_a, indent=2, ensure_ascii=False)
        entity_b_desc = "Entity B:\n" + json.dumps(entity_b, indent=2, ensure_ascii=False)
        
        context_desc = ""
        if context:
            context_desc = f"\nAdditional context: {context}\n"
        
        prompt = f"{entity_a_desc}\n\n{entity_b_desc}{context_desc}\n\nAre these two entities the same?"
        
        try:
            # Get LLM response
            response = self.llm.generate_with_json(prompt, system_prompt)
            
            return {
                'is_match': response.get('is_match', False),
                'confidence': response.get('confidence', 0.0),
                'reasoning': response.get('reasoning', 'No reasoning provided'),
                'matched_attributes': response.get('matched_attributes', []),
                'conflicting_attributes': response.get('conflicting_attributes', []),
                'entity_a': entity_a,
                'entity_b': entity_b
            }
            
        except Exception as e:
            print(f"Error in entity matching: {e}")
            return {
                'is_match': False,
                'confidence': 0.0,
                'reasoning': f'Error during matching: {str(e)}',
                'matched_attributes': [],
                'conflicting_attributes': [],
                'entity_a': entity_a,
                'entity_b': entity_b
            }
    
    def match_batch(
        self,
        entity_pairs: List[tuple],
        context: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Match multiple entity pairs in batch
        
        Args:
            entity_pairs: List of (entity_a, entity_b) tuples
            context: Additional context
            
        Returns:
            List of match results
        """
        results = []
        for entity_a, entity_b in entity_pairs:
            result = self.match(entity_a, entity_b, context)
            results.append(result)
        return results
    
    def find_duplicates(
        self,
        entities: List[Dict[str, Any]],
        context: Optional[str] = None
    ) -> List[List[int]]:
        """
        Find duplicate entities in a list
        
        Args:
            entities: List of entities
            context: Additional context
            
        Returns:
            List of lists, where each inner list contains indices of matching entities
        """
        n = len(entities)
        matched_groups = []
        processed = set()
        
        for i in range(n):
            if i in processed:
                continue
            
            group = [i]
            for j in range(i + 1, n):
                if j in processed:
                    continue
                
                result = self.match(entities[i], entities[j], context)
                if result['is_match'] and result['confidence'] >= self.match_threshold:
                    group.append(j)
                    processed.add(j)
            
            if len(group) > 1:
                matched_groups.append(group)
            processed.add(i)
        
        return matched_groups
    
    def merge_entities(
        self,
        entities: List[Dict[str, Any]],
        strategy: str = "union"
    ) -> Dict[str, Any]:
        """
        Merge multiple matching entities into one
        
        Args:
            entities: List of entities to merge
            strategy: Merge strategy ('union', 'intersection', 'llm')
            
        Returns:
            Merged entity
        """
        if not entities:
            return {}
        
        if len(entities) == 1:
            return entities[0]
        
        if strategy == "union":
            # Union: include all attributes from all entities
            merged = {}
            for entity in entities:
                for key, value in entity.items():
                    if key not in merged:
                        merged[key] = value
                    elif merged[key] != value:
                        # Handle conflicts by creating a list
                        if not isinstance(merged[key], list):
                            merged[key] = [merged[key]]
                        if value not in merged[key]:
                            merged[key].append(value)
            return merged
        
        elif strategy == "intersection":
            # Intersection: only include attributes that are consistent across all entities
            if not entities:
                return {}
            merged = dict(entities[0])
            for entity in entities[1:]:
                keys_to_remove = []
                for key in merged:
                    if key not in entity or merged[key] != entity[key]:
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    del merged[key]
            return merged
        
        elif strategy == "llm":
            # Use LLM to intelligently merge entities
            system_prompt = """You are an entity merging expert. Given multiple entities that represent the same real-world object, merge them into a single, comprehensive entity.

Consider:
1. Choose the most complete and accurate value for each attribute
2. Resolve conflicts intelligently
3. Preserve all unique information
4. Handle different languages, formats, and representations

Return the merged entity as JSON."""
            
            entities_desc = "Entities to merge:\n"
            for i, entity in enumerate(entities, 1):
                entities_desc += f"\nEntity {i}:\n{json.dumps(entity, indent=2, ensure_ascii=False)}\n"
            
            prompt = f"{entities_desc}\n\nMerge these entities into one comprehensive entity."
            
            try:
                merged = self.llm.generate_with_json(prompt, system_prompt)
                return merged
            except Exception as e:
                print(f"Error in LLM merge: {e}, falling back to union strategy")
                return self.merge_entities(entities, "union")
        
        else:
            raise ValueError(f"Unknown merge strategy: {strategy}")
    
    def add_knowledge(self, domain: str, rules: Dict[str, Any]):
        """
        Add domain knowledge for better matching
        
        Args:
            domain: Domain name (e.g., 'companies', 'people')
            rules: Domain-specific matching rules and knowledge
        """
        self.knowledge_base[domain] = rules
    
    def explain_match(self, match_result: Dict[str, Any]) -> str:
        """
        Generate detailed explanation for a match result
        
        Args:
            match_result: Match result dictionary
            
        Returns:
            Human-readable explanation
        """
        is_match = match_result['is_match']
        confidence = match_result['confidence']
        reasoning = match_result['reasoning']
        matched_attrs = match_result.get('matched_attributes', [])
        conflicting_attrs = match_result.get('conflicting_attributes', [])
        
        explanation = f"""
Entity Match Explanation:
------------------------
Match Result: {'MATCH' if is_match else 'NO MATCH'}
Confidence: {confidence:.2%}

Reasoning:
{reasoning}

Matched Attributes: {', '.join(matched_attrs) if matched_attrs else 'None'}
Conflicting Attributes: {', '.join(conflicting_attrs) if conflicting_attrs else 'None'}
"""
        return explanation


def create_entity_matcher(
    llm: LLMInterface,
    match_threshold: float = 0.8
) -> EntityMatching:
    """
    Convenience function to create an entity matcher
    
    Args:
        llm: LLM interface instance
        match_threshold: Minimum match threshold
        
    Returns:
        EntityMatching instance
    """
    return EntityMatching(llm, match_threshold)
