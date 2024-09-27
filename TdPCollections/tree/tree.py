# Copyright 2013, Michael H. Goldwasser
# Copyright 2024, Francesco S.
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# Modified in 2024: Refactored for improved abstraction, efficiency, and Python 3 compatibility
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod

class Tree(ABC):
  """Abstract base class representing a tree structure."""

  #------------------------------- nested Position class -------------------------------
  class Position(ABC):
    """An abstraction representing the location of a single element within a tree."""

    __slots__ = ()  # streamline memory usage

    @abstractmethod
    def element(self):
      """Return the element stored at this Position."""
      pass

    @abstractmethod
    def __eq__(self, other):
      """Return True if other Position represents the same location."""
      pass

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)

  # ---------- abstract methods that concrete subclass must support ----------
  @abstractmethod
  def root(self):
    """Return Position representing the tree's root (or None if empty)."""
    pass

  @abstractmethod
  def parent(self, p):
    """Return Position representing p's parent (or None if p is root)."""
    pass

  @abstractmethod
  def num_children(self, p):
    """Return the number of children that Position p has."""
    pass

  @abstractmethod
  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    pass

  @abstractmethod
  def __len__(self):
    """Return the total number of elements in the tree."""
    pass

  # ---------- concrete methods implemented in this class ----------
  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0

  def is_empty(self):
    """Return True if the tree is empty."""
    return len(self) == 0

  def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

  def height(self, p=None):
    """Return the height of the subtree rooted at Position p.

    If p is None, return the height of the entire tree.
    """
    if p is None:
      p = self.root()
    return self._height2(p)

  def _height2(self, p):                  # time is linear in size of subtree
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))

  # ---------- methods for tree visit ----------
  def __iter__(self):
    """Generate an iteration of the tree's elements."""
    for p in self.positions():                        # use same order as positions()
      yield p.element()                               # but yield each element

  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()                            # return entire preorder iteration

  def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):  # start recursion
        yield p

  def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                           # visit p before its subtrees
    for c in self.children(p):                        # for each child c
      for other in self._subtree_preorder(c):         # do preorder of c's subtree
        yield other                                   # yielding each to our caller

  def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_postorder(self.root()):  # start recursion
        yield p

  def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):                        # for each child c
      for other in self._subtree_postorder(c):        # do postorder of c's subtree
        yield other                                   # yielding each to our caller
    yield p                                           # visit p after its subtrees

  def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not self.is_empty():
      # Initialize a queue to store positions to be visited
      fringe = []
      # Start with the root of the tree
      fringe.append(self.root())
      while len(fringe) > 0:
        # Remove and return the first position from the queue
        p = fringe.pop(0)
        # Yield the current position
        yield p
        # Add all children of the current position to the queue
        # This ensures we visit all nodes at the current level
        # before moving to the next level
        fringe.extend(self.children(p))
