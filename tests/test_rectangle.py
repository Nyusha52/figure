from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestRectangle:
    def test_name_rectangle(self):
        c = Rectangle(1, 1)
        assert c.name == "Rectangle"

    def test_area_1_rectangle(self):
        c = Rectangle(2, 3)
        assert c.area == 6

    def test_negative_number_aria_triangle_1(self):
        c = Rectangle(-1, 1)
        assert c.area is None

    def test_negative_number_aria_triangle_2(self):
        c = Rectangle(1, -1)
        assert c.area is None

    def test_negative_number_perimetr_triangle_1(self):
        c = Rectangle(-1, 1)
        assert c.perimeter is None

    def test_negative_number_perimetr_triangle_2(self):
        c = Rectangle(1, -1)
        assert c.perimeter is None

    def test_string_aria_triangle_1(self):
        c = Rectangle("-1", 2)
        assert c.area is None

    def test_string_aria_triangle_2(self):
        c = Rectangle(2, "-1")
        assert c.area is None

    def test_string_perimetr_triangle_1(self):
        c = Rectangle("-1", 2)
        assert c.perimeter is None

    def test_string_perimetr_triangle_2(self):
        c = Rectangle(2, "-1")
        assert c.perimeter is None

    def test_area_big_number_triangle(self):
        c = Rectangle(199, 250)
        assert c.area == 49750

    def test_area_float_triangle(self):
        c = Rectangle(1.1, 3.3)
        assert round(c.area, 1) == 3.6

    def test_perimeter_float_triangle(self):
        c = Rectangle(1.1, 3.3)
        assert round(c.perimeter, 1) == 8.8

    def test_add_area_rectangle_triangle(self):
        c = Rectangle(3, 5)
        r = Rectangle(3, 3)
        assert round(c.add_area(r), 1) == 24

    def test_add_area_triangle_circle(self):
        c = Rectangle(25, 27)
        c1 = Circle(2)
        assert round(c.add_area(c1), 1) == 687.6

    def test_add_area_triangle_square(self):
        c = Rectangle(23, 27)
        r = Square(5)
        assert c.add_area(r) == 646

    def test_add_area_circle_triangle(self):
        c = Rectangle(21, 30)
        r = Triangle(3, 3, 2)
        assert c.add_area(r) == 632.83

    def test_add_area_rectangle_str(self):
        c = Rectangle(21, 30)
        r = "f"
        assert c.add_area(r) is None

    def test_add_area_rectangle_int(self):
        c = Rectangle(21, 30)
        r = 1
        assert c.add_area(r) is None
