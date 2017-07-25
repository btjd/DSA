import unittest
from Graph import Graph

class TestGraph(unittest.TestCase):
    def test_vertices(self):
        g = { "a" : ["d"], "b" : ["c"], "c" : ["b", "c", "d", "e"], "d" : ["a", "c"], "e" : ["c"], "f" : []}
        graph = Graph(g)
        self.assertEqual(sorted(graph.get_vertices()), ["a", "b", "c", "d", "e", "f"])
        
        
if __name__ == '__main__':
    unittest.main()