from typing import List, Optional

from suitebot3.game.ant import Ant
from suitebot3.game.direction import Direction
from suitebot3.game.game_state import GameState


class Moves:
    def __init__(self,
                 spawn_new_ant: bool,
                 directions: List[Optional[Direction]]):
        self.spawn_new_ant = spawn_new_ant
        self.directions = directions

    def serialize(self) -> str:
        serialized = ''

        for direction in self.directions:
            if direction is not None:
                serialized += str(direction)
            else:
                serialized += 'H'

        if self.spawn_new_ant:
            serialized += 'S'

        return serialized


class MovesBuilder:
    def __init__(self,
                 game_state: GameState,
                 player_id: int):
        self.my_ants = game_state.get_ants_of_player(player_id)
        self.ant_directions = [None for ant in self.my_ants]
        self.should_spawn_new_ant = False

    def move_ant(self, ant: Ant, direction: Direction) -> 'MovesBuilder':
        index = self.my_ants.index(ant)
        self.ant_directions[index] = direction
        return self

    def spawn_new_ant(self) -> 'MovesBuilder':
        self.should_spawn_new_ant = True
        return self

    def build(self) -> Moves:
        return Moves(self.should_spawn_new_ant, self.ant_directions)