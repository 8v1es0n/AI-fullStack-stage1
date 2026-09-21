"""
递归 : 函数自己调用自己的过程
思想 : 先层层递进 , 再逐层回归
注意 : 需要有规律找出公式, 必须有出口
"""

# 阶乘函数
def n_factorial(n):
    """
    当前函数的作用是，接收一个数据，返回此数据的阶乘结果
    :param n:接收数据
    :return:返回阶乘结果
    """
    if n == 0:
        return 1

    return n * n_factorial(n - 1)

# 调用阶乘函数
n_factorial(5)