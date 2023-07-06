class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0},{1})'.format(self._name, self._score)  # e.g. '(Bob,98)'


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity

        All entries are initially None.
        """
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, item):
        """Return entry at index item"""
        return self._board[item]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry: GameEntry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than lasts entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


def insert_sore(A: str):
    """sort list of comparable elements into non-decreasing order."""
    for k in range(1, len(A)):  # from 1 to n-1
        current = A[k]  # current element to be inserted
        j = k
        while j > 0 and A[j - 1] > current:
            A[j] = A[j - 1]
            j -= 1
        A[j] = current  # current is now in the right place
