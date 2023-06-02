from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, item):
        """Return the element at index item of the sequence"""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for i in range(len(self)):
            if val == self[i]:
                return True
        return False

    def __count__(self, val):
        """Return the number of elements eqal to given value"""
        count = 0
        for i in range(len(self)):
            if self[i] == val:
                count += 1
        return count
