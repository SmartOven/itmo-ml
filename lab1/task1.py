import numpy as np


def linan(s1, s2):
    a1, b1, c1 = map(float, s1.split(" "))
    a2, b2, c2 = map(float, s2.split(" "))
    a = np.array([[a1, b1], [a2, b2]])
    b = np.array([c1, c2])
    solution = np.linalg.solve(a, b)
    return f"{solution[0]} {solution[1]}"


str1 = input()
str2 = input()
print(linan(str1, str2))
