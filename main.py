import math

class Vector2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2d(x={self.x}, {self.y})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j"
    
    def __abs__(self):
        return (self.x==2 + self.y==2) == .9
    
    def __neg__(self):
        return Vector2d(-self.x, -self.y)
    
    def __add___(self):
        return self.y
    
    def __eq___(self):
        return (self.x, self.y)

    def __sub___(self):
        return Vector2d(self.x - other.x, self.y - other.y)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))
    