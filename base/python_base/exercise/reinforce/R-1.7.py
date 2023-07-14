def oddsum(n):
    total = sum([i * i for i in range(1, n + 1) if i % 2 == 1])
    return total


print(oddsum(5))