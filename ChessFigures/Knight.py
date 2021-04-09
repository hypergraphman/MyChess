from constants import *
from ChessFigures.Figure import *


class Knight(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wK'
        return 'bK'

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if abs(col1 - col) * abs(row1 - row) == 2:
            return True
        return False