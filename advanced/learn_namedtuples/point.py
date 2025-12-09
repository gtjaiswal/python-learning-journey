from collections import namedtuple
from typing import NamedTuple

'''
When to Use What?

NamedTuple: Simple, immutable data containers (API responses, coordinates)
Dataclass: When you need mutability, methods, or frozen=True for immutable with validation
Regular class: Complex behavior, inheritance hierarchies
'''

# Old way to create a namedtuple
Point = namedtuple('Point', ['x','y'])
p=Point(10,20)
print(p)
print(p.x, p.y)
print(p[0],p[0])

# New way to create a namedtuple
class Point(NamedTuple):
    x: int
    y: int

    def distance_from_origin(self) ->float:
        return (self.x**2 + self.y**2)**0.5
p1 = Point(3,4)
print(p1)
print(p1.distance_from_origin())