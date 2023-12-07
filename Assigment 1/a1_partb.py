#    Main Author(s): Yunus Emre Gumus
#    Main Reviewer(s): Lorenzo Ramos, Dev Jigishkumar Shah

# REFLECTION
# =========================================================
# Please detail what exactly you did for the assignment.

# In this assignment, I was responsible for completing part B,
# which involved implementing the DoublyLinked class and its associated functions.
# I also helped drawing diagrams for part A, and created the repository.

# What was one thing you learned when doing this assignment?

# One thing I learned while working on this assignment is the importance
# of carefully considering the data structure and algorithms used for
# implementing a doubly linked list. This experience reinforced the concept
# of pointer manipulation and how efficient algorithms can be designed to
# perform common operations on such data structures.

# What was its most challenging aspect and what did you do to overcome this challenge?

# The most challenging aspect of this assignment was ensuring that the various methods
# of the DoublyLinked class worked correctly and efficiently, especially when dealing
# with edge cases. I referred to relevant documentation and resources
# to ensure that my implementation aligned with best practices for doubly linked lists.
# This approach helped me overcome the challenges and produce a robust implementation
# for the assignment.


class DoublyLinked:
    class Node:
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):  # Initialize the list
        self.head = None
        self.tail = None
        self.count = 0  # Initialize the count to 0

    def get_front(self):  # Returns the first(head) node if its not empty
        if self.is_empty():
            return None
        return self.head

    def get_back(self):  # Returns the last(tail) node if its not empty
        if self.is_empty():
            return None
        return self.tail

    def push_front(
        self, data
    ):  # Pushing a new node with data in it to the front of the list by pointing head and tail to new node if its empty
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:  # If its not empty
            new_node.next = self.head  # Set new node's next to the current head
            self.head.prev = new_node  # Set current head's previous to the new node
            self.head = new_node  # Update head to the new node
        self.count += 1  # Increment the count

    def push_back(
        self, data
    ):  # Pushing a new node with data in it to the back of the list by pointing head and tail to new node if its empty
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:  # If its not empty
            new_node.prev = self.tail  # Set new node's previous to the current tail
            self.tail.next = new_node  # Set current tail's next to the new node
            self.tail = new_node  # Update tail to the new node
        self.count += 1  # Increment the count

    def pop_front(
        self,
    ):  # Remove a node and return its data from the front if the list is not empty
        if self.is_empty():
            raise IndexError("pop_front() used on empty list")
        data = self.head.get_data()  # storing data from the head in a variable
        self.head = self.head.get_next()  # set the head to the next nodes next element
        if self.head is not None:
            self.head.prev = (
                None  # update the new heads previous to None if head is not None
            )
        else:
            self.tail = None  # If the list becomes empty then uptade tail to None
        self.count -= 1  # Decrement the count
        return data

    def pop_back(
        self,
    ):  # Remove a node and return its data from the back if the list is not empty
        if self.is_empty():
            raise IndexError("pop_back() used on empty list")
        data = self.tail.get_data()  # storing data from the tail in a variable
        self.tail = (
            self.tail.get_previous()
        )  # set the tail to the next nodes previous element
        if self.tail is not None:
            self.tail.next = (
                None  # update the new tails next to None if tail is not None
            )
        else:
            self.head = None  # If list becomes empty update head to None
        self.count -= 1  # Decrement the count
        return data

    def is_empty(self):  # Check if head is None to determine if the list is empty
        return self.head is None

    def insert_after(self, data, node):
        new_node = self.Node(data)
        if node is None:
            self.push_front(data)  # If node is None, insert at the front
        else:
            self.count += 1  # Increment the count
            new_node.next = (
                node.get_next()
            )  # Seting new nodes next to the next of the provided node
            new_node.prev = node  # Seting new node's previous to the provided node
            if (
                node.get_next() is not None
            ):  # Update the next nodes previous to the new node
                node.get_next().prev = (
                    new_node  # Update provided node's next to the new node
                )
            node.next = new_node
            if node == self.tail:
                self.tail = new_node  # If the provided node is the tail, update tail to the new node

    def search(self, data):
        current = self.head  # Start from head
        while current is not None:  # Loop until head is not empty
            if (
                current.get_data() == data
            ):  # look into each nodes data check if its the same with the provided
                return current  # return node when same data found in one
            current = current.get_next()
        return None  # return none if data is not found in any nodes

    def __len__(self):
        return self.count  # returns current count of nodes

    def is_palindrome(self):
        if self.is_empty():
            return True  # An empty list is considered a palindrome

        front = self.head  # initialize two pointers to traverse the list from both ends
        back = self.tail

        while front != back and front.get_next() != back:  # traverse the list
            if front.get_data() != back.get_data():
                return False  # returns false if data doesn`t match
            front = (
                front.get_next()
            )  # moves both head and tail towards middle by going to next node from head and previous node from tail.
            back = back.get_previous()

        if front != back:
            return (
                front.get_data() == back.get_data()
            )  # Checking the data in the middle for odd-length lists

        return True  # Return True if the list is a palindrome
