class Car:  # 定义一个车类
    def __init__(self, weight, color, brand):  # 成员变量有重量，颜色和品牌
        self.weight = weight
        self.color= color
        self.brand = brand

    def drive(self, distance):  # 方法开车， 参数为开车距离，单位为km
        print('这车要开{}km'.format(distance))


GTR = Car(1000, 'black', 'GTR')
GTR.drive(10)


class Cat:  # 定义一个猫类
    def __init__(self, color, gender):  # 成员变量有颜色和性别
        self.color = color
        self.gender = gender

    def eat(self):  # 方法吃， 如果颜色是橘色，则要吃很多鱼
        if self.color == 'orange':
            print('橘猫要吃很多鱼')
        else:
            print('猫要吃鱼')


orange_cat = Cat('orange', 'male')
orange_cat.eat()


class Person:  # 定义一个人类
    def __init__(self, gender, age, prefession):  # 成员变量有性别，年龄和职业
        self.gender = gender
        self.age = age
        self.profession = prefession

    def do_sth(self):  # 方法做事，职业是学生则学习，是工人则干活
        if self.profession == 'student':
            print('我是学生，我要学习')
        elif self.profession == 'worker':
            print('我是工人，我要干活')


employee = Person('male', '25', 'worker')
employee.do_sth()


class Calculator:  # 定义一个计算器类
    def __init__(self, brand):  # 成员变量有品牌
        self.brand = brand

    def product(self):  # 方法产品
        if self.brand == '卡西欧':
            print('卡西欧计算器，学生最爱')
        elif self.brand == '德州':
            print('德州计算器，高端')


casio = Calculator('卡西欧')
casio.product()


class bank_account:  # 定义一个银行类
    def __init__(self, branch, money):  # 成员变量有分行，存款数
        self.branch = branch
        self.money = money

    def deposit(self, deposit):  # 方法存款， 参数有存款数，存款增加要存的钱
        if deposit > 0:
            self.money += deposit
        else:
            print('操作异常，存款数必须大于0')

    def show_money(self):
        print('该账号有{}钱'.format(self.money))
        return self.money


account = bank_account('ICBC', 1000)
print(account.show_money())
account.deposit(200)
print(account.show_money())

