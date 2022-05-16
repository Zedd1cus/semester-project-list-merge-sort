import os
from random import randint


def make_dirs() -> None:
    if not (os.path.isdir('data_of_dynamic_array') and os.path.isdir('data_of_linked_list')):
        os.mkdir('data_of_dynamic_array')
        os.mkdir('data_of_linked_list')

        for i in range(1, 6):
            os.makedirs('data_of_dynamic_array/0' + str(i))
            os.makedirs('data_of_linked_list/0' + str(i))


def make_data(i: str, j: str, some_arr: list) -> None:
    for k in some_arr:
        with open(i + '/' + j + '/' + str(k) + '.txt', 'w') as f:
            for m in range(k-1):
                some_number = randint(1, 1_000_000)
                f.write(str(some_number) + '\n')

            else:
                some_number = randint(1, 1_000_000)
                f.write(str(some_number))


def make_txt_files(some_arr: list) -> None:
    for i in os.listdir():
        if i[-3:] == '.py':
            continue

        for j in os.listdir(i):
            make_data(i, j, some_arr)


arr_for_elements = [100, 500, 900, 1300, 1700, 2100, 2500, 2900]
make_dirs()
make_txt_files(arr_for_elements)