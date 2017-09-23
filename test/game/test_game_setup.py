import json
import unittest

from suitebot3.game.game_setup import dto_2_game_setup
from suitebot3.game.point import Point
from test.test_bot_request_handler import create_game_state_string


class TestGamePlan(unittest.TestCase):

    def test_dto_2_game_setup(self):
        game_setup = dto_2_game_setup(json.loads(create_game_state_string(5)))

        self.assertEquals(game_setup.ai_player_id, 1)

        self.assertEquals(game_setup.game_plan.width, 29)
        self.assertEquals(game_setup.game_plan.height, 30)
        self.assertEquals(len(game_setup.game_plan.starting_positions), 4)
        self.assertEquals(game_setup.game_plan.starting_positions[1], Point(5, 5))
        self.assertEquals(game_setup.game_plan.starting_positions[3], Point(20, 5))
        self.assertEquals(game_setup.game_plan.max_rounds, 149)

        self.assertEquals(len(game_setup.player_ids), 4)
        self.assertTrue(1 in game_setup.player_ids)
        self.assertTrue(2 in game_setup.player_ids)
        self.assertTrue(3 in game_setup.player_ids)
        self.assertTrue(4 in game_setup.player_ids)