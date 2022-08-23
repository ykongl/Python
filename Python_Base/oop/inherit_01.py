
# 继承
# 面向对象三大特征之一
# 定义一个类 Animal(动物)
#  这个类中需要两个方法:run() sleep()
class Animal:
    def __init__(self,name):
        self._name = name

    def run(self):
        print(self._name, '动物会跑。。。。')

    def sleep(self):
        print(self._name, '动物睡觉...')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name



# 定义一个类Dog
# run().sleep(),bark()三个方法

# 父类中的所有方法都会被子类继承，包括特殊方法

class Dog(Animal):
    def __init__(self,name,age):
        # 直接调用父类的__init__来初始化父类中定义的属性
        # Animal.__init__(self,name)
        # super()可以用来获取当前类的父类
        super().__init__(name)
        # self._name = name
        self._age = age

    def bark(self):
        print(self._age,"狗在叫。。。")

    def run(self):
        print('跑。。。')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age


d = Dog('旺财',12)
d.name = '小黑'
d.run()
d.sleep()
d.bark()

h = Animal('123')
# True
r = isinstance(d, Dog)
# True
r = isinstance(d, Animal)
# False
r = isinstance(h, Dog)
print(r)

# object类是所有类的父类，所有类都继承Object


# 重写
# 当前对象有该方法，直接使用，没有就去父类找。一直没找到就报错
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')

c = C()
c.test()