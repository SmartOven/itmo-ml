import numpy as np
from scipy.optimize import minimize


def f(x, *args):
    return (x[0] + args[0]) ** 2 - args[1]


def g(x, *args):
    return abs(f(x, *args))


def find_min(fun, a, b):
    return minimize(fun, args=(a, b), x0=np.array([0]))


A, B = map(int, input().split(" "))
min_f = find_min(f, A, B)
min_g = find_min(g, A, B)
print(f"{min_f.x[0]:.2f} {min_g.x[0]:.2f}")
