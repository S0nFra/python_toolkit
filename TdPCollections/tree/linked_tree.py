from tree import Tree

class LinkedTree(Tree):
    """Linked representation of a tree structure."""

    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = children if children is not None else []

    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._children)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists; tree is not empty')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_child(self, p, e):
        """Create a new child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid.
        """
        node = self._validate(p)
        if self._root is None:
            raise ValueError('Tree is empty; use add_root() first')
        self._size += 1
        child = self._Node(e, node)
        node._children.append(child)
        return self._make_position(child)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """Delete the node at Position p, and replace it with its children.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid.
        """
        node = self._validate(p)
        element = node._element
        
        if node is self._root:
            if len(node._children) > 1:
                raise ValueError('Cannot delete root with multiple children')
            elif len(node._children) == 1:
                self._root = node._children[0]
                self._root._parent = None
            else:
                self._root = None
        else:
            parent = node._parent
            parent._children.remove(node)
            for child in node._children:
                child._parent = parent
                parent._children.append(child)
        
        self._size -= 1
        
        del node._element
        del node._children
        node._parent = node  # convention for deprecated nodes
        
        return element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._children.append(t1._root)
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._children.append(t2._root)
            t2._root = None
            t2._size = 0

    def __del__(self):
        """Destructor to clean up the entire tree."""
        if self._root is not None:
            self._delete_subtree(self._root)

    def _delete_subtree(self, node):
        """Recursively delete the subtree rooted at node."""
        for child in node._children:
            self._delete_subtree(child)
        del node._element
        del node._children
        del node._parent
