"""
2. 题目2：列表合并去重 + 列表推导式
"""
# 已知两个班级的学员编号：
class_a = [101, 102, 105, 108, 102, 110, 105, 112, 108]
class_b = [105, 106, 108, 109, 111, 101, 113, 106]

# 1. 合并两个列表的数据，得到合并后的原始列表 merged
merged = class_a + class_b

# 2. 对 merged 进行列表去重，保留第一次出现的顺序，得到 unique_list
unique_list = []
for item in merged:
    if item not in unique_list:
        unique_list.append(item)

# 3. 使用列表推导式，从 unique_list 中筛选出所有的奇数编号，生成 odd_list，并输出
odd_list = [unique for unique in unique_list if unique % 2 != 0]
print(f"3. 奇数编号列表: {odd_list}")

# 4. 使用列表推导式，odd_list 中每个元素在其基础上加 10000，生成 new_list，并输出
new_list = [num + 10000 for num in odd_list]
print(f"4. 加 10000 后的列表: {new_list}")