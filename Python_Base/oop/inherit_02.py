
# 多重继承
# 子类同时拥有多个父类，获取所有父类中的方法
# 避免使用多重继承
# 前边父类的方法会覆盖后边父类的方法

class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test2(self):
        print('BBB')


class C(B):
    pass
# 类名._bases_这个属性可以用来获取当前类的所有父类
# (<class '__main__.B'>,)
print(C.__bases__)
# (<class '__main__.A'>,)
print(B.__bases__)

class D(A, B):
    pass

# (<class '__main__.A'>, <class '__main__.B'>)
print(D.__bases__)