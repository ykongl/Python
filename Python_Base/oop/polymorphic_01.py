
# 多态,三大特征之一
# 一个对象可以以不同的形态去呈现

class A:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name


class B:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self,name):
        self._name = name


class C:
    pass


a = A('孙悟空')

b = B('猪八戒')

# 定义一个函数
# 对于say_hello()这个函数来说,只要对象中含有name属性,他就可以作为参数传递
#  这个函数并不会考虑对象的类型,只要有name属性即可


def say_hello(obj):
    print('你好 %s'%obj.name)


# 在say_hello_2中我们做了一个类型检查,也就是只有obj是A类型对象时,才可以正常使用
#  其他类型的对象都无法使用该函数
# say_hello(b)


def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('你好 %s'%obj.name)


say_hello_2(b)