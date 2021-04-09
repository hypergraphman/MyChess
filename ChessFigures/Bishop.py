from constants import *
from ChessFigures.Figure import *


class Bishop(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wB'
        return 'bB'

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) == abs(col - col1):
            return True
        return False
