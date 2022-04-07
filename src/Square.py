from src.Figure import Figure
from src.decorator import exept


class Square(Figure):
    name = 'Square'

    def __init__(self, side):
        try:
            if side > 0:
                self.side = side
            else:
                raise ValueError
        except TypeError:
            print("Нельзя создать такой квадрат")
        except ValueError:
            print("Нельзя создать такой квадрат")

    @property
    @exept
    def perimeter(self):
        return self.side * 4

    @property
    @exept
    def area(self):
        area = self.side ** 2
        return area
