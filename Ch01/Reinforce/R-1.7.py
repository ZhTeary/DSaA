def oddsum(n):
    total = sum([i*i if i %2 == 1 else 0 for i in range(1,n+1)] )
    return total


print(oddsum(5))