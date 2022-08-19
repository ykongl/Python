# 元组 tuple
# 不可变序列

# 创建
tuple01 = ()
print(tuple01,type(tuple01))

tuple02 = (1,2,3)
print(tuple02)
# tuple02[0] = 99不能改变
# 括号可以省略,至少有一个值
tuple03 = 1,2,3,4
print(tuple03,type(tuple03))


# 元组的解包（list,字符串都可以）
# 解包指就是将元组当中每一个元素都赋值给一个变量
a,b,c,d = tuple03
print(a,b,c,d)

x = 100
y = 200
x, y = y, x
print(x, y)


tuple04 = 1,2,3,4,5,6
# 变量数量与元组数量必须一致，或者加*（*只能有一个，位置任意）
a,b,*c = tuple04
print(a,b,c)