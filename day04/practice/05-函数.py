# 函数 : 可以完成特定的代码块 , 提高代码的复用性!!!

"""
    def 函数名(参数列表):
        函数体
        return 返回值

    def : 关键字 , 固定的
    函数名 : 见名之意 , 符合规则(蛇形命名法) , 后续使用此函数需要通过函数名使用
    (参数列表) : 函数体需要用到的数据
    函数体 : 因为函数可以完成特定的功能 , 所以函数体就完成特定功能的代码
    return 返回值 : 把函数结束, 并把值返回给调用者
"""


# 求两个数据的较大值
def get_max(num1, num2):
    """
    当前函数的功能是求两个数据的较大值
    :param num1:  第一个数据
    :param num2:  第二个数据
    :return: 最大值
    """
    if num1 > num2:
        max = num1
    else:
        max = num2
    return max


# 有返回值的函数调用方式有两种
# 方式1 : 赋值调用
result1 = get_max(10, 20)
print(result1)
# 方式2 : 输出调用
print(get_max(20, 30))


# 打印10次helloworld
def print_hello():
    """
    打印10次helloworld
    :return: 无
    """
    for i in range(10):
        print("hello world")


# 当函数没有返回值时 , 只能直接调用
# 调用 : 直接调用
print_hello()


# 函数的调用格式 : 函数名(传递参数)
# 注意1 : 必须先定义函数 , 才能调用函数
# 注意2 : 调用函数, 函数需要几个参数就必须传递几个数据值


def get_max_min(list):
    """
    获取列表的最大值和最小值
    :param list: 需要接收的列表
    :return: 返回一个元组 , 存储的是最大值和最小值
    """
    # 求列表的最大值
    max_value = max(list)
    # 求列表的最小值
    min_value = min(list)
    return max_value, min_value


max_value, min_value = get_max_min([33, 22, 11, 55, 44])
print(f"最大值为:{max_value} ,最小值为:{min_value}")
