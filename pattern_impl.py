import math
from typing import Protocol


# === Protocol for better type safety ===
class WidthProvider(Protocol):
    """Protocol defining the interface expected by SquareHole."""
    def get_width(self) -> float:
        """Return the width needed to fit through a square hole."""
        ...


# === Adaptee (Legacy API) ===
class Circle:
    """A circle with a given radius."""
    
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        self.radius = radius

    def get_radius(self) -> float:
        """Get the radius of the circle."""
        return self.radius


# === Target Interface ===
class SquareHole:
    """A square hole that objects can fit through."""
    
    def __init__(self, width: float):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        self.width = width

    def fits(self, square_object: WidthProvider) -> bool:
        """Check if the object (must implement get_width) fits in the square hole."""
        try:
            return square_object.get_width() <= self.width
        except AttributeError:
            raise TypeError("Object must implement get_width() method")


# === Adapter ===
class CircleAdapter:
    """Adapter that allows a Circle to work with SquareHole interface."""
    
    def __init__(self, circle: Circle):
        if not isinstance(circle, Circle):
            raise TypeError("Adapter requires a Circle object.")
        self.circle = circle

    def get_width(self) -> float:
        """Calculate the minimum square width needed for the circle to fit through.
        
        A circle needs a square hole with width >= diameter to fit through.
        """
        return self.circle.get_radius() * 2


# === Demo / Main block ===
def main():
    """Simple demonstration of the adapter pattern."""
    print("=== Adapter Pattern Demo ===")
    
    hole = SquareHole(width=8)
    
    



    print("\nTrying with a Circle of radius 3 (diameter=6):")
    circle1 = Circle(radius=3)
    # This won't work:
    # hole.fits(circle1)  # Raises TypeError because Circle does not implement get_width()
    # This works with adapter:
    adapter1 = CircleAdapter(circle1)
    print("Fits:", hole.fits(adapter1))  # Should print: Fits: True

    print("\nTrying with a Circle of radius 6 (diameter=12):")
    circle2 = Circle(radius=6)
    adapter2 = CircleAdapter(circle2)
    print("Fits:", hole.fits(adapter2))  # Should print: Fits: False


if __name__ == "__main__":
    main()