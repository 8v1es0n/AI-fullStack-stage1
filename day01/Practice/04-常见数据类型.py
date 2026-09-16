# 定义变量

# 通过type()语句来得到数据/变量的类型
print(type(1), type(2.1), type("abc"))
print(type(True), type(None))

# 通过 isinstance() 语句来检查数据是否属于指定的类型，返回的是一个bool值
# bool = True
print(isinstance(1.1, float))
# bool = False
print(isinstance("abc",int))

print("--------------------------")