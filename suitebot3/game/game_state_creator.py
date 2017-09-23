from typing import Any, List

from suitebot3.game.direction import string_2_direction
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point
from suitebot3.game.standard_game_state import StandardGameState
from suitebot3.game.util.visualisation_util import VisualisationUtil

DEFAULT_MAX_ROUNDS = 150


def string_2_game_state(game_state_as_string: str) -> StandardGameState:
    """
    Creates a game state from a string representation.
    See VisualisationUtil.java for description of all available characters.
    In general:
     - Capital letters A-H are locations of home bases. Ants are placed on the home bases.
     - Small letters a-h represent ants.
     - Characters " .:-=+*#%@" are fields with different number of resources on it.
       ' '  has 0 resources,
       '.' a little bit
       ...
       '@' has maximum number of resources.
        
    For example the following will create 5x5 game plan.
    There will be:
     - 2 ants of player 1 (letters 'A' and 'a')
     - one ant of player 2 in the home base 'B'
     - little bit of resources in the upper left corner
     - lot of resources along the bottom line.
        
        ("...a \n"
         ".A   \n"
         "     \n"
         "  B  \n"
         "#####\n")
    """
    
    lines = game_state_as_string.splitlines()

    height = len(lines)
    width = len(lines[0])

    players = []
    starting_positions = {}

    for line in lines:
        if len(line) != width:
            raise Exception('String is not rectangular - all lines must have the same length.')

    for x in range(0, width):
        for y in range(0, height):
            c = lines[y][x]

            if c in VisualisationUtil.BASE_CHARS:
                player_id = VisualisationUtil.get_player_id(c)
                players.append(player_id)
                starting_positions[player_id] = Point(x, y)
            elif c not in VisualisationUtil.ANT_CHARS and c not in VisualisationUtil.RESOURCES_CHARS:
                raise Exception("Unknown character '" + c + "'")

    game_plan = GamePlan(width, height, starting_positions, DEFAULT_MAX_ROUNDS)
    game_state = StandardGameState(game_plan, players, True)

    for position, field in game_state.all_fields():
        c = lines[position.y][position.x]

        if c in VisualisationUtil.ANT_CHARS:
            game_state.spawn_ant(position, VisualisationUtil.get_player_id(c))
            game_state.set_resources_on_field(position, 0)
        elif c in VisualisationUtil.RESOURCES_CHARS:
            game_state.set_resources_on_field(position, VisualisationUtil.get_resources(c))
        elif c not in VisualisationUtil.BASE_CHARS:
            raise Exception("Unknown character '" + c + "'")

    return game_state


def dto_2_game_state(dto: Any) -> StandardGameState:
    players = create_player_list_from_dto(dto)
    game_plan = create_game_plan_from_dto(dto)

    game_state = StandardGameState(game_plan, players, False, dto["currentRound"], dto["remainingRounds"])

    for player_id_str, playerDto in dto["players"].items():
        player_id = int(player_id_str)
        ant_locations = playerDto["antLocations"]
        if len(ant_locations) != len(playerDto["antLastMoves"]):
            raise Exception("Array of antLocations has different length than antLastMoves")

        for i in range(0, len(ant_locations)):
            antLocation = Point(ant_locations[i]["x"], ant_locations[i]["y"])
            ant = game_state.spawn_ant(antLocation, player_id)
            ant.last_move = string_2_direction(playerDto["antLastMoves"][i])

        game_state.set_player_resources(player_id, playerDto["resources"])

    for position, field in game_state.all_fields():
        game_state.set_resources_on_field(position, dto["fieldResources"][position.x][position.y])

    return game_state


def create_player_list_from_dto(dto: Any) -> List[int]:
    return [int(player_id_str) for player_id_str in dto["players"].keys()]


def create_game_plan_from_dto(dto: Any) -> GamePlan:
    starting_positions = {
        int(player): Point(playerDto["homeBaseLocation"]["x"], playerDto["homeBaseLocation"]["y"]) for
        player, playerDto in dto["players"].items()}

    return GamePlan(dto["gamePlanWidth"], dto["gamePlanHeight"], starting_positions, dto["remainingRounds"] + dto["currentRound"] - 1)