import math

class Vector(object):

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
vec1 = Vector(4,5)
vec2 = Vector(2,3)
vec = vec1 + vec2

print(vec.x)
print(vec.y)

