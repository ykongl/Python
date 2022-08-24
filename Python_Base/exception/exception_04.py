
# 自定义异常
class MyError(Exception):
    pass


def add(a, b):
    # 如果a 和 b中有负数,就向调用出抛出异常
    if a < 0 or b < 0:
        # raise用于向外部抛出异常
        raise MyError('参数不能为负数!!')
    return a + b


print(add(1, -1))



