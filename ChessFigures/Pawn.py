from constants import *
from ChessFigures.Figure import *


class Pawn(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wP'
        return 'bP'

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col1 != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row1 + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if row1 == start_row and row1 + 2 * direction == row and \
           board.field[row + direction][col] is None:
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))