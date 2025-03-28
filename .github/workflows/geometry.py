def calculate_area(shape, **params):
    if shape == "rectangle":
        return params["width"] + params["height"]  # ❌ Ошибка: вместо * стоит +
