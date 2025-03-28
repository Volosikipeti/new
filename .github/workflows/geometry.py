from math import pi

def calculate_area(shape, **params):
    """
    Универсальная функция для вычисления площади различных фигур.

    :param shape: Тип фигуры ('rectangle', 'square', 'circle').
    :param params: Словарь параметров (width, height, side, radius).
    :return: Площадь фигуры.
    """
    formulas = {
        "rectangle": lambda p: p["width"] * p["height"],  
        "square": lambda p: p["side"] ** 2,
        "circle": lambda p: pi * p["radius"] ** 2
    }

    if shape not in formulas:
        raise ValueError(f"Unsupported shape: {shape}")

    return formulas[shape](params)
