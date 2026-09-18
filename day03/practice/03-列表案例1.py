#   案例一:
# 1. 将用户输入的10个数字，存储到一个列表中，
# 并将列表中的数字进行排序, 输出其中的最小值、最大值 和 平均值。

num_list = []

for num in range(1,11):
    num_value = int(input(f"请输入第 {num} 个数字: "))
    num_list.append(num_value)

print(num_list)

# 排序后的列表
num_list.sort()
print(num_list)

print("最小值: ", min(num_list))
print("最大值: ", max(num_list))
print("求和: ", sum(num_list))
print("平均值: ", sum(num_list)/len(num_list))