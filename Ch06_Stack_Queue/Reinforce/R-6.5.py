from Ch06_Stack_Queue.Demo.ArrayStack import ArrayStack


def reverseList(L: list)->list:
    S = ArrayStack()
    length = len(L)
    for i in range(length):
        S.push(L[i])
    L = [None] * length
    for i in range(length):
        L[i] = S.pop()
    return L


L = [1, 2, 3, 4, 5]
L = reverseList(L)
print(L)
