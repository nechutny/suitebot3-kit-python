from typing import Optional

from suitebot3.game.point import Point


class Direction(object):
    def __init__(self, dx: int, dy: int, char: str) -> None:
        self.dx = dx
        self.dy = dy
        self.char = char

    def __str__(self) -> str:
        return self.char

    def fromPoint(self, point: Point) -> Point:
        return Point(point.x + self.dx, point.y + self.dy)


class Directions:
    UP = Direction(0, -1, "U")
    DOWN = Direction(0, 1, "D")
    LEFT = Direction(-1, 0, "L")
    RIGHT = Direction(1, 0, "R")


def string_2_direction(c: str) -> Optional[Direction]:
    if c == "U": return Directions.UP
    elif c == "D": return Directions.DOWN
    elif c == "L": return Directions.LEFT
    elif c == "R": return Directions.RIGHT
    else: return None
