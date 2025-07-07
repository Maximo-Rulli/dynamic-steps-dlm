#!/usr/bin/env python3

# Test script to verify imports work correctly
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Test importing the models
    from MMaDA.models import MMadaModelLM
    print("✓ Successfully imported MMadaModelLM from MMaDA.models")
    
    # Test importing the generate function
    from MMaDA.generate import generate
    print("✓ Successfully imported generate function from MMaDA.generate")
    
    # Test importing other functions
    from MMaDA.generate import add_gumbel_noise, get_num_transfer_tokens
    print("✓ Successfully imported additional functions from MMaDA.generate")
    
    print("\nAll imports successful! You can now use these in your notebook.")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    sys.exit(1) 