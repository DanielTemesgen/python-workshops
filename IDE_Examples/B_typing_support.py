# Typing support
def add_ten(x: int) -> int:
    return x + 10


add_ten(10)

add_ten(10.0)

# Works with third party packages

from sklearn.datasets import load_iris
import pandas as pd

iris_data = pd.DataFrame(load_iris()[0])


def take_first_col(data: pd.DataFrame) -> pd.Series:
    func_data = data.copy()
    return func_data.iloc[:, 0]


take_first_col(iris_data)

take_first_col(10)
