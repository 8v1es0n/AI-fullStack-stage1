# 注意 : 函数存在默认值参数 , 需要把它放在参数列表的最后位置 , 可以存在多个默认值参数
def add(a, b=20, c=10):
    return a + b + c


# 赋值调用
# result = add(10, 20, 30)
# print(result)

# 输出调用
print(add(100))
