
# 在类中可以定义一些特殊方法(魔术方法)
# 特殊方法都是以_开头，_结尾的方法
# 特殊方法不需要自己调用
# 特殊方法会自动调用

# 创建对象的流程
# p1 = Person()的运行流程
#  1.创建一个变量
#  2.在内存中创建一个新对象
#  3.__init__(self)方法执行:
#  4.将对象的id复制给变量
# init会在对象创建以后离开执行
# init可以用来向新创建的对象中初始化属性


class Person:
    # 初始化信息
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print("你好", self.name)


p1 = Person('雷电将军')
# 不需要自己调用
# p1.__init__()
p1.say_hello()
