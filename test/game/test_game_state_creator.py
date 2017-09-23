import json
import unittest

from suitebot3.game.game_state_creator import string_2_game_state, dto_2_game_state
from suitebot3.game.point import Point
from test.test_bot_request_handler import create_game_state_string


class TestGameStateCreator(unittest.TestCase):

    def test_creating_from_valid_string(self):
        game_state = string_2_game_state(" A \n"
                                         "B  \n")

        self.assertEquals(game_state.game_plan.width, 3)
        self.assertEquals(game_state.game_plan.height, 2)

        self.assertEquals(game_state.get_field(Point(2, 0)).get_ant(), None)
        self.assertEquals(game_state.get_field(Point(1, 1)).get_ant(), None)
        self.assertEquals(game_state.get_field(Point(1, 0)).get_ant().get_player(), 1)

        self.assertEquals(len(game_state.get_players()), 2)
        self.assertEquals(game_state.get_ants_of_player(1)[0].get_position(), Point(1, 0))
        self.assertEquals(game_state.get_ants_of_player(2)[0].get_position(), Point(0, 1))

    def test_invalid_character_should_throw(self):
        self.assertRaises(Exception, string_2_game_state, ' A&')

    def test_non_rectangular_throws(self):
        self.assertRaises(Exception, string_2_game_state, '  \n   \n')

    def test_from_dto(self):
        game_state = dto_2_game_state(json.loads(create_game_state_string(5)))

        self.assertEquals(game_state.current_round, 5)
        self.assertEquals(game_state.rounds_remaining, 145)

        self.assertEquals(game_state.get_field(Point(0, 0)).get_resource_count(), 10)
        self.assertEquals(game_state.get_field(Point(20, 5)).get_resource_count(), 0)
        self.assertEquals(game_state.get_field(Point(20, 5)).get_base(), 3)
        self.assertEquals(game_state.get_field(Point(5, 5)).get_ant().get_player(), 1)

        self.assertEquals(game_state.game_plan.width, 29)
        self.assertEquals(game_state.game_plan.height, 30)


