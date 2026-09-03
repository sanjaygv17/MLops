import pytest
from app import predict

def test_predict_positive():
    """Verify that positive numbers return True."""
    assert predict(5.5) is True

def test_predict_negative():
    """Verify that negative numbers return False."""
    assert predict(-1.2) is False

def test_predict_invalid_input():
    """Verify that wrong types raise a ValueError."""
    with pytest.raises(ValueError):
        predict("not a number")
