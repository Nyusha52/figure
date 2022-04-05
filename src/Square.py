from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def area(self):
        return self.side ** 2
