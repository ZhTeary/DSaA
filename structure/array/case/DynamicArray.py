import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Create a empty array"""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low_level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, item):
        """Return element at index item"""
        if not 0 <= item <= self._n:
            raise IndexError('invalid index')
        return self._A[item]

    def append(self, obj):
        """Add object to the end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utiity
        """Return internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward.

        运行时间为Ω(n),在结束位置插入为O(1),总摊销时间为O(n-k+1)
        最好还是append, 运行时间为O(1)
        """
        # (for simplicity, we assume 0<=k<=n in this version)
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurence of value(or raise ValueError)
        remove每一次都需要Ω(n)
        pop()删除最后一个元素，效率为O(1),但pop(0)运行时间为Ω(n)
        """
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')
