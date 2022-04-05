from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.name = 'Rectangle'
        self.perimeter = (side1 + side2) * 2
        self.half_perimeter = self.perimeter / 2
        self.area = side1 * side2
