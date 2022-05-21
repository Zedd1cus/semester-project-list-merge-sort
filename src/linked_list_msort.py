class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def sorted_merge(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    if a.data <= b.data:
        result = a
        a = a.next
    else:
        result = b
        b = b.next

    rslt = result
    while a is not None and b is not None:
        if a.data <= b.data:
            rslt.next = a
            rslt = rslt.next
            a = a.next
        else:
            rslt.next = b
            rslt = rslt.next
            b = b.next

    if a is None:
        rslt.next = b
    if b is None:
        rslt.next = a

    return result


def front_back_split(source, link_len):
    if source is None or source.next is None:
        return source, None

    index = link_len // 2
    middle = source
    for i in range(index-1):
        middle = middle.next
    lst = middle
    middle = middle.next
    lst.next = None
    ret = (source, middle)
    return ret


def merge_sort(head, link_len):
    if head is None or head.next is None:
        return head

    front, back = front_back_split(head, link_len)
    len1 = link_len//2
    len2 = link_len - len1
    front = merge_sort(front, len1)
    back = merge_sort(back, len2)
    return sorted_merge(front, back)
