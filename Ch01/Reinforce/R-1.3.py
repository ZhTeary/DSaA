def minmax(data):
    mini = maxi = data[0]
    for i in data:
        if mini > i:
            mini = i
        if maxi < i:
            maxi = i
    return mini, maxi


l = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]
mini, maxi = minmax(l)
print(mini, maxi)
