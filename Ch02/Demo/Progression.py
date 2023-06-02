# 数列
class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current  # record current value to return
            self._advance()  # advance to prepare for next time
            return answer  # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def show_progression(self, n):
        """Print next n values of the progression."""
        return ' '.join(str(next(self)) for j in range(n))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression 等差数列"""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression

        increment   the fixed constant to add to each term (defalut 1)
        start       the first item of the progression
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment

    def pp(self):
        s = 0
        print(s)
        s = next(self)
        # print(type(next(self)))
        return s

    def times(self, target):
        flags = 1
        s = 0
        while target != s:
            s = next(self)
            if s > target:
                return False
            if target == s:
                return flags
            flags += 1
        return 0


class GeometricProgression(Progression):
    """Iterator producing an geometric progression 等比数列"""

    def __init__(self, base=2, start=1):
        """Create a new arithmetic progression

        base        the fixed constant to add to each term (default 2)
        start       the first item of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying the base value."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing an fibonacci progression 斐波那契数列"""

    def __init__(self, first=0, second=1):
        """Create a new arithmetic progression

        first        the first term of the progression (defalut 0)
        second       the second item of the progression (default 1)
        """
        super().__init__(first)  # start progression at first
        self._prev = second - first  # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking the sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current


def funcyield():
    yield 300
    yield 100
    yield 200


if __name__ == '__main__':
    v = ArithmeticProgression(128, 0)
    print(v.show_progression(4))
    # 要从头算次数 之前就不能调用了 不然都不是从头开始了
    print(v.times(128))
    f = funcyield()
    for i in f:
        print(i)
