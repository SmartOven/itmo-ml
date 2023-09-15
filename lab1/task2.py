import numpy as np


def decorate_matrix(n):
    try:
        matrix = np.zeros((n, n), dtype=float)
        matrix[0, :] = 1      # первая строка
        matrix[n - 1, :] = 1  # последняя строка
        matrix[:, 0] = 1      # первый столбец
        matrix[:, n - 1] = 1  # последний столбец
        return matrix
    except ValueError as e:
        return None


size = int(input())
print(decorate_matrix(size))
