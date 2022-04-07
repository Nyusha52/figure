from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestCircle:
    def test_name_circle(self):
        c = Circle(1)
        assert c.name == "Circle"

    def test_area_1_circle(self):
        c = Circle(1)
        assert c.area == 3.14

    def test_negative_number_aria_circle(self):
        c = Circle(-1)
        assert c.area is None

    def test_negative_number_perimetr_circle(self):
        c = Circle(-1)
        assert c.perimeter is None

    def test_string_aria_circle(self):
        c = Circle("-1")
        assert c.area is None

    def test_string_perimetr_circle(self):
        c = Circle("-1")
        assert c.perimeter is None

    def test_area_99_circle(self):
        c = Circle(99)
        assert c.area == 30775.14

    def test_area_1_1_circle(self):
        c = Circle(1.1)
        assert round(c.area, 1) == 3.8

    def test_perimeter_100_circle(self):
        c = Circle(100)
        assert c.perimeter == 628.0

    def test_perimeter_1_1_circle(self):
        c = Circle(1.1)
        assert round(c.perimeter, 1) == 6.9

    def test_add_area_rectangle_circle(self):
        c = Circle(1)
        r = Rectangle(3, 3)
        assert round(c.add_area(r), 1) == 12.1

    def test_add_area_curcle_circle(self):
        c = Circle(1)
        c1 = Circle(2)
        assert round(c.add_area(c1), 1) == 15.7

    def test_add_area_circle_square(self):
        c = Circle(1)
        r = Square(5)
        assert c.add_area(r) == 28.14

    def test_add_area_circle_triangle(self):
        c = Circle(2)
        r = Triangle(3, 3, 2)
        assert c.add_area(r) == 15.39
