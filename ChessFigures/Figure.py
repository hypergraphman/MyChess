class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # Реализация проверки хода в каждой фигуре своя
        pass

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)