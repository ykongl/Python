
# 特殊方法
# 特殊方法都是使用__开头和结尾的
# 特殊方法一般不需要我们手动调用,需要在一些特殊情况下自动执行

# 定义一个Person类
class Person(object):
    def __init__(self, name, age):
        super(Person, self).__init__()
        self.name = name
        self.age = age

    # __str__()会在尝试将对象转换为字符串的时候调用
    # 可以用来指定对象转换为字符串的结果
    def __str__(self):
        return '123'

    # __repr__()对当前对象使用repr()函数时调用
    # 作用是指定对象在'交互模式'中直接输出的效果
    def __repr__(self):
        return 'hello'

    # object.__lt__(self,other)小于
    # object.__le__(self,other)小于等于
    # object.__eq__(self,other)等于
    # object.__ne__(self,other)不等于
    # object.__gt__(self,other)大于
    # object.__ge__(self,other)大于等于

    # __gt__会在对象做大于比较的时候调用.该方法的返回值将会作为比较的结果
    def __gt__(self, other):
        return self.age > other.age

    # __len__()获取对象的长度

    # object.__bool__(self)
    # 可以通过bool来指定对象转换为布尔值的情况
    def __bool__(self):
        return True

p1 = Person('雷电将军',18)
p2 = Person('温蒂',222)

# 打印对象时,实际上打印的是对象中的特殊方法__str__()的返回值
print(repr(p1), p2)

print(p1 < p2)