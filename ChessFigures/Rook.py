from constants import *
from ChessFigures.Figure import *


class Rook(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wR'
        return 'bR'

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        if row1 != row and col1 != col:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False

        return True