from src.linked_list_merge_sort import LinkedList
from src.dynamic_array_merge_sort import dynamic_array_merge_sort
from typing import List
import time


def fill_dynamic_array(new_array: List[int], array_from_data: List[int]) -> List[int]:
    new_array = array_from_data
    return new_array


def fill_linked_list(linklist: LinkedList, array_from_data: List[int]) -> LinkedList:
    for elem in array_from_data:
        linklist.append(elem)
    return linklist


def bench_dynamic_array(path: str) -> float:
    dyn_array = []
    with open(path) as data:
        arr = [int(line) for line in data.readlines()]
        fill_dynamic_array(dyn_array, arr)
    time_lst = time.time()
    dyn_array = dynamic_array_merge_sort(dyn_array)
    return (time.time() - time_lst) * 1000


def bench_linked_list(path: str) -> float:
    linklist = LinkedList()
    with open(path) as data:
        arr = [int(line) for line in data.readlines()]
        fill_linked_list(linklist, arr)
    time_lst = time.time()
    linklist.merge_sort(linklist.head)
    return (time.time() - time_lst) * 1000


