
# print('测试模块')
# 模块中定义变量和方法，引入模块后，可以直接使用
a = 10
b = 30

# 添加_的变量,只能在模块内部访问,再通过import* 引入时,不会引入_开头的变量
_c = 22


def test():
    print('无想一刀')


def test2():
    print("天动万象")


# 判断是否是主模块
if __name__ == '__main__':
    test()
    test2()