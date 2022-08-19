
# 集合
# 集合只能存储不可变对象
# 集合中国存储的对象是无序的
# 集合中不能存在重复的数据

s = {9,3,1,2,3,4}
print(s,type(s))
# 空集合
s1 = set()

# 将序列和字典转换成集合
s = [1,2,2,4,5,8,5]
s2 = set(s)
print(s2)
s2 = set('hello')
print(s2)
# 转换字典时,只包含key
s2 = set({'name':'雷电将军','age':32})
print(s2)

s3 = {'a','d',2,3,1,5,5,5}
# 集合无法通过索引来操作
print(s3)
# in not in 是否存在
print(5 in s3)

# len() 长度
print(len(s3))

# add()向集合中添加元素
s3.add(10)
print(s3)

# update()将一个集合中元素添加到一个另一个集合
# update()可以传递序列和字典作为参数,字典只传key
s4 = {9999}
s4.update(s3)
print(s4)


# pop()随机删除一个集合中的元素并返回
print(s4.pop())
print(s4)

# remove()删除集合中的指定元素
s4.remove(9999)
print(s4)

# clear()清空
s4.clear()
print(s4)

# copy() 对集合浅复制

