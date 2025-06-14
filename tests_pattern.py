# tests_pattern.py
import pytest
from pattern_impl import SquareHole, Circle, CircleAdapter
from unittest.mock import MagicMock


# POSITIVE TESTS — Normal behavior with correct math (diameter = 2 * radius)
def test_small_circle_fits_in_large_square_hole():
    """Test that a circle with diameter < hole width fits through."""
    circle = Circle(radius=3)  # diameter = 6
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=8)
    assert hole.fits(adapter) is True


def test_circle_fits_exactly_in_square_hole():
    """Test boundary condition where circle diameter equals hole width."""
    circle = Circle(radius=4)  # diameter = 8
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=8)
    assert hole.fits(adapter) is True


def test_large_circle_does_not_fit_in_small_square_hole():
    """Test that a circle with diameter > hole width does not fit through."""
    circle = Circle(radius=5)  # diameter = 10
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=9)
    assert hole.fits(adapter) is False


def test_very_small_circle_fits_anywhere():
    """Test that a very small circle fits in any reasonably sized hole."""
    circle = Circle(radius=0.5)  # diameter = 1
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=2)
    assert hole.fits(adapter) is True


# EDGE CASES
def test_zero_radius_circle_fits():
    """Test that a circle with zero radius (point) fits through any hole."""
    circle = Circle(radius=0)  # diameter = 0
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=1)
    assert hole.fits(adapter) is True


def test_circle_barely_too_large():
    """Test circle that's just slightly too large."""
    circle = Circle(radius=2.1)  # diameter = 4.2
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=4)
    assert hole.fits(adapter) is False


def test_circle_barely_fits():
    """Test circle that just barely fits."""
    circle = Circle(radius=1.9)  # diameter = 3.8
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=4)
    assert hole.fits(adapter) is True


#  NEGATIVE TESTS — Invalid inputs and error conditions
def test_circle_invalid_string_radius_raises_type_error():
    """Test that creating a circle with string radius raises TypeError."""
    with pytest.raises(TypeError, match="Radius must be a number"):
        Circle(radius="not-a-number")


def test_circle_invalid_list_radius_raises_type_error():
    """Test that creating a circle with list radius raises TypeError."""
    with pytest.raises(TypeError, match="Radius must be a number"):
        Circle(radius=[1, 2, 3])


def test_circle_invalid_none_radius_raises_type_error():
    """Test that creating a circle with None radius raises TypeError."""
    with pytest.raises(TypeError, match="Radius must be a number"):
        Circle(radius=None)


def test_square_hole_negative_width_raises_value_error():
    """Test that creating a square hole with negative width raises ValueError."""
    with pytest.raises(ValueError, match="Width must be a positive number"):
        SquareHole(width=-5)


def test_square_hole_zero_width_raises_value_error():
    """Test that creating a square hole with zero width raises ValueError."""
    with pytest.raises(ValueError, match="Width must be a positive number"):
        SquareHole(width=0)


def test_square_hole_string_width_raises_value_error():
    """Test that creating a square hole with string width raises ValueError."""
    with pytest.raises(ValueError, match="Width must be a positive number"):
        SquareHole(width="invalid")




#  MOCK TESTS — Testing interface contracts
def test_mocked_adapter_fits_successfully():
    """Test that a mocked adapter with small width fits through hole."""
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 3.5

    hole = SquareHole(width=5)
    result = hole.fits(mock_adapter)
    
    assert result is True
    mock_adapter.get_width.assert_called_once()


def test_mocked_adapter_fails_to_fit():
    """Test that a mocked adapter with large width doesn't fit through hole."""
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 12.5

    hole = SquareHole(width=8)
    result = hole.fits(mock_adapter)
    
    assert result is False
    mock_adapter.get_width.assert_called_once()


def test_mocked_adapter_exact_fit():
    """Test that a mocked adapter with exact width fits through hole."""
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 6.0

    hole = SquareHole(width=6.0)
    result = hole.fits(mock_adapter)
    
    assert result is True
    mock_adapter.get_width.assert_called_once()

