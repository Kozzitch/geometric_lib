# calculate.py
import math  # Используем только math, так как circle и square не нужны
# импортировать только то, что будет использовано
# import circle
# import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
}

def calc(fig, func, size):
    # Проверка корректности данных
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}. Available figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. Available functions are: {funcs}")
    if len(size) != sizes.get(f"{func}-{fig}", 1):
        raise ValueError(f"Invalid number of parameters for {fig} and {func}. Expected {sizes.get(f'{func}-{fig}', 1)} parameters.")

    # Выполнение расчёта
    try:
        result = eval(f'{fig}.{func}(*{size})')  # Этот подход следует рассматривать с осторожностью в реальном проекте
        return result
    except Exception as e:
        raise ValueError(f"Error in calculation: {e}")

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
