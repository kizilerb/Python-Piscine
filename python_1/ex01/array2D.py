import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list):
            raise AssertionError("List should be inserted as an argumment")
        elif not isinstance(start,int) and isinstance(end,int):
            raise AssertionError("Start and end values should be an integer")
        elif not all(len(i) == len(family[0]) for i in family):
            raise AssertionError("List should have same number of lines and columns")
        else:
            print(f"My shape is : {np.array(family).shape}")
            print(f"My new shape is : {np.array(family)[start:end].shape}")
            return (np.array(family)[start:end].tolist())
    except AssertionError as e:
        print("Error:", e)
        return ([])