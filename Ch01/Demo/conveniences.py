def demo_func(n):
    print("It is a demo, Param is", n)


# 1. 条件表达式
# old
# if n >= 0:
#     print(n)
# else:
#     print(-n)

# new
n = -1
res = n if n >= 0 else -n

print(res)

# 2. 解析语法
# 一般形式  expression for value in iterable if condition
# for value in iteraor:
#     if condition:
#         ...do somehings...

# 列表解析
squares = [k * k for k in range(1, n + 1)]
factors = [k for k in range(1, n + 1) if n % k == 0]
# 集合解析
collections = {k * k for k in range(1, n + 1)}
# 生成器解析
gen = (k * k for k in range(1, n + 1))
# 字典解析
dic = {k: k * k for k in range(1, n + 1)}
# 当结果不需要存在内存中时，生成器语法特别有优势：
total = sum(k * k for k in range(1, n + 1))

# 3.序列类型的打包和解包
# 自动打包
data = 2, 4, 6, 8  # 自动识别成 data = (2, 4, 6, 8)
# 自动解包
a, b, c, d = range(7, 11)
# 同时分配
# 自动打包和解包结合起来就是 同时分配 技术
x,y,z = 1,2,3
# 该赋值右边将自动打包成元组，然后自动解包，将元素分配给左边的三个字符
