from listSingle import LinkedList


class ListNode:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class DequeLinkedList:
    """
    A doubly linked list implementation of a deque.

    Args:
        None

    Returns:
        None

    Methods:
        - get(index: int) -> int: Returns the value at the given index in the deque.
        - insertFront(val: int) -> None: Inserts a value at the front of the deque.
        - insertRear(val: int) -> None: Inserts a value at the rear of the deque.
        - removeFront() -> bool: Removes the value at the front of the deque.
        - removeRear() -> bool: Removes the value at the rear of the deque.
        - getValues() -> LinkedList: Returns a list of all values in the deque.
    """

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0

        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def insertFront(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        if self.head.next:
            self.head.next.prev = new_node
        else:
            self.tail = new_node
        self.head.next = new_node
        new_node.prev = self.head

    def insertRear(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def removeFront(self) -> bool:
        if self.head.next:
            if self.head.next == self.tail:
                self.tail = self.head
            self.head.next = self.head.next.next
            if self.head.next:
                self.head.next.prev = self.head
            return True
        return False

    def removeRear(self) -> bool:
        if self.tail.prev:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return True
        return False

    def getValues(self) -> LinkedList:
        current = self.head.next
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res
