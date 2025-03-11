def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    bmi_values = []
    try:
        if len(height) != len(weight):
            raise ValueError("Number of inputs should be equal")
        for h, w in zip(height, weight):
            if (not isinstance(h, (float, int))
                    or not isinstance(w, (float, int))):
                raise TypeError("Values should be integer or float")
            if h <= 0 or w <= 0:
                raise ValueError("Values of should be positive.")
            else:
                bmi_values.append(w/(h**2))
    except Exception as e:
        print("Error:", e)
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    limit_check = []
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit should be an integer.")
        else:
            limit_check.append(list(True if i > limit else False for i in bmi))
    except TypeError as e:
        print("Type error:", e)
    return (limit_check)
