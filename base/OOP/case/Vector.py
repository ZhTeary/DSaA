class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vecor of zeros."""
        if isinstance(d,list):
            self._coords = d
        else:
            self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vectors."""
        return len(self._coords)

    def __getitem__(self, item):
        """Return itemth coordinate of vector."""
        return self._coords[item]

    def __setitem__(self, key, value):
        """Set keyth coordinate of vector to given value."""
        self._coords[key] = value

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):  # relies on __len__method
            raise ValueError('dimensions must agree')
        result = Vector(len(other))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):  # relies on __len__method
            raise ValueError('dimensions must agree')
        result = Vector(len(other))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __call__(self, *args, **kwargs):
        """Produce 括号 representation of vecotr. such as v()"""
        return str(self)

    def __sub__(self, other):
        """return the difference between two vectors"""
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for i in range(result):
            result[i] = self[i] - other[i]
        return result

    def __neg__(self):
        """Return negative self"""
        for i in range(len(self)):
            self[i] = 0 - self[i]

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for i in range(len(result)):
            result[i] = self[i] * other[i]
        return result

    # def __rmul__(self, n):
    #     for i in range(len(self)):
    #         self[i] = n * self[i]
    #     return self

    def __rmul__(self, n):
        for i in range(len(self)):
            self[i] = n * self[i]
        return self


v = Vector([2,0,0,0,0])
u = Vector(5)
u[0] = 3

print(v * u)
print(v)
