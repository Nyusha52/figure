from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestTriangle:
    def test_name_triangle(self):
        c = Triangle(1, 1, 1)
        assert c.name == "Triangle"

    def test_area_1_triangle(self):
        c = Triangle(2, 2, 3)
        assert c.area == 1.98

    def test_negative_number_aria_triangle_1(self):
        c = Triangle(-1, 1, 2)
        assert c.area is None

    def test_negative_number_aria_triangle_2(self):
        c = Triangle(1, -1, 2)
        assert c.area is None

    def test_negative_number_aria_triangle_3(self):
        c = Triangle(1, 1, -2)
        assert c.area is None

    def test_negative_number_perimetr_triangle_1(self):
        c = Triangle(-1, 1, 2)
        assert c.perimeter is None

    def test_negative_number_perimetr_triangle_2(self):
        c = Triangle(1, -1, 2)
        assert c.perimeter is None

    def test_negative_number_perimetr_triangle_3(self):
        c = Triangle(1, 1, -2)
        assert c.perimeter is None

    def test_string_aria_triangle_1(self):
        c = Triangle("-1", 2, 2)
        assert c.area is None

    def test_string_aria_triangle_2(self):
        c = Triangle(2, "-1", 2)
        assert c.area is None

    def test_string_aria_triangle_3(self):
        c = Triangle(2, 2, "-1")
        assert c.area is None

    def test_string_perimetr_triangle_1(self):
        c = Triangle("-1", 2, 2)
        assert c.perimeter is None

    def test_string_perimetr_triangle_2(self):
        c = Triangle(2, "-1", 2)
        assert c.perimeter is None

    def test_string_perimetr_triangle_3(self):
        c = Triangle(2, 2, "-1")
        assert c.perimeter is None

    def test_area_big_number_triangle(self):
        c = Triangle(199, 250, 320)
        assert c.area == 24874.89

    def test_area_float_triangle(self):
        c = Triangle(1.1, 3.3, 4.1)
        assert round(c.area, 1) == 1.4

    def test_perimeter_float_triangle(self):
        c = Triangle(1.1, 3.3, 4.1)
        assert round(c.perimeter, 1) == 8.5

    def test_add_area_rectangle_triangle(self):
        c = Triangle(3, 5, 3)
        r = Rectangle(3, 3)
        assert round(c.add_area(r), 1) == 13.2

    def test_add_area_triangle_circle(self):
        c = Triangle(25, 27, 15)
        c1 = Circle(2)
        assert round(c.add_area(c1), 1) == 197.6

    def test_add_area_triangle_square(self):
        c = Triangle(23, 27, 15)
        r = Square(5)
        assert c.add_area(r) == 197.39

    def test_add_area_triangle_triangle(self):
        c = Triangle(21, 30, 15)
        r = Triangle(3, 3, 2)
        assert c.add_area(r) == 149.06

    def test_add_area_triangle_str(self):
        c = Triangle(21, 30, 15)
        r = "f"
        assert c.add_area(r) is None

    def test_add_area_triangle_int(self):
        c = Triangle(21, 30, 15)
        r = 1
        assert c.add_area(r) is None
