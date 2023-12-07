import unittest
from minheap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        min_heap = MinHeap()
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(7)
        min_heap.insert(2)
        self.assertEqual(len(min_heap), 4)

    def test_get_min(self):
        min_heap = MinHeap([5, 3, 7, 2])
        self.assertEqual(min_heap.get_min(), 2)

    def test_extract_min(self):
        min_heap = MinHeap([5, 3, 7, 2])
        min_val = min_heap.extract_min()
        self.assertEqual(min_val, 2)
        self.assertEqual(len(min_heap), 3)
        self.assertEqual(min_heap.get_min(), 3)

    def test_is_empty(self):
        min_heap = MinHeap()
        self.assertTrue(min_heap.is_empty())
        min_heap.insert(10)
        self.assertFalse(min_heap.is_empty())

    def test_len(self):
        min_heap = MinHeap([5, 3, 7, 2])
        self.assertEqual(len(min_heap), 4)
        min_heap.insert(8)
        self.assertEqual(len(min_heap), 5)

    def test_heap_property(self):
        min_heap = MinHeap([5, 3, 7, 2])
        min_heap.insert(1)
        min_heap.insert(6)
        min_heap.insert(4)
        min_heap.insert(0)
        self.assertEqual(min_heap.extract_min(), 0)
        self.assertEqual(min_heap.extract_min(), 1)
        self.assertEqual(min_heap.extract_min(), 2)
        self.assertEqual(min_heap.extract_min(), 3)
        self.assertEqual(min_heap.extract_min(), 4)
        self.assertEqual(min_heap.extract_min(), 5)
        self.assertEqual(min_heap.extract_min(), 6)
        self.assertEqual(min_heap.extract_min(), 7)
        self.assertTrue(min_heap.is_empty())


if __name__ == "__main__":
    unittest.main()
