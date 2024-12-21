import importlib

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
        raise ValueError(f"Invalid figure: {fig}. \
        Available figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. \
        Available functions are: {funcs}")
    if len(size) != sizes.get(f"{func}-{fig}", 1):
        raise ValueError(f"Invalid number of parameters \
        for {fig} and {func}. \
        Expected {sizes.get(f'{func}-{fig}', 1)} parameters.")

    # Динамический импорт модуля фигуры
    try:
        module = importlib.import_module(fig)  
        # Получение функции из модуля и её вызов
        func_to_call = getattr(module, func)  
        result = func_to_call(*size)
        return result
    except Exception as e:
        raise ValueError(f"Error in calculation: {e}")
