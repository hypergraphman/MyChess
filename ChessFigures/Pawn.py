from constants import *
from ChessFigures.Figure import *


class Pawn(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wP'
        return 'bP'

    def can_move(self, row, col):
        return True