from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * 3.14 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2
