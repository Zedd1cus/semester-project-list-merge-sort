from src.linked_list_msort import merge_sort, Node


def print_linked_list(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


if __name__ == "__main__":
    some_array = [1, 17, 4, 15, 20, 20, 2]

    head = None
    link_len = len(some_array)
    for i in some_array:
        head = Node(i, head)

    head = merge_sort(head, link_len)

    print_linked_list(head)


