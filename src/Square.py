from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.side = side
        self.name = 'Square'
        self.perimeter = side * 4
        self.half_perimeter = self.perimeter / 2
        self.area = side**2


