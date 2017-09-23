import random

from suitebot3.game.ant import Ant
from suitebot3.game.direction import Directions
from suitebot3.ai.bot_ai import BotAi
from suitebot3.game.game_setup import GameSetup
from suitebot3.game.game_state import GameState
from suitebot3.game.moves import Moves, MovesBuilder
from suitebot3.game.point import Point


class SampleBotAi(BotAi):

    DIRECTIONS = [ Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT ]

    antDirections = {}

    startAntCount = 4
    startAntRound = 0

    incAntCount = 8
    incAntRound = 80


    def __init__(self, game_setup: GameSetup):
        ''' Called before each new game '''
        self.my_id = game_setup.ai_player_id
        self.antDirections = {}

    def createAnt(self, game_state: GameState, move: MovesBuilder):
        move.spawn_new_ant()
        index = len(game_state.get_ants_of_player(self.my_id))
        self.antDirections[ index ] = self.DIRECTIONS[ index % 4 ] #TODO: direction

    def getFieldInDirection(self, position: Point, direction, game_state: GameState):
        if direction == Directions.UP:
            position.y -= 1
        elif direction == Directions.DOWN:
            position.y += 1
        elif direction == Directions.RIGHT:
            position.x += 1
        elif direction == Directions.LEFT:
            position.x -= 1

        return game_state.get_field(position)

    def getDirection(self, ant : Ant, game_state: GameState):
        position = ant.get_position()

        up = self.getFieldInDirection(position, Directions.UP, game_state)
        down = self.getFieldInDirection(position, Directions.DOWN, game_state)
        left = self.getFieldInDirection(position, Directions.LEFT, game_state)
        right = self.getFieldInDirection(position, Directions.RIGHT, game_state)

        top = Directions.UP;
        topCount = up.get_resource_count();
        if(topCount < down.get_resource_count()):
            top = Directions.DOWN
            topCount = down.get_resource_count()

        if (topCount < left.get_resource_count()):
            top = Directions.LEFT
            topCount = left.get_resource_count()

        if (topCount < right.get_resource_count()):
            top = Directions.RIGHT
            topCount = right.get_resource_count()

        return top

    def make_moves(self, game_state: GameState) -> Moves:

        moves = MovesBuilder(game_state, self.my_id)

        if len(game_state.get_ants_of_player(self.my_id)) < self.startAntCount and game_state.get_current_round() >= self.startAntRound and game_state.get_current_round() < self.incAntRound:
            self.createAnt(game_state, moves)

        if len(game_state.get_ants_of_player(self.my_id)) < self.incAntCount and game_state.get_current_round() >= self.incAntRound:
            self.createAnt(game_state, moves)

        for my_ant in game_state.get_ants_of_player(self.my_id):
            direction = self.getDirection(my_ant, game_state);
            moves.move_ant(my_ant, direction)

        return moves.build()
