
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Общее описание решения
Решение представляет собой набор функций для расчета площади и периметра различных геометрических фигур: круга, квадрата и треугольника. Функции реализованы в отдельных модулях (circle.py, square.py, triangle.py) и могут быть использованы для расчета соответствующих величин.

# Функции
## Круг
### Площадь круга
Возвращает площадь круга по формуле πr^2
- Пример вызова:
    print(area(2))
    -> 12,566370614359172
### Периметр круга
Возвращает периметр круга по формуле 2πr
- Пример вызова:
    print(perimeter(5))
    -> 31.41592653589793

## Квадрат
### Площадь квадрата
Возвращает площадь квадрата по формуле a^2
- Пример вызова:
    print(area(2))
    -> 4
### Периметр квадрата
Возвращает периметр квадрата по формуле 4a
- Пример вызова:
    print(perimeter(5))
    -> 20

## Треугольник
### Полупериметр треугольника
Возвращает полупериметр треугольника по формуле (a + b + c) / 2
- Пример вызова:
    print(area(2, 5, 7))
    -> 7
### Периметр треугольника
Возвращает периметр треугольника по формуле a + b + c
- Пример вызова:
    print(perimeter(2, 5, 7))
    -> 14
  
## Основная функция
### Функция для расчета периметра или площади фигуры

def calc(fig, func, size): 
    # Проверяем, что фигура и функция являются допустимыми значениями 
    assert fig in figs 
    assert func in funcs 

    # Вызываем соответствующую функцию из импортированного модуля 
    # с помощью eval и выводим результат 
    result = eval(f'{fig}.{func}(*{size})') 
    print(f'{func} of {fig} is {result}') 

- Примеры вызова функций:
1. calc('circle', 'area', [5])  # расчет площади круга радиуса 5 

Результат: area of circle is 78.5
2. calc('square', 'perimeter', [4])  # расчет периметра квадрата со стороной 4 

Результат: perimeter of square is 16
3. calc('circle', 'perimeter', [3])  # расчет периметра круга радиуса 3 

Результат: perimeter of circle is 18.84

### Использование
Для использования функций необходимо импортировать соответствующие модули и вызвать функцию calc с необходимыми аргументами.

- Пример использования:

import circle

import square


figs = ['circle', 'square']

funcs = ['perimeter', 'area']


calc('circle', 'area', [5])  # расчет площади круга радиуса 5

calc('square', 'perimeter', [4])  # расчет периметра квадрата со стороной 4

# История изменения проекта с хешами комитов
- commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (HEAD -> develop_kozzitch, origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

- commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

- commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

- commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

