# 运算符
# -算术运算符(+，-，*，/,//,**,%)
# -赋值运算符(+=,-=,/=,*=,**=,//=,%=)
# -逻辑运算符(not非,and与,or或)
# 非布尔值的与或运算
#   当我们对非布尔值进行与或运算时，Python会将其当作布尔值运算，最终会返回原值
result = 1 and 2
print(result)
result = 1 and 0
print(result)
result = 0 and 1
print(result)

# 条件运算符(三元运算符)
print(1) if 1 > 2 else print(2)