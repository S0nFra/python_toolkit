import unittest
from TdPCollections.tree.binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    class ConcreteBinaryTree(BinaryTree):
        """A concrete implementation of the abstract BinaryTree class for testing."""
        def __init__(self):
            self._root = None
            self._left = {}
            self._right = {}
            self._parent = {}

        def root(self):
            return self._root

        def parent(self, p):
            return self._parent.get(p)

        def left(self, p):
            return self._left.get(p)

        def right(self, p):
            return self._right.get(p)

        def num_children(self, p):
            count = 0
            if p in self._left: count += 1
            if p in self._right: count += 1
            return count

        def __len__(self):
            return len(self._parent)

        def add_root(self, e):
            if self._root is not None:
                raise ValueError('Root exists')
            self._root = e
            return e

        def add_left(self, p, e):
            if p in self._left:
                raise ValueError('Left child exists')
            self._left[p] = e
            self._parent[e] = p
            return e

        def add_right(self, p, e):
            if p in self._right:
                raise ValueError('Right child exists')
            self._right[p] = e
            self._parent[e] = p
            return e

    def setUp(self):
        self.tree = self.ConcreteBinaryTree()

    def test_root(self):
        root = self.tree.add_root(1)
        self.assertEqual(self.tree.root(), root)

    def test_left_right(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.assertEqual(self.tree.left(root), left)
        self.assertEqual(self.tree.right(root), right)

    def test_sibling(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.assertEqual(self.tree.sibling(left), right)
        self.assertEqual(self.tree.sibling(right), left)

    def test_children(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        children = list(self.tree.children(root))
        self.assertEqual(len(children), 2)
        self.assertIn(left, children)
        self.assertIn(right, children)

    def test_inorder(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.tree.add_left(left, 4)
        self.tree.add_right(left, 5)
        inorder = list()
        for e in self.tree.inorder():
            inorder.append(e)
        self.assertEqual(inorder, [4, 2, 5, 1, 3])

if __name__ == '__main__':
    unittest.main()
