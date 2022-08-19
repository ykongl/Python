
# 字典(dict) 称为映射mapping
# 与列表类似，用来存储对象的容器
# 列表存储数据性能好，数据查询的性能很差
# 字典查询数据效率高
# 字典可以保存多个对象(value)，每个对象都有唯一的名字(key 键)
# 字典 (key-value)键值对

d = {}
print(d,type(d))

# 语法{key:value,key:value}
# value可以是任意对象
# key是任意的不可变对象(int,str,bool,tuple...)
# key不能重复
d = {'name':'孙悟空','age':19}
print(d)
print(d['name'],d['age'])
