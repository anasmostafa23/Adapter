import math

# === Adaptee (Legacy API) ===
class Circle:
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius


# === Target Interface ===
class SquareHole:
    def __init__(self, width: float):
        self.width = width

    def fits(self, square_object) -> bool:
        """Check if the object (must implement get_width) fits in the square hole."""
        return square_object.get_width() <= self.width


# === Adapter ===
class CircleAdapter:
    def __init__(self, circle: Circle):
        self.circle = circle

    def get_width(self) -> float:
        # Calculate the width of the square that can contain this circle
        return self.circle.get_radius() * math.sqrt(2)


# === Demo / Main block ===
def main():
    hole = SquareHole(width=8)

    # Original square object interface is expected
    print("Trying with a Circle of radius 3:")
    circle1 = Circle(radius=3)
    adapter1 = CircleAdapter(circle1)
    print("Fits:", hole.fits(adapter1))  # Should print: Fits: True

    print("\nTrying with a Circle of radius 6:")
    circle2 = Circle(radius=6)
    adapter2 = CircleAdapter(circle2)
    print("Fits:", hole.fits(adapter2))  # Should print: Fits: False


if __name__ == "__main__":
    main()
