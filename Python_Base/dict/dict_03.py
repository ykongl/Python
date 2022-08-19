
# 遍历字典
# keys() 该方法会返回字典的所有的key
d = {'name': '班尼特', 'age': 12}
print(d.keys())

for k in d.keys():
    print(d[k])
# values()返回字典中所有的value
for v in d.values():
    print(v)

# items()
# 该方法会返回字典中所有的项
# 他会返回一个序列,序列中包含有双值子序列
# 双值分别是字典中的key和value
print(d.items())

for k,v in d.items():
    print(k,v)