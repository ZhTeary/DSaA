# 可变对象：list, set, dict 作为参数时直接传递自身，会随着函数中的修改儿修改
# 不可变对象： bool, int, float, tuple, str, frozenset 作为参数时会产生复制的形参，在函数中的修改不影响自身


def scale(data, factor):
    for val in data:
        val *= factor


def scale_new(data, factor):
    for v in range(0, len(data)):
        data[v] *= factor


data = [1, 2, 3, 4, 5]
scale(data, 2)
print(data)

scale_new(data,2)
print(data)


