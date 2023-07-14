"""循环链表实现循环队列"""
from queue import Empty


class CircularQueue:

    # ---------------------------------------------------------------------
    class _Node:
        """Lightweight,nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ---------------------------------------------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._tail = None   # will represent tail of queue
        self._size = 0      # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return(but do not remove) the element at the front of the queue.

        Raise Empty if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._next._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO)

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._tail._next._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail._next = newest
        self._size += 1

    def rotate(self):
        """Return front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next
