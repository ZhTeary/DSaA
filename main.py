from Ch06_Stack_Queue.Demo.ArrayStack import ArrayStack


# def insert_at_bottom(S: ArrayStack, item):
#     if len(S) == 0:
#         S.push(item)
#     else:
#         temp = S.pop()
#         insert_at_bottom(S, item)
#         S.push(temp)
#
#
# def reverse_stack(S: ArrayStack):
#     if not S.is_empty():
#         temp = S.pop()
#         reverse_stack(S)
#         insert_at_bottom(S,temp)


def rev_stk(S:ArrayStack):
    result = S.pop()
    if S.is_empty():
        return result
    else:
        last = rev_stk(S)
        S.push(last)
        return last

if __name__ == '__main__':
    A = ArrayStack()
    A.push(1)
    A.push(2)
    A.push(3)
    rev_stk(A)
    # reverse_stack(A)
    # insert_at_bottom(A, A.pop())
    # insert_at_bottom(A, A.pop())

    # insert_at_bottom(A, A.pop())

    print(A)

