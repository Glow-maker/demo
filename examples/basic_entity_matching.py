"""
Basic Entity Matching Example

This example demonstrates how to use KcMF for entity matching to identify
duplicate or related entities across different data sources.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.llm_interface import create_llm
from src.entity_matching import create_entity_matcher


def main():
    """Run basic entity matching example"""
    
    print("=" * 60)
    print("KcMF Basic Entity Matching Example")
    print("=" * 60)
    print()
    
    # Step 1: Initialize LLM
    print("Step 1: Initializing LLM interface...")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("WARNING: No API key found. Set OPENAI_API_KEY environment variable.")
        demo_mode = True
    else:
        demo_mode = False
    
    llm = create_llm(
        provider="openai",
        model="gpt-4",
        api_key=api_key,
        temperature=0.3
    )
    print("✓ LLM interface created")
    print()
    
    # Step 2: Define entities to match
    print("Step 2: Defining entities from different sources...")
    print()
    
    # Example 1: Company entities
    print("Example 1: Matching company entities")
    print("-" * 40)
    
    company_a = {
        "name": "Apple Inc.",
        "location": "Cupertino, California, USA",
        "industry": "Technology",
        "founded": "1976",
        "ceo": "Tim Cook",
        "stock_symbol": "AAPL"
    }
    
    company_b = {
        "name": "苹果公司",
        "location": "美国加利福尼亚州库比蒂诺",
        "industry": "科技",
        "founded": "1976年",
        "ceo": "蒂姆·库克"
    }
    
    print("Company A (English source):")
    for key, value in company_a.items():
        print(f"  {key}: {value}")
    print()
    
    print("Company B (Chinese source):")
    for key, value in company_b.items():
        print(f"  {key}: {value}")
    print()
    
    # Example 2: Person entities with slight variations
    person_a = {
        "name": "John Smith",
        "email": "john.smith@company.com",
        "phone": "+1-555-0123",
        "title": "Senior Software Engineer",
        "department": "Engineering"
    }
    
    person_b = {
        "name": "J. Smith",
        "email": "jsmith@company.com",
        "phone": "555-0123",
        "title": "Sr. Software Eng.",
        "department": "Engineering Dept"
    }
    
    # Step 3: Create entity matcher
    print("Step 3: Creating entity matcher...")
    matcher = create_entity_matcher(
        llm=llm,
        match_threshold=0.8  # 80% confidence minimum
    )
    print("✓ Entity matcher created")
    print()
    
    # Step 4: Perform matching
    if demo_mode:
        print("Step 4: [DEMO MODE] Showing expected output structure...")
        print()
        print("Expected results:")
        print()
        print("Company Match:")
        print("  is_match: True")
        print("  confidence: ~0.95")
        print("  reasoning: Both entities refer to Apple Inc., despite language differences")
        print("  matched_attributes: location, founded, ceo")
        print()
        print("Person Match:")
        print("  is_match: True")
        print("  confidence: ~0.85")
        print("  reasoning: Same person with abbreviated name and email variations")
        print("  matched_attributes: department, phone (normalized)")
        print()
    else:
        print("Step 4: Performing entity matching...")
        print()
        
        # Match companies
        print("Matching companies...")
        try:
            result1 = matcher.match(
                company_a,
                company_b,
                context="Companies in technology sector"
            )
            
            print(f"Match Result: {'✓ MATCH' if result1['is_match'] else '✗ NO MATCH'}")
            print(f"Confidence: {result1['confidence']:.2%}")
            print(f"Reasoning: {result1['reasoning']}")
            if result1.get('matched_attributes'):
                print(f"Matched Attributes: {', '.join(result1['matched_attributes'])}")
            if result1.get('conflicting_attributes'):
                print(f"Conflicting Attributes: {', '.join(result1['conflicting_attributes'])}")
            print()
            
            # Show detailed explanation
            explanation1 = matcher.explain_match(result1)
            print(explanation1)
            
        except Exception as e:
            print(f"Error matching companies: {e}")
            print()
        
        # Match persons
        print("Matching persons...")
        try:
            result2 = matcher.match(
                person_a,
                person_b,
                context="Employee records from different HR systems"
            )
            
            print(f"Match Result: {'✓ MATCH' if result2['is_match'] else '✗ NO MATCH'}")
            print(f"Confidence: {result2['confidence']:.2%}")
            print(f"Reasoning: {result2['reasoning']}")
            if result2.get('matched_attributes'):
                print(f"Matched Attributes: {', '.join(result2['matched_attributes'])}")
            if result2.get('conflicting_attributes'):
                print(f"Conflicting Attributes: {', '.join(result2['conflicting_attributes'])}")
            print()
            
        except Exception as e:
            print(f"Error matching persons: {e}")
            print()
    
    # Step 5: Finding duplicates in a list
    print("=" * 60)
    print("Step 5: Finding duplicates in a list of entities")
    print("=" * 60)
    print()
    
    # Example customer list with duplicates
    customers = [
        {"id": "1", "name": "Microsoft Corp", "location": "Redmond, WA"},
        {"id": "2", "name": "Microsoft Corporation", "location": "Redmond, Washington"},
        {"id": "3", "name": "Google LLC", "location": "Mountain View, CA"},
        {"id": "4", "name": "微软公司", "location": "华盛顿州雷德蒙德"},
        {"id": "5", "name": "Alphabet Inc", "location": "Mountain View, California"},
    ]
    
    print("Customer list:")
    for customer in customers:
        print(f"  {customer['id']}: {customer['name']} - {customer['location']}")
    print()
    
    if demo_mode:
        print("[DEMO MODE] Expected duplicate groups:")
        print("  Group 1: [0, 1, 3] - Microsoft entities")
        print("  Group 2: [2, 4] - Google/Alphabet entities")
        print()
    else:
        print("Finding duplicate groups...")
        try:
            duplicate_groups = matcher.find_duplicates(
                customers,
                context="Technology companies"
            )
            
            print(f"Found {len(duplicate_groups)} duplicate groups:")
            for i, group in enumerate(duplicate_groups, 1):
                print(f"\nGroup {i}:")
                for idx in group:
                    print(f"  - {customers[idx]['name']} (ID: {customers[idx]['id']})")
            print()
            
            # Step 6: Merge duplicates
            if duplicate_groups:
                print("Step 6: Merging duplicate entities...")
                first_group = duplicate_groups[0]
                entities_to_merge = [customers[idx] for idx in first_group]
                
                merged = matcher.merge_entities(entities_to_merge, strategy="llm")
                print("\nMerged entity:")
                for key, value in merged.items():
                    print(f"  {key}: {value}")
                print()
        
        except Exception as e:
            print(f"Error finding duplicates: {e}")
            print()
    
    print("=" * 60)
    print("Example Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Try with your own entity data")
    print("  2. Experiment with different match thresholds")
    print("  3. Add domain-specific knowledge for better accuracy")
    print("  4. Check out database_integration.py for real-world usage")


if __name__ == "__main__":
    main()
