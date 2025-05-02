import pandas as pd
import os


def path_check(path: str):
    try:
        if not os.path.exists(path) or not os.path.isfile(path):
            raise AssertionError("File path is wrong.")
        elif not path.lower().endswith(".csv"):
            raise AssertionError("File is not in a csv format.")
        return True
    except AssertionError as e:
        print("Error:", e)
        return False


def load(path: str) -> pd.DataFrame:
    if not path_check(path):
        return None
    data = pd.read_csv(path)
    data_table = pd.DataFrame(data)
    print("Loading dataset of dimensions", data_table.shape)
    return (data_table)


