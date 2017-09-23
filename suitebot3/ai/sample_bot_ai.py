import random

from suitebot3.game.direction import Directions
from suitebot3.ai.bot_ai import BotAi
from suitebot3.game.game_setup import GameSetup
from suitebot3.game.game_state import GameState
from suitebot3.game.moves import Moves, MovesBuilder


class SampleBotAi(BotAi):

    DIRECTIONS = [ Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT ]

    def __init__(self, game_setup: GameSetup):
        ''' Called before each new game '''
        self.my_id = game_setup.ai_player_id

    def make_moves(self, game_state: GameState) -> Moves:

        moves = MovesBuilder(game_state, self.my_id)

        if len(game_state.get_ants_of_player(self.my_id)) < 5:
            moves.spawn_new_ant()

        for my_ant in game_state.get_ants_of_player(self.my_id):
            moves.move_ant(my_ant, random.choice(self.DIRECTIONS))

        return moves.build()
