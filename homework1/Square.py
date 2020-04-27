def square_sort(l):
    alist = [num ** 2 for num in l]  # 将list的元素平方
    alist.sort()  # 降序排序
    return alist  # 返回排序后的list


a = [-4, -1, 0, 3, 10]

print(a)
print(square_sort(a))



class XuZhu(TongLao):
    def __init__(self, hp, power, age):
        super(XuZhu, self).__init__(hp, power)
        self.age = age

    def read(self):
        print('罪过罪过')