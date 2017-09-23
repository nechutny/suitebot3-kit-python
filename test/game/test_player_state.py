import unittest

from suitebot3.game.point import Point
from suitebot3.game.player_state import PlayerState


class TestPlayerState(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.player_state = PlayerState(1)
        self.player_state.spawn_new_ant(Point(1, 2))

    def test_get_ant(self):
        self.assertEquals(self.player_state.ants[0].get_position(), Point(1, 2))

    def test_kill_ant(self):
        self.player_state.kill_ant(self.player_state.ants[0])
        self.assertEquals(self.player_state.ants, [])

    def test_kill_ant_2(self):
        self.player_state.ants[0].kill()
        self.assertEquals(self.player_state.ants, [])

    def test_get_player(self):
        self.assertEquals(self.player_state.player_id, 1)
        self.assertEquals(self.player_state.ants[0].get_player(), 1)