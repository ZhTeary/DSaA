from Ch06_Stack_Queue.Demo.ArrayStack import ArrayStack

LEFTY = '({['
RIGHTY = ')}]'
S = ArrayStack()

def RecursionDelimiters(expr: str):
    if len(expr)==0:
        return S.is_empty()
    c = expr[0]
    if c in LEFTY:
        S.push(c)
    elif c in RIGHTY:
        if S.is_empty() or RIGHTY.index(c) != LEFTY.index(S.pop()):
            return False
    return RecursionDelimiters(expr[1:])

#
# def symbol_matching(string):
opening_symbols = ['(', '[', '{']
closing_symbols = [')', ']', '}']
symbol_pairs = {'(': ')', '[': ']', '{': '}'}

#
# def is_matching_recursive(string, stack):
#     if len(string) == 0:
#         return len(stack) == 0
#
#     char = string[0]
#     if char in opening_symbols:
#         stack.append(char)
#     elif char in closing_symbols:
#         if len(stack) == 0 or symbol_pairs[stack.pop()] != char:
#             return False
#
#     return is_matching_recursive(string[1:], stack)


#
# return is_matching_recursive(string, [])
#
# # 测试
# print(symbol_matching("()"))  # True
# print(symbol_matching("([{}])"))  # True
# print(symbol_matching("([)]"))  # False


if __name__ == '__main__':
    # print(RecursionDelimiters('cc(123)cc'))
    # print(is_matching_recursive("({{[}}])",[]))  # False
    s = 'a'
    # s = s[0]
    # print(s)
    s = s[1:]
    print(s)