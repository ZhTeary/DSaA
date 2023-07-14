from structure.Ch06_Stack_Queue.Stack.ArrayStack import ArrayStack


def CleanList(S: ArrayStack):
    S.pop()
    while not S.is_empty():
        CleanList(S)

