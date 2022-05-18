import matplotlib.pyplot as plt
import numpy as np


def array_plot() -> None:
    fig, ax = plt.subplots()

    x = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
    y = [9.49, 167.11, 385.48, 829.21, 22600.04, 1631.36, 2838.84, 2603.60]

    x1 = [100, 2900]
    y1 = [9.49, 2603.60]

    ax.plot(x1, y1, label='предполагалось')
    ax.plot(x, y, label='получилось')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('Dynamic_Array')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()


def linklist_plt() -> None:
    fig, ax = plt.subplots()

    x = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
    y = [1.60, 7.52, 8.26, 17.53, 12.91, 16.40, 28.90, 24.70]

    one = 9.49 / 1000

    z = x[:]
    z.append(1)
    z.sort()

    ax.plot(x, y, label='получилось')
    ax.plot(z, 0, label='предполагалось')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('Linked_List')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()

if __name__ == '__main__':
    array_plot()
    linklist_plt()