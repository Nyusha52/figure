from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius
        self.__perimeter = 2 * 3.14 * radius
        self.__area = 3.14 * radius ** 2

    @property
    def perimeter(self):
        return self.perimeter

    @property
    def area(self):
        return self.area


c = Circle(1)
print(c.area())
