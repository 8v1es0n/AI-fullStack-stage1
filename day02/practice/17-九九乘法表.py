#  九九乘法表
for num_x in range(1, 10):
    for num_y in range(1, num_x + 1):
        print(f"{num_y} × {num_x} = {num_x * num_y}", end="\t")
        if num_x == num_y:
            print()