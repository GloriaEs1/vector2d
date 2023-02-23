class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector = {self.x}, {self.y}"
    def __str__(self):
        return f"({self.x}i + {self.y}j)"
    def __abs__(self):
        return self.x
    def __neg__(self):
        return "Vector(-self.x, -self.y)"
    def __add__(self):
        return self.y