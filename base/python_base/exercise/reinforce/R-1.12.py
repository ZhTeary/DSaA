# 1. random num
# 2. use in randrange
import random
import time


def myChoice(li: list):
    t = time.time()
    random.seed(t)
    r = random.randrange(0, len(li))
    print(li[r])


li = ["a", "b", "c", "d", "e"]
myChoice(li)
