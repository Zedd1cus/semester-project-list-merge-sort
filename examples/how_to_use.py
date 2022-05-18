from src.linked_list_merge_sort import merge_sort, Node


def print_linked_list(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


if __name__ == "__main__":
    some_array = [1, 17, 4, 15, 20, 20, 2]

    head = None
    for i in some_array:
        head = Node(i, head)

    head = merge_sort(head)

    print_linked_list(head)


