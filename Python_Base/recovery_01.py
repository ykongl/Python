# 垃圾回收

# 在程序中没有被引用的对象就是垃圾,及时清理,否则影响程序性能

class A:
    def __init__(self):
        self.name = 'A类'

    # del是一个特殊方法,会在对象被垃圾回收前调用

    def __del__(self):
        print('A被删除')


a = A()
print(a.name)
a = None
# python中有自动的垃圾回收机制,会自动将这些没有被引用的对象删除
