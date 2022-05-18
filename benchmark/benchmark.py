from src.linked_list_merge_sort import Node, merge_sort
from src.dynamic_array_merge_sort import dynamic_array_merge_sort
from typing import List
import time


def fill_dynamic_array(new_array: List[int], array_from_data: List[int]) -> List[int]:
    new_array = array_from_data
    return new_array


def fill_linked_list(some_array: List[int]):
    head = None
    for i in some_array:
        head = Node(i, head)
        return head


def bench_dynamic_array(path: str) -> float:
    dyn_array = []
    with open(path) as data:
        arr = [int(line) for line in data.readlines()]
        fill_dynamic_array(dyn_array, arr)
    time_lst = time.time()
    dyn_array = dynamic_array_merge_sort(dyn_array)
    return (time.time() - time_lst) * 100000000000000


def bench_linked_list(path: str) -> float:
    with open(path) as data:
        arr = [int(line) for line in data.readlines()]
        head = fill_linked_list(arr)
    time_lst = time.time()
    head = merge_sort(head)
    return (time.time() - time_lst) * 100000000000000

def bench_linked_list_arr(array) -> float:
    arr = [line for line in array]
    head = fill_linked_list(arr)
    time_lst = time.time()
    head = merge_sort(head)
    return (time.time() - time_lst) * 100000000000000


if __name__ ==  '__main__':
    print(bench_linked_list('dataset/data_of_linked_list/01/2900.txt'))