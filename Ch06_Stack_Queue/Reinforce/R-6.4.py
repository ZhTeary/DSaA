from Ch06_Stack_Queue.Demo.ArrayStack import ArrayStack


def CleanList(S: ArrayStack):
    S.pop()
    while not S.is_empty():
        CleanList(S)

