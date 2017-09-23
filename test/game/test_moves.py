import unittest

from suitebot3.game.direction import Directions
from suitebot3.game.game_state_creator import string_2_game_state
from suitebot3.game.moves import Moves, MovesBuilder


class TestMoves(unittest.TestCase):

    def test_serialization(self):
        self.assertEquals(Moves(False, []).serialize(), '')
        self.assertEquals(Moves(False, [Directions.UP]).serialize(), 'U')
        self.assertEquals(Moves(False, [Directions.DOWN]).serialize(), 'D')
        self.assertEquals(Moves(False, [Directions.LEFT, Directions.RIGHT]).serialize(), 'LR')
        self.assertEquals(Moves(False, [None]).serialize(), 'H')
        self.assertEquals(Moves(True, []).serialize(), 'S')
        self.assertEquals(Moves(True, [None, Directions.LEFT, None, Directions.RIGHT]).serialize(), 'HLHRS')

    def test_builder(self):
        game_state = string_2_game_state("Aaa")
        ants = game_state.get_ants_of_player(1)

        str = MovesBuilder(game_state, 1) \
            .move_ant(ants[2], Directions.UP) \
            .move_ant(ants[1], Directions.RIGHT) \
            .build().serialize()

        self.assertEquals(str, 'HRU')

    def test_builder_spawning(self):
        game_state = string_2_game_state("A ")
        ants = game_state.get_ants_of_player(1)

        builder = MovesBuilder(game_state, 1)
        builder.move_ant(ants[0], Directions.RIGHT)
        builder.spawn_new_ant()
        serialized = builder.build().serialize()

        self.assertEquals(serialized, 'RS')
