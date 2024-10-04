# Импортируем модуль math для использования константы π
import math

# Функция для расчета площади круга
def area(r):
    ''' 
    Возвращает площадь круга по формуле πr^2 
    Пример вызова: 
    print(area(2))
    -> 12,566370614359172
    '''
    return math.pi * r * r

# Функция для расчета периметра круга
def perimeter(r):
    ''' 
    Возвращает периметр круга по формуле 2πr 
    Пример вызова:
    print(perimeter(5))
    -> 31.41592653589793
    '''

    return 2 * math.pi * r
