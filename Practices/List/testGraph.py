import unittest
from graphAndLabeled import Graph
from graphAndLabeled import LabelGraph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(3)

    def test_add_vertex(self):
        self.graph.add_vertex()
        self.assertEqual(self.graph.num_verts(), 4)

    def test_add_edge(self):
        self.assertTrue(self.graph.add_edge(0, 1))
        self.assertEqual(self.graph.num_edges(), 1)
        self.assertFalse(self.graph.add_edge(0, 1))  # Edge already exists
        self.assertFalse(self.graph.add_edge(5, 1))  # Invalid vertices

    def test_num_edges(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.assertEqual(self.graph.num_edges(), 2)

    def test_has_edge(self):
        self.graph.add_edge(0, 1)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertFalse(self.graph.has_edge(1, 0))

    def test_edge_weight(self):
        self.graph.add_edge(0, 1, 5)
        self.assertEqual(self.graph.edge_weight(0, 1), 5)
        self.assertIsNone(self.graph.edge_weight(1, 0))

    def test_get_connected(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        connected = self.graph.get_connected(0)
        self.assertEqual(connected, [(1, 1), (2, 1)])

    def test_validate_indexes(self):
        self.assertTrue(self.graph.validate_indexes(0, 1))
        self.assertFalse(self.graph.validate_indexes(0, 5))


class TestLabelGraph(unittest.TestCase):
    def setUp(self):
        self.label_graph = LabelGraph(["A", "B", "C"])

    def test_add_vertex(self):
        self.label_graph.add_vertex("D")
        self.assertEqual(self.label_graph.num_verts(), 4)

    def test_add_edge(self):
        self.assertTrue(self.label_graph.add_edge("A", "B"))
        self.assertEqual(self.label_graph.num_edges(), 1)
        self.assertFalse(self.label_graph.add_edge("A", "B"))  # Edge already exists
        self.assertFalse(self.label_graph.add_edge("A", "X"))  # Invalid vertices

    def test_num_edges(self):
        self.label_graph.add_edge("A", "B")
        self.label_graph.add_edge("B", "C")
        self.assertEqual(self.label_graph.num_edges(), 2)

    def test_has_edge(self):
        self.label_graph.add_edge("A", "B")
        self.assertTrue(self.label_graph.has_edge("A", "B"))
        self.assertFalse(self.label_graph.has_edge("B", "A"))

    def test_edge_weight(self):
        self.label_graph.add_edge("A", "B", 5)
        self.assertEqual(self.label_graph.edge_weight("A", "B"), 5)
        self.assertIsNone(self.label_graph.edge_weight("B", "A"))

    def test_get_connected(self):
        self.label_graph.add_edge("A", "B")
        self.label_graph.add_edge("A", "C")
        connected = self.label_graph.get_connected("A")
        self.assertEqual(connected, [("B", 1), ("C", 1)])

    def test_get_ids(self):
        ids = self.label_graph.get_ids("A", "B")
        self.assertEqual(ids, (0, 1))
        ids = self.label_graph.get_ids("A", "X")
        self.assertIsNone(ids)


if __name__ == "__main__":
    unittest.main()
