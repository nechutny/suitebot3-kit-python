import unittest

from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point


class TestGamePlan(unittest.TestCase):

    def test_check_is_on_plan(self):
        game_plan = GamePlan(5, 10, {}, 1)
        self.assertRaises(RuntimeError, game_plan.check_is_on_plan, Point(5, 0))
        self.assertRaises(RuntimeError, game_plan.check_is_on_plan, Point(4, 10))
        self.assertRaises(RuntimeError, game_plan.check_is_on_plan, Point(-1, 0))
        self.assertRaises(RuntimeError, game_plan.check_is_on_plan, Point(0, -1))
        game_plan.check_is_on_plan(Point(0, 0))

    def test_iterator(self):
        game_plan = GamePlan(3, 4, {}, 1)

        positions = set()
        for position in game_plan:
            positions.add(position)

        self.assertEquals(len(positions), 12)
        self.assertTrue(Point(0, 0) in positions)
        self.assertTrue(Point(2, 3) in positions)
        self.assertTrue(Point(1, 0) in positions)
