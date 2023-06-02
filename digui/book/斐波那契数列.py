# 给定整数N 返回斐波那契数列的第N项
# O(2n)
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# O(2n) 加缓存
def f(n: int) -> int:
    cache = {}
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = f(n - 1) + f(n - 2)
        return cache[n]


print(f(4))


# O(n) 动态规划-滚动数组
def fib2(n: int) -> int:
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    pre = 1
    cur = 1
    ans = 0
    for i in range(2, n):
        ans = pre + cur
        pre = cur
        cur = ans
    return ans

# O(logN)
# 如果递归式严格遵循F(N) = F(N-1) + F(N-2)
