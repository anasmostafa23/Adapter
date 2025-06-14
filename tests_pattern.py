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


# 🔍 EDGE CASES
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


def test_fits_with_object_missing_get_width_method():
    """Test that fits() raises TypeError when object lacks get_width() method."""
    class InvalidObject:
        pass

    hole = SquareHole(width=5)
    with pytest.raises(TypeError, match="Object must implement get_width\\(\\) method"):
        hole.fits(InvalidObject())




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


def test_mocked_adapter_get_width_called_multiple_times():
    """Test that get_width() can be called multiple times consistently."""
    mock_adapter = MagicMock()
    mock_adapter.get_width.return_value = 4.0

    hole = SquareHole(width=5)
    
    # Call fits multiple times
    result1 = hole.fits(mock_adapter)
    result2 = hole.fits(mock_adapter)
    
    assert result1 is True
    assert result2 is True
    assert mock_adapter.get_width.call_count == 2


# Testing the full adapter pattern flow
def test_adapter_pattern_integration_multiple_circles():
    """Test the complete adapter pattern with multiple circles and holes."""
    circles = [
        Circle(radius=1),    # diameter = 2
        Circle(radius=2.5),  # diameter = 5
        Circle(radius=4),    # diameter = 8
        Circle(radius=6),    # diameter = 12
    ]
    
    hole = SquareHole(width=7)
    
    expected_results = [True, True, False, False]
    
    for i, circle in enumerate(circles):
        adapter = CircleAdapter(circle)
        result = hole.fits(adapter)
        assert result == expected_results[i], f"Circle {i} (radius={circle.radius}) failed"


def test_circle_adapter_preserves_original_circle():
    """Test that the adapter doesn't modify the original circle."""
    original_radius = 3.5
    circle = Circle(radius=original_radius)
    adapter = CircleAdapter(circle)
    
    # Use the adapter
    _ = adapter.get_width()
    
    # Verify original circle is unchanged
    assert circle.get_radius() == original_radius


def test_multiple_adapters_same_circle():
    """Test that multiple adapters can be created for the same circle."""
    circle = Circle(radius=2)
    adapter1 = CircleAdapter(circle)
    adapter2 = CircleAdapter(circle)
    
    hole = SquareHole(width=5)
    
    assert hole.fits(adapter1) is True
    assert hole.fits(adapter2) is True
    assert adapter1.get_width() == adapter2.get_width()


# 📊 PARAMETRIZED TESTS — Testing multiple scenarios efficiently
@pytest.mark.parametrize("radius,hole_width,expected", [
    (1, 3, True),     # diameter=2, fits easily
    (2, 4, True),     # diameter=4, exact fit
    (2.5, 4, False),  # diameter=5, too big
    (3, 5, False),    # diameter=6, too big
    (0.1, 1, True),   # very small circle
    (10, 15, False),  # large circle, smaller hole
])
def test_various_circle_hole_combinations(radius, hole_width, expected):
    """Test various combinations of circle sizes and hole widths."""
    circle = Circle(radius=radius)
    adapter = CircleAdapter(circle)
    hole = SquareHole(width=hole_width)
    
    assert hole.fits(adapter) is expected