def squaresum(n):
    square = sum([k*k for k in range(1,n+1)])
    return square

print(squaresum(3))