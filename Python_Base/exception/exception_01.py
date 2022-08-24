
# 异常
# 程序运行中,出现异常错误,程序终止

# 处理异常
# try:代码块(可能错误语句) except:(出现错误以后的处理方式)else:(没出错时要执行的语句) finally:(该部分代码块总会执行)

print('hello')
try:
    print(10/2)
except:
    print('出错了')
else:
    print('没错')
finally:
    print('总会被执行')