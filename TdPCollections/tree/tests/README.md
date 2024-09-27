# Tree Data Structures Tests

This directory contains unit tests for the Tree, BinaryTree, and LinkedBinaryTree data structures.

## Running the Tests

You can run the tests in two ways:

### 1. Running All Tests

To run all tests at once, use the following command from the project root directory:

```
python -m unittest discover tests
```

Or, you can use the `run_all_tests.py` script:

```
python tests/run_all_tests.py
```

### 2. Running Individual Test Files

To run tests for a specific data structure, use one of the following commands from the project root directory:

- For Tree:
  ```
  python -m unittest tests.test_tree
  ```

- For BinaryTree:
  ```
  python -m unittest tests.test_binary_tree
  ```

- For LinkedBinaryTree:
  ```
  python -m unittest tests.test_linked_binary_tree
  ```

## Requirements

- Python 3.6 or higher
- The tree data structure modules should be in the parent directory of `tests/`

## Test Files

- `test_tree.py`: Tests for the basic Tree structure
- `test_binary_tree.py`: Tests for the BinaryTree structure
- `test_linked_binary_tree.py`: Tests for the LinkedBinaryTree implementation
- `run_all_tests.py`: Script to run all tests at once

If you encounter any issues or have questions about the tests, please contact the project maintainer.
