class MinHeap:
    def __init__(self, arr=[]):
        # Initialize the heap with elements from the input list using insert method
        self.heap = []
        for element in arr:
            self.insert(element)

    def insert(self, element):
        # Add a new element to the heap
        self.heap.append(element)
        # Ensure the heap property is maintained by calling heap_up
        self.heap_up(len(self.heap) - 1)

    def get_min(self):
        # Return the smallest element in the heap (root of the heap)
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        # Remove and return the smallest element in the heap
        if not self.heap:
            return None

        min_val = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            # Replace the root with the last element and heap_down
            self.heap[0] = last_element
            self.heap_down(0)

        return min_val

    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0

    def __len__(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def heap_up(self, i):
        # Move the element up the heap until the heap property is restored
        if i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self.heap_up(parent)

    def heap_down(self, i):
        # Move the element down the heap until the heap property is restored
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[smallest]
        ):
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heap_down(smallest)
