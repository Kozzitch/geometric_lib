import pytest
import math
from calculate import calc

def test_calc_circle_area():
    result = calc('circle', 'area', [5])
    expected = math.pi * 5 * 5
    assert result == pytest.approx(expected)

def test_calc_square_area():
    result = calc('square', 'area', [5])
    expected = 5 * 5
    assert result == expected

def test_calc_circle_perimeter():
    result = calc('circle', 'perimeter', [5])
    expected = 2 * math.pi * 5
    assert result == pytest.approx(expected)

def test_calc_square_perimeter():
    result = calc('square', 'perimeter', [5])
    expected = 4 * 5
    assert result == expected

# Тестирование некорректных данных
def test_invalid_figure():
    with pytest.raises(ValueError):
        calc('rectangle', 'area', [5])

def test_invalid_function():
    with pytest.raises(ValueError):
        calc('circle', 'volume', [5])

def test_invalid_number_of_parameters():
    with pytest.raises(ValueError):
        calc('circle', 'area', [5, 10])

def test_invalid_size_type():
    with pytest.raises(ValueError):
        calc('square', 'area', ['five'])
