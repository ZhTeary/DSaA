class Flower:
    def __init__(self, name, number, price):
        self._name = name
        self._number = number
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_price(self):
        return self._price

# R-2.5~2.8 见Credit
# 为什么没有参数的异常不能捕获！！！ 因为这个问题 出在外面 ，应该在外面捕获异常

# R-2.9-2.15 见Vector

# 2.16 不会

