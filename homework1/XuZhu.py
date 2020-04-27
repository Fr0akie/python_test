from homework1.TongLao import TongLao

class XuZhu(TongLao):
    def __init__(self, hp, power, age):
        super(XuZhu, self).__init__(hp, power)
        self.age = age

    def read(self):
        print('罪过罪过')

xuzhu = XuZhu(10000, 5000, 20)
xuzhu.read()