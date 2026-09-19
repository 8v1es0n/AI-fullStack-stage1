# 函数的嵌套调用
# 先进后出, 后进先出
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")


def function_b():
    print("b ... before")
    function_c()
    print("b ... after")


def function_c():
    print("c ...")


# 函数的调用
function_a()

print("函数调用完毕 ~")
