from constants import *
from ChessFigures.Figure import *


class Queen(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wQ'
        return 'bQ'

    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) == abs(col - col1) or \
           row1 != row and col1 != col:
            return True
        return False