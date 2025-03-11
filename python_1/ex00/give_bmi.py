def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi_values = []
    try:
        if len(height) != len(weight):
            raise ValueError("Number of height and weight inputs should be equal")
        for h, w in zip(height, weight):
            if not isinstance(h, (float, int)) or not isinstance(w, (float,int)):
                raise TypeError("Values shuould be integer or float")
            if h <= 0 or w <= 0:
                raise ValueError("Values of height and weight should be positive.")
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


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()