def square_sort(l):
    alist = [num ** 2 for num in l]
    alist.sort()
    return alist


a = [-4, -1, 0, 3, 10]

print(a)
print(square_sort(a))

class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def __see_people(self, name):
        if name == 'WYZ':
            print('师弟！！！！')
        if name == 'LQS':
            print('呸，贱人')
        if name == 'DCQ':
            print('叛徒！我杀了你')

    def __fight_zms(self, enermy_hp, enermy_power):
        self.hp /= 2
        self.power *= 10
        if self.hp - enermy_power > enermy_hp - self.power:
            print('Tonglao wins')
        else:
            print('The enermy wins')

class XuZhu(TongLao):
    def __init__(self, hp, power, age):
        super(XuZhu, self).__init__(hp, power)
        self.age = age

    def read(self):
        print('罪过罪过')