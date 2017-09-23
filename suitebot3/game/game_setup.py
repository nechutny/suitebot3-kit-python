from typing import Iterable, Any

from suitebot3.game.game_plan import GamePlan
from suitebot3.game.game_state_creator import create_player_list_from_dto, create_game_plan_from_dto


class GameSetup:
    def __init__(self,
                 ai_player_id: int,
                 player_ids: Iterable[int],
                 game_plan: GamePlan):
        self.ai_player_id = ai_player_id
        self.player_ids = tuple([int(player_id) for player_id in player_ids])
        self.game_plan = game_plan


def dto_2_game_setup(dto: Any) -> GameSetup:
    return GameSetup(dto['aiPlayerId'], create_player_list_from_dto(dto), create_game_plan_from_dto(dto))