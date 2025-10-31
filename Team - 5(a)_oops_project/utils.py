"""
Utility functions.
"""
import uuid

def generate_id(prefix):
    """Generate a random unique ID with a given prefix."""
    return f"{prefix}-{uuid.uuid4().hex[:6].upper()}"
