# 类
class Person:

    # 类中的函数称为方法

    def say_hello(self):
        print(self.name, '您好')


p1 = Person()
p1.name = '雷电将军'
p1.say_hello()
p2 = Person()
p2.name = '钟离'
p2.say_hello()