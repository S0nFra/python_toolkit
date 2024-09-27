import unittest
from TdPCollections.tree.tree import Tree

class TestTree(unittest.TestCase):
    class ConcreteTree(Tree):
        """A concrete implementation of the abstract Tree class for testing."""
        def __init__(self):
            self._root = None
            self._children = {}
            self._parent = {}

        def root(self):
            return self._root

        def parent(self, p):
            return self._parent.get(p)

        def num_children(self, p):
            return len(self._children.get(p, []))

        def children(self, p):
            return iter(self._children.get(p, []))

        def __len__(self):
            return len(self._parent)

        def add_root(self, e):
            if self._root is not None:
                raise ValueError('Root exists')
            self._root = e
            self._children[e] = []
            return e

        def add_child(self, p, e):
            self._children.setdefault(p, []).append(e)
            self._parent[e] = p
            return e

    def setUp(self):
        self.tree = self.ConcreteTree()

    def test_root(self):
        root = self.tree.add_root(1)
        self.assertEqual(self.tree.root(), root)

    def test_parent(self):
        root = self.tree.add_root(1)
        child = self.tree.add_child(root, 2)
        self.assertEqual(self.tree.parent(child), root)

    def test_num_children(self):
        root = self.tree.add_root(1)
        self.tree.add_child(root, 2)
        self.tree.add_child(root, 3)
        self.assertEqual(self.tree.num_children(root), 2)

    def test_is_root(self):
        root = self.tree.add_root(1)
        self.assertTrue(self.tree.is_root(root))

    def test_is_leaf(self):
        root = self.tree.add_root(1)
        leaf = self.tree.add_child(root, 2)
        self.assertTrue(self.tree.is_leaf(leaf))
        self.assertFalse(self.tree.is_leaf(root))

    def test_depth(self):
        root = self.tree.add_root(1)
        child = self.tree.add_child(root, 2)
        grandchild = self.tree.add_child(child, 3)
        self.assertEqual(self.tree.depth(grandchild), 2)

    def test_height(self):
        root = self.tree.add_root(1)
        child1 = self.tree.add_child(root, 2)
        child2 = self.tree.add_child(root, 3)
        self.tree.add_child(child1, 4)
        self.tree.add_child(child2, 5)
        self.assertEqual(self.tree.height(), 2)

if __name__ == '__main__':
    unittest.main()
