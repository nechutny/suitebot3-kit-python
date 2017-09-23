import unittest

from suitebot3.game.point import Point


class TestPoint(unittest.TestCase):

    def test_values_accesible(self):
        self.assertEquals(Point(1, 2).x, 1)
        self.assertEquals(Point(1, 2).y, 2)

    def test_equality(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(2, 2) == Point(1, 2))