# list01 = [10,'hello',1,2,True,[1,2,3],print]
# # 索引index（可以为负数）
# print(list01[-7])
# print(list01)

# # 切片：从现有列表中，获取一个子列表[x,y)
# list02 = list01[1:5]
# list03 = list01[1:]
# list04 = list01[:6]
# list05 = list01[:]
# print(list02)
# print(list03)
# print(list04)
# print(list05)

# # [起始：结束：步长]（步长可以是负数，不能为0）
# list06 = list01[::-1]
# print(list06)

# # + *
# list_01 = [1,2,3] + [4,5,6]
# print(list_01)
# list_02 = [1,2,3] * 2
# print(list_02)

# # in not in
# list_03 = [1,2,3]
# print(1 in list_03)
# print(1 not in list_03)

# # len max min
# list_04 = [1,2,3]
# print(len(list_04))
# print(max(list_04))
# print(min(list_04))

# .index()第一次出现的索引 .index(元素,开始位置,结束位置)
# .count()统计次数
list_05 = [1,2,3,2]
print(list_05.index(2,1,3))
print(list_05.count(2))