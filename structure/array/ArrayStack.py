class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []  # nonpublic list instance

    def __str__(self):
        return ' '.join([str(i) for i in self._data])

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but not remove) the top of the stack."""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Return and remove the top of the stack."""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()  # remove last item from list.
