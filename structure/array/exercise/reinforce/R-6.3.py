from structure.Ch06_Stack_Queue.Stack.ArrayStack import ArrayStack


def transfer(S: ArrayStack, T: ArrayStack) -> ArrayStack:
    while not S.is_empty():
        temp = S.pop()
        T.push(temp)
    return T


if __name__ == '__main__':
    S = ArrayStack()
    for i in range(10):
        S.push(i)
    T = ArrayStack()
    T = transfer(S, T)
    # while not T.is_empty():
    #     print(T.pop())
    print(T )