# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


def sorted_merge(a, b):
    if a is None:
        return b
    elif b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)

    return result


def front_back_split(source):
    if source is None or source.next is None:
        return source, None

    (slow, fast) = (source, source.next)

    while fast:

        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    ret = (source, slow.next)
    slow.next = None

    return ret


def merge_sort(head):
    if head is None or head.next is None:
        return head

    front, back = front_back_split(head)

    front = merge_sort(front)
    back = merge_sort(back)

    return sorted_merge(front, back)


if __name__ == "__main__":
    some_array = [1, 17, 4, 15, 20, 2]

    head = None
    for i in some_array:
        head = Node(i, head)

    head = merge_sort(head)

    printList(head)

