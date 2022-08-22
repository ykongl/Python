# 闭包
# 将函数作为返回值返回，也是一种高阶函数
# 这种告诫函数称为闭包，通过闭包可以创建一些只有当前函数能访问的变量
# 可以将一些私有的数据藏到闭包中
# 形成闭包条件
# 1.函数嵌套
# 2将内部函数作为返回值返回
# 3内部函数必须要使用到外部函数的变量
def fn():
    a = 10

    def inner():
        print('我是fn2', a)

    return inner


# r是一个函数，时调用fn()后返回的函数
# 这个函数是在fn()内部定义，并不是全局函数
# 所以这个函数总是能访问到fn()函数内的变量

r = fn()


# r()


def make_averager():
    nums = []

    def averager(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return averager


averager = make_averager()
print(averager(10))
print(averager(20))
