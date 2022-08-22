
# 类
# 创建一个int类的实例
a = int(10)

# 创建一个str类的实例
b = str('hello')

# print(a,type(a))
# print(b,type(b))

# 定义一个简单的类
class MyClass():
    pass


print(MyClass)
# 使用MyClass创建一个对象
mc = MyClass()

print(mc,type(mc))

# isinstance()检查一个对象是否是另一个类的实例
result = isinstance(mc,MyClass)
# True
print(result)