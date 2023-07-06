""" only contains origin English alpha"""


# WARNING: do not do this
def wrong_method(document: str):
    """
    效率非常低下, 因为字符串大小固定, 指令letters+=c 很可能串联部分letters+c
    并把结果作为新的字符串实例且重新分配给标识符letters
    构造新字符串所用时间与该字符串的长度成正比
    假如最终结果有n个字符，那花费时间与求和公式1+2+3+..+n成正比，
    所以运行时间为O(n^2)
    """
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c


def right_method(document:str):
    """
    保证在线性时间内组成字符串的另一个标准是：
        使用临时表存储单个数据，然后使用字符串类的join方法组合最终结果
    该方法能确保运行时间为O(n)
    首先，连续n次append共需要O(n)；其次对join的调用也能保证线性
    """
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)

# 列表简便写法: 使用临时表
document = 'a,b,c,d e f g'
letters = ''.join([c for c in document if c.isalpha()])
# 更简便: 使用生成器
letters2 = ''.join(c for c in document if c.isalpha())