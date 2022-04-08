import math

from src.Figure import Figure
from src.decorator import exept


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side1, side2, side3):
        try:
            if side1 < 0 or side2 < 0 or side3 < 0:
                raise ValueError
            if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
                raise ValueError
            else:
                self.side1 = side1
                self.side2 = side2
                self.side3 = side3
        except TypeError:
            print("Нельзя создать такой треугольник")
        except ValueError:
            print("Нельзя создать такой треугольник")

    @property
    @exept
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    @exept
    def area(self):
        half_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = round(math.sqrt(half_perimeter * (half_perimeter - self.side1) * (half_perimeter - self.side2) * (
                half_perimeter - self.side3)), 2)
        return area
