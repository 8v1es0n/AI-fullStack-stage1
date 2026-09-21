# 可变参数   : 位置参数可变参数, 可以传递0到任一个数据
# *args , 类型属于元组类型 , 传递时需要传递的是0-任意的数据值

# 可变参数 : 关键字参数可变参数, 可以传递0到任一个数据
# **kwargs : 类型属于字典类型 , 传递时需要传递的是0-任意的键值对数据

def calc_number(*args, **kwargs):
    # 求最大值
    max_value = max(args)
    # 求最小值
    min_value = min(args)
    # 求数据和
    sum_value = sum(args)

    if kwargs.get("flag"):  # None , 0 , "" , 数据容器中没有数据 --> False
        # if kwargs["flag"]: # 报错
        # 需要把平均值返回
        return max_value, min_value, round(sum_value / len(args), kwargs["count"])
    else:
        # 不需要返回平均值
        return max_value, min_value

    # 返回值是多个数据 , 以元组返回
    # return max_value, min_value, sum_value / len(args)
    # 返回列表
    # return [max_value , min_value , sum_value / len(args)]
    # 返回集合
    # return {max_value, min_value, sum_value / len(args)}


# flag的值为True表示返回平均值 , 否则不返回平均值   count表示的是保留小数的位数
print(calc_number(37, 22, 11, 57, 49, 77, 88, count=3, flag=True))
# print(calc_number(37, 22, 11, 57, 49, 77, 88))

# # number = calc_number(1, 2, 3, 4, 5)
# # print(type(number), number)
#
# # 可变参数 : 关键字参数可变参数, 可以传递0到任一个数据
# # **kwargs : 类型属于字典类型 , 传递时需要传递的是0到任一个键值对数据
# def calc_number2(**kwargs):
#     print(type(kwargs) , kwargs)
#
# calc_number2(name = "张三" , age = 23)
