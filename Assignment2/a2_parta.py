class HashTable:
    def __init__(self, capacity=32):
        self.cap = capacity
        self.table = [None] * capacity
        self.tombstone = object()  # A unique object to represent tombstones
        self.size = 0

    def insert(self, key, value):
        index = hash(key) % self.cap
        original_index = index

        while self.table[index] is not None and self.table[index] is not self.tombstone:
            if self.table[index][0] == key:
                return False  # Key already exists, don't insert

            index = (index + 1) % self.cap
            if index == original_index:
                # If we've iterated through the entire table, return False (table full)
                return False

        self.table[index] = (key, value)
        self.size += 1
        if self._load_factor() > 0.7:
            self._resize()
        return True

    def modify(self, key, value):
        index = self._find_index(key)
        if index is not None:
            self.table[index] = (key, value)
            return True
        return False

    def remove(self, key):
        index = self._find_index(key)
        if index is not None:
            self.table[index] = self.tombstone
            self.size -= 1
            return True
        return False

    def search(self, key):
        index = self._find_index(key)
        if index is not None:
            return self.table[index][1]
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size

    def _find_index(self, key):
        index = hash(key) % self.cap
        original_index = index

        while self.table[index] is not None:
            if self.table[index] is not self.tombstone and self.table[index][0] == key:
                return index
            index = (index + 1) % self.cap
            if index == original_index:
                break

        return None

    def _load_factor(self):
        return self.size / self.cap

    def _resize(self):
        new_capacity = self.cap * 2
        new_table = [None] * new_capacity

        for entry in self.table:
            if entry is not None and entry is not self.tombstone:
                key, value = entry
                new_index = hash(key) % new_capacity

                while new_table[new_index] is not None:
                    new_index = (new_index + 1) % new_capacity

                new_table[new_index] = (key, value)

        self.table = new_table
        self.cap = new_capacity
