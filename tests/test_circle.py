import pytest
from src.Circle import Circle


class TestCircle:
    def test_name(self):
        c = Circle(1)
        assert c.name == "Circle"

    def test_area(self):
        c = Circle(1)
        assert c.area == 3.14
