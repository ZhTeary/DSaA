def isdif(li):
    for i in range(0, len(li)):
        for u in range(i + 1, len(li)):
            if li[i] == li[u]:
                return False
    return True


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("li is dif :", isdif(li))
