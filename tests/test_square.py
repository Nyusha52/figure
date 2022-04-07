from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestSquare:
    def test_name_square(self):
        c = Square(1)
        assert c.name == "Square"

    def test_area_1_square(self):
        c = Square(2)
        assert c.area == 4

    def test_negative_number_aria_square(self):
        c = Square(-1)
        assert c.area is None

    def test_negative_number_perimetr_square(self):
        c = Square(-1)
        assert c.perimeter is None

    def test_string_aria_square(self):
        c = Square("-1")
        assert c.area is None

    def test_string_perimetr_square(self):
        c = Square("-1")
        assert c.perimeter is None

    def test_area_big_number_square(self):
        c = Square(199)
        assert c.area == 39601

    def test_area_float_square(self):
        c = Square(1.1)
        assert round(c.area, 1) == 1.2

    def test_perimeter_float_square(self):
        c = Square(1.1)
        assert round(c.perimeter, 1) == 4.4

    def test_add_area_rectangle_square(self):
        c = Square(3)
        r = Rectangle(3, 3)
        assert round(c.add_area(r), 1) == 18

    def test_add_area_square_circle(self):
        c = Square(25)
        c1 = Circle(2)
        assert round(c.add_area(c1), 1) == 637.6

    def test_add_area_square_square(self):
        c = Square(23)
        r = Square(5)
        assert c.add_area(r) == 554

    def test_add_area_square_triangle(self):
        c = Square(21)
        r = Triangle(3, 3, 2)
        assert c.add_area(r) == 443.83
