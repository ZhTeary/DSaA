"""
    生成器Generator语法实现类似于函数，但不返回值

"""


# 返回值
def factors1(n):
    results = []
    for i in range(1, n + 1):
        if n % i == 0:
            results.append(i)
    return results


# 生成器1
def factors2(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


# 生成器2
def factors3(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


r1 = factors1(100)
r2 = factors2(100)
r3 = factors3(100)
print("返回值：\n",r1)
print("直接输出生成器:\n",r2)

"""
想拿到生成器里面的值 得对生成器遍历
"""
print("遍历生成器才能拿到里面的值:")
for i in r3:
    print(i)

