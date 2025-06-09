# tests_pattern.py
import pytest
from pattern_impl import SquareHole , Circle , CircleAdapter
from unittest.mock import MagicMock

# ✅ POSITIVE TEST — normal behavior
def test_circle_fits_in_large_square_hole():
    circle = Circle(radius=5)
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=8)
    assert hole.fits(adapter) == True

# ✅ POSITIVE TEST — does not fit if hole too small
def test_circle_does_not_fit_in_small_square_hole():
    circle = Circle(radius=5)
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=6)  # 5 * sqrt(2) ≈ 7.07
    assert hole.fits(adapter) == False

# ❌ NEGATIVE TEST — invalid input to Circle
def test_invalid_radius_raises_type_error():
    with pytest.raises(TypeError):
        Circle(radius="not-a-number")

# ❌ NEGATIVE TEST — test behavior with missing method (interface misuse)
def test_fits_raises_attribute_error_on_wrong_object():
    class WrongObject:
        pass

    hole = SquareHole(width=5)
    with pytest.raises(AttributeError):
        hole.fits(WrongObject())  # No get_width() method

# 🧪 MOCK TEST — simulate adapter behavior using MagicMock
def test_mocked_adapter_fits_correctly():
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 3

    hole = SquareHole(width=4)
    assert hole.fits(mock_adapter) is True
    mock_adapter.get_width.assert_called_once()

# 🧪 MOCK TEST — simulate adapter failure
def test_mocked_adapter_fails_fit_check():
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 10

    hole = SquareHole(width=6)
    assert hole.fits(mock_adapter) is False
