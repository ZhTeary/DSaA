# # 带缓存的递归
# cache = {}
#
#
# def climbStairs(n: int) -> int:
#     if n == 1 or n == 0:
#         return 1
#     if n in cache:
#         return cache[n]
#     else:
#         cache[n] = climbStairs(n - 1) + climbStairs(n - 2)
#
#         return cache[n]
#
#
# print(climbStairs(2))
#
# mat = np.array([[2,0],[0,2]])
import numpy as np