# 装饰器

def fn1(a, b):
    r = a + b
    return r


def mul(a, b):
    r = a * b
    return r


# 希望函数可以在计算前，打印开始计算，结束后打印计算结束
# 直接修改代码会产生以下问题
# 1.修改麻烦，数量过多
# 2.不方便后期维护
# 3.违反开闭原则（ocp）

# def fn(a, b):
#     print("计算开始")
#     print(fn1(a, b))
#     print("计算结束")
#
#
# fn(1, 2)

# 自动生产

def begin_end(old):
    def new_function(a, b):
        print("计算开始")
        print(old(a, b))
        print("计算结束")

    return new_function


# f = begin_end(mul)
#
# f(1, 2)
# begin_end()就是装饰器
# 通过装饰器,可以在不修改原来函数的情况下来对函数进行扩展
# 在开发中,我们都是通过装饰器来扩展函数的功能
# 定义函数时,可以通过@装饰器,来使用指定的装饰器,来装饰当前的函数
# 可以同时为一个函数指定多个
@begin_end
def say_hello():
    print('大家好')

say_hello()