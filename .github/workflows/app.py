def predict(val: float) -> bool:
    """Returns True if input is positive, matching dummy model criteria."""
    if not isinstance(val, (int, float)):
        raise ValueError("Input must be a number")
    return val > 0.0
