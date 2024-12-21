import pytest
import circle
import math


def test_circle_area():
    radius = 5
    expected_area = math.pi * radius * radius
    result = circle.area(radius)
    assert result == pytest.approx(expected_area)


def test_circle_perimeter():
    radius = 5
    expected_perimeter = 2 * math.pi * radius
    result = circle.perimeter(radius)
    assert result == pytest.approx(expected_perimeter)

