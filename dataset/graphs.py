import matplotlib.pyplot as plt
import numpy as np
from generate_txt_dataset import arr_for_elements


def array_plot() -> None:
    fig, ax = plt.subplots()

    x = arr_for_elements
    y = [0.31235218, 26.93439484, 56.89840794, 87.54626274, 120.563755, 163.9518452]

    x1 = arr_for_elements
    y1 = [0.312495232, 21.712327, 46.7825985, 75.17297745, 101.3124561, 141.7034006]

    one_oper = y1[3] / (15100*14)
    x2 = arr_for_elements
    list_cnt_operations = [700, 5100*13, 10100*14, 15100*14, 20100*15, 25100*15]
    y2 = [one_oper*i for i in list_cnt_operations]
    ax.plot(x1, y1, label='link list', color='r')
    ax.plot(x, y, label='dynamic array', color='b')
    ax.plot(x2, y2, label='Предполагалось', color='k')

    ax.plot()

    ax.legend(loc='upper left')

    ax.set_title('Merge Sort')
    ax.set_ylabel('Время работы(мс)')
    ax.set_xlabel('Кол-во элементов')

    plt.show()

if __name__ == '__main__':
    array_plot()