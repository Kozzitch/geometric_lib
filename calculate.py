# Импортируем модули для работы с кругом и квадратом
import circle
import square

# Списки доступных фигур и функций
figs = ['circle', 'square']
funcs = ['perimeter', 'area']

# Словарь для хранения информации о размерах фигур
sizes = {}

# Функция для расчета периметра или площади фигуры
def calc(fig, func, size):
    # Проверяем, что фигура и функция являются допустимыми значениями
    assert fig in figs
    assert func in funcs

    # Вызываем соответствующую функцию из импортированного модуля
    # с помощью eval и выводим результат
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

    ''' 
    Примеры вызова функций:
    calc('circle', 'area', [5])  # расчет площади круга радиуса 5
    Результат: area of circle is 78.5
    calc('square', 'perimeter', [4])  # расчет периметра квадрата со стороной 4
    Результат: perimeter of square is 16
    calc('circle', 'perimeter', [3])  # расчет периметра круга радиуса 3
    Результат: perimeter of circle is 18.84
    '''
if __name__ == "__main__":
    # Инициализируем переменные для хранения имени фигуры, имени функции и размеров
    func = ''
    fig = ''
    size = list()

    # Цикл для ввода имени фигуры
    while fig not in figs:
        fig = input(f"Введите имя фигуры, доступны следующие значения: {figs}:\n")

    # Цикл для ввода имени функции
    while func not in funcs:
        func = input(f"Введите имя функции, доступны следующие значения: {funcs}:\n")

    # Цикл для ввода размеров фигуры
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Введите размеры фигуры через пробел, 1 для круга и квадрата\n").split(' ')))

    # Вызываем функцию calc для расчета и вывода результата
    calc(fig, func, size)
