"""
Basic Schema Matching Example

This example demonstrates how to use KcMF for schema matching between two databases.
Perfect for understanding the basics and getting started.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.llm_interface import create_llm
from src.schema_matching import create_schema_matcher


def main():
    """Run basic schema matching example"""
    
    print("=" * 60)
    print("KcMF Basic Schema Matching Example")
    print("=" * 60)
    print()
    
    # Step 1: Initialize LLM
    print("Step 1: Initializing LLM interface...")
    print("Note: Set your API key in environment variable or pass it directly")
    print()
    
    # Try to get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("WARNING: No API key found. Set OPENAI_API_KEY environment variable.")
        print("Example: export OPENAI_API_KEY='your-key-here'")
        print()
        print("For this demo, we'll show the structure without making API calls.")
        demo_mode = True
    else:
        demo_mode = False
    
    # Create LLM interface
    # You can change provider to "qwen", "glm", etc.
    llm = create_llm(
        provider="openai",
        model="gpt-4",
        api_key=api_key,
        temperature=0.3
    )
    print("✓ LLM interface created")
    print()
    
    # Step 2: Define schemas to match
    print("Step 2: Defining database schemas...")
    
    # Schema A: E-commerce customer database
    schema_a = {
        "database": "ecommerce_db",
        "table": "customers",
        "columns": [
            {
                "name": "customer_id",
                "type": "INTEGER",
                "description": "Unique customer identifier"
            },
            {
                "name": "customer_name",
                "type": "VARCHAR(100)",
                "description": "Full name of the customer"
            },
            {
                "name": "email",
                "type": "VARCHAR(255)",
                "description": "Customer email address"
            },
            {
                "name": "phone_number",
                "type": "VARCHAR(20)",
                "description": "Contact phone number"
            },
            {
                "name": "registration_date",
                "type": "DATETIME",
                "description": "Date when customer registered"
            }
        ]
    }
    
    # Schema B: CRM client database
    schema_b = {
        "database": "crm_db",
        "table": "clients",
        "columns": [
            {
                "name": "client_id",
                "type": "INT",
                "description": "Unique identifier for client"
            },
            {
                "name": "full_name",
                "type": "TEXT",
                "description": "Client's complete name"
            },
            {
                "name": "email_address",
                "type": "TEXT",
                "description": "Primary email for communication"
            },
            {
                "name": "contact_phone",
                "type": "TEXT",
                "description": "Phone number for contact"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "description": "Account creation timestamp"
            },
            {
                "name": "company_name",
                "type": "TEXT",
                "description": "Company/organization name"
            }
        ]
    }
    
    print(f"Schema A: {schema_a['database']}.{schema_a['table']}")
    print(f"  Columns: {len(schema_a['columns'])}")
    print()
    print(f"Schema B: {schema_b['database']}.{schema_b['table']}")
    print(f"  Columns: {len(schema_b['columns'])}")
    print()
    
    # Step 3: Create schema matcher
    print("Step 3: Creating schema matcher...")
    matcher = create_schema_matcher(
        llm=llm,
        similarity_threshold=0.7  # 70% confidence minimum
    )
    print("✓ Schema matcher created")
    print()
    
    # Step 4: Perform matching
    if demo_mode:
        print("Step 4: [DEMO MODE] Showing expected output structure...")
        print()
        print("Expected matches would include:")
        print("  - customer_id ↔ client_id (confidence: ~0.95)")
        print("  - customer_name ↔ full_name (confidence: ~0.90)")
        print("  - email ↔ email_address (confidence: ~0.95)")
        print("  - phone_number ↔ contact_phone (confidence: ~0.88)")
        print("  - registration_date ↔ created_at (confidence: ~0.85)")
        print()
    else:
        print("Step 4: Performing schema matching...")
        print("This may take a moment as we query the LLM...")
        print()
        
        # Add context for better matching
        context = "Both databases store customer/client information for business operations."
        
        try:
            matches = matcher.match(schema_a, schema_b, context=context)
            
            print(f"Found {len(matches)} matches:")
            print()
            
            for i, match in enumerate(matches, 1):
                print(f"Match {i}:")
                print(f"  Source: {match['source_column']['name']} ({match['source_column']['type']})")
                print(f"  Target: {match['target_column']['name']} ({match['target_column']['type']})")
                print(f"  Confidence: {match['confidence']:.2%}")
                print(f"  Reasoning: {match['reasoning']}")
                print()
            
            # Step 5: Show detailed explanation for best match
            if matches:
                print("Step 5: Detailed explanation of best match...")
                print()
                best_match = max(matches, key=lambda m: m['confidence'])
                explanation = matcher.explain_match(best_match)
                print(explanation)
        
        except Exception as e:
            print(f"Error during matching: {e}")
            print()
            print("This might be due to:")
            print("  - Invalid API key")
            print("  - Network connectivity issues")
            print("  - API quota exceeded")
    
    print()
    print("=" * 60)
    print("Example Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Try modifying the schemas with your own data")
    print("  2. Experiment with different similarity thresholds")
    print("  3. Add domain-specific context for better results")
    print("  4. Check out advanced_schema_matching.py for more features")


if __name__ == "__main__":
    main()
