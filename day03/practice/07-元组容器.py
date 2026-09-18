#   元组特点: 有序, 可重复, 不可修改, 可存储多种元素

# 定义格式
tuple01 = (55, 44, 88, 88, 55, 22, 10)

# 定义空元素
tuple02 = ()
tuple03 = tuple()

# 元素不可修改
# tuple01[3] = 10

# 切片
print(tuple01[1: 5: 2])

# 统计元组中某个元素中出现的次数
count = tuple01.count(22)
print(count)

# 查找某个元素在元组中的索引位置(第一次出现的位置)
print(tuple01.index(22))

# 注意事项: 定义一个只有一个元素的元组时
tuple04 = (100,)
print(tuple04)