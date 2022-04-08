from src.Figure import Figure
from src.decorator import exept


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, side1, side2):
        try:
            if side1 > 0 and side2 > 0:
                self.side1 = side1
                self.side2 = side2
            else:
                raise ValueError
        except TypeError:
            print("Нельзя создать такой прямоугольник")
        except ValueError:
            print("Нельзя создать такой прямоугольник")

    @property
    @exept
    def perimeter(self):
        return (self.side1 + self.side2) * 2

    @property
    @exept
    def area(self):
        return self.side1 * self.side2
