a = 10  # 全局变量
b = 20  # 全局变量
c = 100  # 全局变量


def get_sum(x, y): # x y 局部变量 : 只能在所在的函数中使用
    print(a)
    print(b)

    # 局部变量
    # global c
    c = 1000
    # 局部变量 和 成员变量重名使用: 局部的 , 就近原则
    print(c)
    return x + y


# print(c , x , y)
print(a , b , c)
print(get_sum(10, 20))
