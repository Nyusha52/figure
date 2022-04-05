import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle


class TestCircle:
    def test_name(self):
        c = Circle(1)
        assert c.name == "Circle"

    def test_area_1(self):
        c = Circle(1)
        assert c.area == 3.14

    def test_area_99(self):
        c = Circle(99)
        assert c.area == 30775.14

    def test_area_100(self):
        c = Circle(100)
        assert c.area == 31400.00

    def test_area_100(self):
        c = Circle("100")
        assert c.area == TypeError

    def test_add_area_rectangle(self):
        c = Circle(1)
        r = Rectangle(3, 3)
        assert c.add_area(r) == 12.14
