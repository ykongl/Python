
# 异常对象

try:
    print(10/0)
except NameError:
    print('NameError错误')
except Exception as e:
    print(type(e))
except ZeroDivisionError:
    print('ZeroDivisionError错误')

# Exception是所有的异常对象的父类

