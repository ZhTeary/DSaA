def prefix_average(s: list):
    n = len(s)
    Ans = [0] * n
    total = 0
    for i in range(n):
        total = total + s[i]
        Ans[i] = total / (i + 1)
    return Ans


a = [1, 2, 3, 4, 5]
a = prefix_average(a)
print(a)
