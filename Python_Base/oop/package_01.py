
# 封装，面向对象的三大特性之一
# 封装，是指隐藏对象中一些不希望被外部所访问到的属性或方法


class Dog:
    def __init__(self, name,age):
        self.hidden_name = name
        self.age = age

    def say_hel(self):
        print('大家好',self.hidden_name)

    # get/set方法取值赋值
    def get_name(self):
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name




d = Dog('旺财',11)
d.name = '小黑'
d.say_hel()
d.set_name('爆米花')
print(d.get_name())

# 双下划线开头的属性,是对象的隐藏属性,隐藏属性只能在类的内部访问,无法通过对象访问

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person('hhh')
p.set_name('sss')
# p.__name = 'aa'
# print(p._Person__name)依然可以访问
print(p.get_name())