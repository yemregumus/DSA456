# Copy over your a1_partc.py file here
#    Main Author(s): Dev Jigishkumar Shah
#    Main Reviewer(s): Yunus Gumus, Lorenzo Ramos


class Stack:
    def __init__(self, cap=10):
        self.capp = cap
        self.items = [None] * self.capp
        self.occupied = 0

    def capacity(self):
        return self.capp

    def push(self, data):
        if self.occupied == self.capp:
            new_list_capacity = self.capp * 2
            new_list = [None] * new_list_capacity

            for i in range(self.capp):
                new_list[i] = self.items[i]

            self.items = new_list
            self.capp = new_list_capacity

        self.items[self.occupied] = data
        self.occupied += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() used on empty stack")
        else:
            redundent_item = self.items[self.occupied - 1]
            self.items[self.occupied - 1] = None
            self.occupied -= 1
            return redundent_item

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.items[self.occupied - 1]

    def is_empty(self):
        return self.occupied == 0

    def __len__(self):
        return self.occupied


class Queue:
    def __init__(self, cap=10):
        self.capp = cap
        self.items = [None] * self.capp
        self.occupied = 0
        self.front = 0
        self.rear = self.occupied - 1

    def capacity(self):
        return self.capp

    def enqueue(self, data):
        if self.occupied == self.capp:
            new_list_capacity = self.capp * 2
            new_list = [None] * new_list_capacity

            for i in range(self.capp):
                new_list[i] = self.items[(self.front + i) % self.capp]

            self.items = new_list
            self.front = 0
            self.rear = self.occupied - 1
            self.capp = new_list_capacity

        self.rear = (self.rear + 1) % self.capp
        self.items[self.rear] = data
        self.occupied += 1

    def dequeue(self):
        if not self.is_empty():
            redundent_item = self.items[self.front]

            self.items[self.front] = None

            self.front = (self.front + 1) % self.capp

            self.occupied -= 1

            return redundent_item

        else:
            raise IndexError("dequeue() used on empty queue")

    def get_front(self):
        if not self.is_empty():
            return self.items[self.front]
        else:
            return None

    def is_empty(self):
        return self.occupied == 0

    def __len__(self):
        return self.occupied


class Deque:
    def __init__(self, cap=10):
        self.capp = cap
        self.items = [None] * self.capp
        self.occupied = 0
        self.front = 0
        self.rear = self.capp - 1

    def capacity(self):
        return self.capp

    def resize(self):
        if self.occupied == self.capp:
            new_list_capacity = self.capp * 2
            new_list = [None] * new_list_capacity

            for i in range(self.capp):
                new_list[i] = self.items[(self.front + i) % self.capp]

            self.items = new_list
            self.front = 0
            self.rear = self.occupied - 1
            self.capp = new_list_capacity

    def add_new_item(self, data, index):
        self.items[index] = data
        self.occupied = self.occupied + 1

    def push_front(self, data):
        self.resize()

        if not self.is_empty():
            self.front = (self.front - 1) % self.capp
        else:
            self.rear = self.front

        self.add_new_item(data, self.front)

    def push_back(self, data):
        self.resize()

        if not self.is_empty():
            self.rear = (self.rear + 1) % self.capp
        else:
            self.front = self.rear

        self.add_new_item(data, self.rear)

    def remove_item(self, index):
        if not self.is_empty():
            redundent_item = self.items[index]
            self.items[index] = None
            self.occupied -= 1

            return redundent_item

        else:
            return False

    def pop_front(self):
        redundent_item = self.remove_item(self.front)

        if redundent_item:
            self.front = (self.front + 1) % self.capp
            return redundent_item

        else:
            raise IndexError("pop_front() used on empty deque")

    def pop_back(self):
        redundent_item = self.remove_item(self.rear)

        if redundent_item:
            self.rear = (self.rear - 1) % self.capp
            return redundent_item

        else:
            raise IndexError("pop_back() used on empty deque")

    def get_front(self):
        if not self.is_empty():
            return self.items[self.front]
        else:
            return None

    def get_back(self):
        if not self.is_empty():
            return self.items[self.rear]
        else:
            return None

    def is_empty(self):
        return self.occupied == 0

    def __len__(self):
        return self.occupied

    def __getitem__(self, k):
        if 0 <= k < self.occupied:
            return self.items[(self.front + k) % self.capp]
        else:
            raise IndexError("Index out of range")
