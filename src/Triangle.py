import math

from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return round(math.sqrt(half_perimeter * (half_perimeter - self.side1) * (half_perimeter - self.side2)
                               * (half_perimeter - self.side3)), 2)
