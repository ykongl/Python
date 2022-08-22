
# property装饰器
class Person:
    def __init__(self,name):
        self._name = name

    # property装饰器,用来将一个get方法,转换为对象的属性
    @property
    def name(self):
        return self._name

    # setter方法的装饰器:@属性名.setter
    @name.setter
    def name(self, name):
        self._name = name

p = Person('猪八戒')
p.name = '123'
print(p.name)
