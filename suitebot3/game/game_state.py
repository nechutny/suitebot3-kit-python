from abc import ABCMeta, abstractmethod
from typing import List

from suitebot3.game.ant import Ant
from suitebot3.game.field_state import FieldState
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point


class GameState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_game_plan(self) -> GamePlan: pass

    @abstractmethod
    def is_game_over(self) -> bool: pass

    @abstractmethod
    def get_current_round(self) -> int: pass

    @abstractmethod
    def get_rounds_remaining(self) -> int: pass

    @abstractmethod
    def get_players(self) -> List[int]: pass

    @abstractmethod
    def get_ants_of_player(self, player_id: int) -> List[Ant]: pass

    @abstractmethod
    def get_player_resources(self, player_id: int) -> int: pass

    @abstractmethod
    def set_player_resources(self, player_id: int, resources: int) -> None: pass

    @abstractmethod
    def spawn_ant(self, position: Point, player_id: int) -> Ant: pass

    @abstractmethod
    def kill_ant(self, ant: Ant) -> None: pass

    @abstractmethod
    def move_ant(self, ant: Ant, target_position: Point) -> None: pass

    @abstractmethod
    def get_field(self, position: Point) -> FieldState: pass

    @abstractmethod
    def set_resources_on_field(self, position: Point, resources: int) -> None: pass



