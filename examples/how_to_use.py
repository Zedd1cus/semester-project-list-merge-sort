from src.linked_list_merge_sort import LinkedList


def print_linked_list(head):
    string = ''
    if head is None:
        return
    curr_node = head
    while curr_node:
        string += f'{curr_node.data}->'
        curr_node = curr_node.next
    print(string[:-2])


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(8)
    ll.append(17)
    ll.append(33)
    ll.append(15)
    ll.append(2)

    ll.head = ll.merge_sort(ll.head)
    print("Sorted Linked List is:")
    print_linked_list(ll.head)
