import math

from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.name = 'Triangle'
        self.perimeter = side1 + side2 + side3
        self.half_perimeter = self.perimeter / 2
        self.area = round(math.sqrt(self.half_perimeter * (self.half_perimeter - side1) * (self.half_perimeter - side2)
                                    * (self.half_perimeter - side3)), 2)
