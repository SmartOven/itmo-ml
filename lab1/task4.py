import matplotlib.pyplot as plt
import numpy as np
from task3 import f, g, min_f, min_g, A, B


def plot_fun(fun, fun_name, color, min_x, min_y):
    x_values = np.linspace(-10, 10, 400)
    y_values = [fun([x], *(A, B)) for x in x_values]
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=fun_name, color=color)
    plt.scatter(min_x, min_y, color='red', label=f'Minimum (x={min_x:.2f}, y={min_y:.2f})')
    plt.title('График функции с отмеченным минимум')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()


plot_fun(f, "f(x)", "blue", min_f.x[0], min_f.fun)
plot_fun(g, "g(x)", "green", min_g.x[0], min_g.fun)
