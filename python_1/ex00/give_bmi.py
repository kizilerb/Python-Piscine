import numpy as np
import sys


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi_values = []
    try:
        if not isinstance(height, (list, int)) or not isinstance(weight, (list,int)):
            raise TypeError("Values shuould be integer or float")
        elif len(height) != len(weight):
            raise ValueError("Number of height and weight inputs should be equal")
        elif height <= 0 or weight <= 0:
            raise ValueError("Values of height and weight should be positive.")
        else:
            bmi_values.append(weight/(height**2))
    except Exception as e:
        print("Error:", e)
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here
    