from dataclasses import dataclass, field

@dataclass(order=True)
class Point:
    x: int = 5
    y: int = 5

@dataclass()
class Line:
    # coordinates: List[Point] = field(default_factory=list)
    coordinates: list[Point] = field(default_factory=list)

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point()
    print(p1)
    print(p2)
    print(p3)
    print(p1 == p2)
    print(p1 <= p2)
    
    # You can create a line with points
    line1 = Line(coordinates=[Point(), Point()])
    print(line1)

    # Or create an empty line that uses the default_factory
    empty_line = Line(["qweqwrqwrqwr"])
    print(empty_line)
    # help(Line)