import random


def myshuffle(li: list):
    #  序列相等 每个 都一样
    li.pop()
    random.randint(0, len(li))
    return li
