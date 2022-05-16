class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # push new value to linked list
    # using append method
    def append(self, new_value):

        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def sorted_merge(self, a, b):
        result = None

        # Base cases
        if a is None:
            return b
        if b is None:
            return a

        # pick either a or b and recursion
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def merge_sort(self, h):

        # Base case if head is None
        if h is None or h.next is None:
            return h

        # get the middle of the list
        middle = self.get_middle(h)
        next_to_middle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.merge_sort(h)

        # Apply mergeSort on right list
        right = self.merge_sort(next_to_middle)

        # Merge the left and right lists
        sortedlist = self.sorted_merge(left, right)
        return sortedlist

    # Utility function to get the middle
    # of the linked list
    @staticmethod
    def get_middle(head):
        if head is None:
            return head

        slow = head
        fast = head

        while (fast.next is not None and
               fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow
