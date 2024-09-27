import unittest

# Import test modules
from TdPCollections.tree.tests.test_tree import TestTree
from TdPCollections.tree.tests.test_binary_tree import TestBinaryTree
from TdPCollections.tree.tests.test_linked_binary_tree import TestLinkedBinaryTree

if __name__ == '__main__':
    # Create a test suite combining all test cases
    test_suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestTree),
        unittest.TestLoader().loadTestsFromTestCase(TestBinaryTree),
        unittest.TestLoader().loadTestsFromTestCase(TestLinkedBinaryTree)
    ])

    # Run the combined test suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)
