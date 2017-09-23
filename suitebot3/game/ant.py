from abc import ABCMeta, abstractmethod

from suitebot3.game.direction import Direction


class Ant:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_player(self) -> int:
        ''' The player id of the owner '''

    @abstractmethod
    def get_position(self) -> int:
        ''' Current position of the ant '''

    def get_last_move(self) -> Direction:
        ''' Returns the last direction in which the ant moved or None '''