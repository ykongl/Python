
# 异常传播(抛出异常)
# 当函数中出现异常时,如果对异常进行处理了,则不会继续传播
# 如果没有处理,则会向调用出传播异常,直到主模块(全局)依然没有处理,程序终止.

# print(10/0)

# def fn():
#     print('hello')
#     try:
#         print(10 / 0)
#     except:
#         print(123)
#     else:
#         print('0000')
#
#
# # 当在函数中出现异常时,如果在函数中对异常进行了处理,则异常不会再继续
# fn()


def fn2():
    print('fn2')
    print(10 / 0)


try:
    fn2()
except:
    print('error')
else:
    print('success')

# 异常对象信息会被保存到一个异常对象中.
# 例:ZeroDivisionError类的对象专门用来表示除0的异常
