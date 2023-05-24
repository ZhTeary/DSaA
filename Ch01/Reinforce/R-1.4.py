def squaresum(item):
    total = 0
    for k in range(item+1):
        total += k * k
    return total


print(squaresum(3))