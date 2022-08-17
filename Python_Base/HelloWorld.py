print('HelloWorld!')
print(123 + 456)

a = 'hello %s'%'ss'
print(a)
# %s 在字符串中表示任意字符
# %f 浮点数占位符
# %d 整数占位符
d = 'hello %.2f'%123.789
print(d)

a = 123
b = 'hello %d'%123.54
c = f'hello {a} {b}'
# 格式化字符串，可以通过字符串前添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
print(c)