def reverseList(li: list):
    for i in range(0, int(len(li) / 2)):
        li[i], li[len(li) - i - 1] = li[len(li) - i - 1], li[i]


li = [1, 2, 3, 4, 5]
reverseList(li)
print(li)

# 内置
li.reverse()
print(li)
