"""A module for demonstrating exceptions."""

def convert(s):
    """Convert to an integer"""
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
    return x