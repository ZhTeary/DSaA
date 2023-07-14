def oddsum(n):
    total = 0
    for i in range(1,n+1):
        if i%2 == 1 :
            total += i*i
    return total


print(oddsum(5))