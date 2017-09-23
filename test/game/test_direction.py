import unittest

from suitebot3.game.direction import Directions, string_2_direction
from suitebot3.game.point import Point


class TestSimpleServer(unittest.TestCase):

    def test_point_transformation(self):
        source = Point(3, 7)

        self.assertEquals(Directions.UP.fromPoint(source), Point(3, 6))
        self.assertEquals(Directions.DOWN.fromPoint(source), Point(3, 8))
        self.assertEquals(Directions.LEFT.fromPoint(source), Point(2, 7))
        self.assertEquals(Directions.RIGHT.fromPoint(source), Point(4, 7))

    def test_from_string(self):
        self.assertEquals(string_2_direction('U'), Directions.UP)
        self.assertEquals(string_2_direction('D'), Directions.DOWN)
        self.assertEquals(string_2_direction('L'), Directions.LEFT)
        self.assertEquals(string_2_direction('R'), Directions.RIGHT)
        self.assertEquals(string_2_direction('H'), None)
        self.assertEquals(string_2_direction(''), None)
        self.assertEquals(string_2_direction(' '), None)
        self.assertEquals(string_2_direction('None'), None)

