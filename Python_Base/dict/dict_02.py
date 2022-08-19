# 字典的使用
# 创建{key:value,key:value}
b = {'name': '孙悟空', 'age': 19}
# 使用dict()函数创建字典
d = dict(name='孙悟空', age=11, sex='男')
print(d, type(d))

# 双值子序列转换为字典[(1,2),(3,4)]
d = dict([('name', '雷电将军'), ('age', 22)])
print(d, type(d))

# len()获取长度
print(len(d))

# in not in 检查字典中是否包含指定的键
print('name' in d)
# d[key]
# key不存在会报错
print(d['name'])

# 不会报错
print(d.get('name'))
print(d.get('123'))
# 如果key不存在，会返回默认值
print(d.get('123', '默认值'))

# 修改
d['name'] = '钟离'
print(d)
# 添加
d['属性'] = '岩'
print(d)

# setdefault(key,default)
# 如果key已经存在,则返回key的值,不会对字典做任何操作
# 如果key不存在,则向字典中添加这个key,并设置value
re = d.setdefault('name', '雷电将军')
print(re)
re = d.setdefault('hh', '雷电将军')
print(d)

# update([other])
# 将其他的字典中的key-value添加到当前字典中
a = {'name': '班尼特', 'age': 12}
c = {'属性': '火', '武器': '单手剑'}
a.update(c)
print(a)

# 删除字典 del
del a['武器']
print(a)

# popitem()
# 随机删除字典中的一个键值对,一般是最后一个
# 删除的键值对作为返回值返回.返回的是一个元组
a.popitem()
result = a.popitem()
print(result)
print(a)

# pop(key)
# 根据key删除,返回被删除的value
# 删除不存在的key会报错,指定默认值则不会
z = {'name': '班尼特', 'age': 12}
result = z.pop('name')
result1 = z.pop('sss', '默认值')
print(result1)
print(result)
print(z)

# clear() 清空
z.clear()
print(z)

# copy()
# 对字典进行浅复制
# 复制以后的对象与原对象是相互独立的.
# 浅复制会简单复制对象内部的值,如果值也是一个可变对象,这个可变对象不会被复制
q = dict([('name', '雷电将军'), ('age', 22)])
q1 = q
q2 = q.copy()
print(q,id(q))
print(q1,id(q1))
print(q2,id(q2))
