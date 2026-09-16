"""
    ****
    ****
    ****
"""
for i in range(1, 4):   # 控制行
    for j in range(4):  # 控制列
        print("*", end="")    # 不换行输出
    print()
print("-----------------------")

"""
    *
    **
    ***
    ****
"""
for x in range(1, 5):   # 控制行
    for y in range(1, x + 1):  # 控制列
        print("*", end="")    # 不换行输出
    print()
print("-----------------------")

"""
    ****
    ***
    **
    *
"""
for a in range(1, 5):   # 控制行
    for b in range(1, 6 - a):  # 控制列
        print("*", end="")    # 不换行输出
    print()
print("-----------------------")

#  九九乘法表
for num_x in range(1, 10):
    for num_y in range(1, num_x + 1):
        print(f"{num_y} × {num_x} = {num_x * num_y}", end="\t")
        if num_x == num_y:
            print()
