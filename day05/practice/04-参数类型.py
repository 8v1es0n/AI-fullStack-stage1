# 加
def add(a, b):
    return a + b


# 减
def sub(a, b):
    return a - b


# 乘
def mul(a, b):
    return a * b


# 除
def div(a, b):
    return a / b


#  / : 左边必须是位置参数
#  * : 右边必须是关键字参数
def calc(x, y, *, operator):
    # 调用mul,函数
    result = operator(x, y)
    return result


rs = calc(x=1, y=2, operator=lambda a, b: a + b)
print(rs)

# def calc2(a , b , * ,  c):
#     print(a + b + c)
#
# calc2(1 ,   2 ,  c = 3)


data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]

data_list.sort(key=lambda a: len(a))
#
# print(data_list)

# def sort_len(item):
#     return len(item)
# add = lambda a , b : print("hello")

# sort函数中 有一个参数 key  参数key需要的是一个函数
# 函数需要有一个形参 , item参数代表的就是列表中的每一个元素
# 匿名函数的函数体是len(item) , 所以根据字符串的长度进行排序
# data_list.sort(key=lambda item: len(item))
# print(data_list)
