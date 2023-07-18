"""双向链表实现双向队列"""


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """LightWeight,nonpublic class for storing a doublt linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create am empty list."""
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._tailer._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._pre = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non-c node from the list and return its element. """
        predecessor = node._prev
        successor = node._next
        predecessor._next = node._next
        successor._pre = node._prev
        self._size -= 1

        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return deleted element


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implement based on a doubly linked list."""
    super().__init__()

    def first(self):
        """Return(but not remove)the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._header._next._element  # real item just after header

    def last(self):
        """Return (but not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._tailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  # use inherited method

    def insert_last(self, e):
        """Add an element to the last of the deque."""
        self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._delete_node(self._tailer._prev)  # use inherited method
