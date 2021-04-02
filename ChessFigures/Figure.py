

class Figure:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

    def get_color(self):
        return self.color

    def set_position(self, row, col):
        self.row, self.col = row, col