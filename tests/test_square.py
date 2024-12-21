import square


def test_square_area():
    side = 5
    expected_area = side * side
    result = square.area(side)
    assert result == expected_area


def test_square_perimeter():
    side = 5
    expected_perimeter = 4 * side
    result = square.perimeter(side)
    assert result == expected_perimeter
