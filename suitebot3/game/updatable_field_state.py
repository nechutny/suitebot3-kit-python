from typing import Optional

from suitebot3.game.ant import Ant
from suitebot3.game.field_state import FieldState
from suitebot3.game.game_constants import GameConstants


class UpdatableFieldState(FieldState):
    def __init__(self, base: Optional[int]):
        self.ant = None
        self.base = base
        self.resources = 0 if base else GameConstants.FIELD_INITIAL_RESOURCES

    def get_resource_count(self) -> int:
        return self.resources

    def get_ant(self) -> Optional[Ant]:
        return self.ant

    def get_base(self) -> Optional[int]:
        return self.base
