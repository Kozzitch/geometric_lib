import pytest
import triangle
import math


def test_triangle_area():
    side1 = 3
    side2 = 4
    side3 = 5
    semiperimeter = (side1 + side2 + side3) / 2
    expected_area = math.sqrt(semiperimeter *
        (semiperimeter - side1) * (semiperimeter - side2) *
            (semiperimeter - side3))
    result = triangle.area(side1, side2, side3)
    assert result == pytest.approx(expected_area)


def test_triangle_perimeter():
    side1 = 3
    side2 = 4
    side3 = 5
    expected_perimeter = side1 + side2 + side3
    result = triangle.perimeter(side1, side2, side3)
    assert result == expected_perimeter
