from suitebot3.game.ant import Ant
from suitebot3.game.direction import Direction
from suitebot3.game.game_constants import GameConstants
from suitebot3.game.point import Point


class PlayerState:
    def __init__(self, player_id: int):
        self.ants = []
        self.resources = GameConstants.PLAYER_INITIAL_RESOURCES
        self.player_id = player_id

    def spawn_new_ant(self, position: Point) -> Ant:
        new_ant = _PlayersAnt(position, self)
        self.ants.append(new_ant)
        return new_ant

    def kill_ant(self, ant: Ant):
        self.ants.remove(ant)


class _PlayersAnt(Ant):
    def __init__(self,
                 position: Point,
                 player_state: PlayerState):
        self.position = position
        self.player_state = player_state
        self.last_move = None

    def get_player(self) -> int:
        return self.player_state.player_id

    def get_position(self) -> int:
        return self.position

    def get_last_move(self) -> Direction:
        return self.last_move

    def kill(self):
        self.player_state.kill_ant(self)


