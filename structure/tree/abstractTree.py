class Tree:
    """Abstract base class representing a tree structure."""

    # ----------------------------nested Position class ----------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position"""
            return NotImplementedError('must be implemented by subclass.')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass.')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

    # ---------------abstract methods that concrete subclass must support---------
    def root(self):
        """Return Position representing the tree`s root (or None if empty.)"""
        raise NotImplementedError('must be implemented by subclass.')

    def parent(self, p):
        """Return Position representing p`s parent(or None if empty.)"""
        raise NotImplementedError('must be implemented by subclass.')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass.')

    def children(self, p):
        """Generate an iteration of Positions representing p`s children."""
        raise NotImplementedError('must be implemented by subclass.')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass.')

    # -------------concrete methods implemented in this class.------------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have ant children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root.(祖先的个数)
        运行时间为O(dp+1),dp为树T中p节点的深度；最坏的时间复杂度为O(n)，但通常dp<<n
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self,p):
        """Return the height of the tree. O(n)

        树T中节点p的高度的定义如下：
        - 如果p是一个叶子节点，那么它的高度为0
        - 否则，p的高度是他孩子节点中的最大高度+1
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            return 0
        return self._height(p)
