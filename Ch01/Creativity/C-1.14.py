def multiOdd(li):
    for i in range(0, len(li)):
        for u in range(i + 1, len(li)):
            if (li[i] * li[u]) % 2 == 1:
                yield li[i],li[u]


payload = multiOdd([1, 2, 3, 4, 5])
for i in payload:
    print(i)
