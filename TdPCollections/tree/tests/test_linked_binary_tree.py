import unittest
from TdPCollections.tree.linked_binary_tree import LinkedBinaryTree

class TestLinkedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = LinkedBinaryTree()

    def test_add_root(self):
        root = self.tree.add_root(1)
        self.assertEqual(root.element(), 1)
        self.assertEqual(len(self.tree), 1)

    def test_add_left_right(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.assertEqual(self.tree.left(root).element(), 2)
        self.assertEqual(self.tree.right(root).element(), 3)
        self.assertEqual(len(self.tree), 3)

    def test_replace(self):
        root = self.tree.add_root(1)
        old_value = self.tree.replace(root, 4)
        self.assertEqual(old_value, 1)
        self.assertEqual(root.element(), 4)

    def test_delete(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        deleted = self.tree.delete(left)
        self.assertEqual(deleted, 2)
        self.assertEqual(len(self.tree), 1)
        self.assertIsNone(self.tree.left(root))

    def test_attach(self):
        tree1 = LinkedBinaryTree()
        tree2 = LinkedBinaryTree()
        root1 = tree1.add_root(1)
        root2 = tree2.add_root(2)
        
        main_tree = LinkedBinaryTree()
        main_root = main_tree.add_root(0)
        
        main_tree.attach(main_root, tree1, tree2)
        self.assertEqual(len(main_tree), 3)
        self.assertEqual(main_tree.left(main_root).element(), 1)
        self.assertEqual(main_tree.right(main_root).element(), 2)

    def test_is_root_and_is_leaf(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        self.assertTrue(self.tree.is_root(root))
        self.assertFalse(self.tree.is_root(left))
        self.assertTrue(self.tree.is_leaf(left))
        self.assertFalse(self.tree.is_leaf(root))

    def test_depth_and_height(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.tree.add_left(left, 4)
        self.tree.add_right(left, 5)
        
        self.assertEqual(self.tree.depth(root), 0)
        self.assertEqual(self.tree.depth(left), 1)
        self.assertEqual(self.tree.height(), 2)

    def test_inorder_traversal(self):
        root = self.tree.add_root(1)
        left = self.tree.add_left(root, 2)
        right = self.tree.add_right(root, 3)
        self.tree.add_left(left, 4)
        self.tree.add_right(left, 5)
        
        inorder = list(self.tree.inorder())
        self.assertEqual([p.element() for p in inorder], [4, 2, 5, 1, 3])

if __name__ == '__main__':
    unittest.main()
