# === Adaptee (Legacy API) ===
class Circle:
    
    
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        self.radius = radius

    def get_radius(self) -> float:
        
        return self.radius


# === Target Interface ===
class SquareHole:
    
    
    def __init__(self, width: float):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        self.width = width

    def fits(self, square_object) -> bool:
            
        return square_object.get_width() <= self.width


# === Adapter ===
class CircleAdapter:
    
    
    def __init__(self, circle: Circle):
       
        self.circle = circle

    def get_width(self) -> float:
        
        return self.circle.get_radius() * 2


# === Demo / Main block ===
def main():
    
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