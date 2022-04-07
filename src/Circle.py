from src.Figure import Figure
from src.decorator import exept


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        try:
            if radius > 0:
                self.radius = radius
            else:
                raise ValueError
        except TypeError:
            print("Нельзя создать такой круг")
        except ValueError:
            print("Нельзя создать такой круг")

    @property
    @exept
    def perimeter(self):
        return 2 * 3.14 * self.radius

    @property
    @exept
    def area(self):
        return 3.14 * self.radius ** 2
