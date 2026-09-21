"""
1. 函数基础作业
    1-1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
      (1). 分数 >= 90：A
      (2). 分数 >= 75：B
      (3). 分数 >= 60：C
      (4). 分数 < 60：D(
"""


def score_level(num):
    if 90 <= num <= 100:
        return "A"
    elif num >= 75:
        return "B"
    elif num >= 60:
        return "C"
    elif 0 <= num < 60:
        return "D"
    else:
        return "输入不合法"


print(score_level(float(input("请输入分数: "))))

"""
    1-2. 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
         把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
"""


def is_palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False


print(is_palindrome("asdsa"))

"""
    1-3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
"""


def time_conver(s):
    result_hour = s // 3600
    result_minute = (s // 60) % 60
    result_second = s % 60
    return result_hour, result_minute, result_second


all_second = int(input("请输入一个秒数: "))
hour, minute, second = time_conver(all_second)
print(f"输入的秒数: {all_second}, 转换后的小时: {hour} | 转换后的分钟: {minute} | 转换后的秒: {second}")

"""
    1-4. 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
"""


def id_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side2 + side3 > side1:
        if side1 == side2 or side1 == side3 or side2 == side3:
            if side1 == side2 and side1 == side3 and side2 == side3:
                return "等边三角形"
            elif side1 ** 2 + side2 ** 2 == side3 ** 2 or side1 ** 2 + side3 ** 2 == side2 ** 2:
                return "等腰直角三角形"
            else:
                return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"


"""
    1-5. 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
    - 具体规则如下：
      (1). 商品总金额
        - 遍历所有传入的商品元组，将每个商品的 价格 × 数量 累加求和。
      (2). 优惠券扣减
        - 使用条件：商品总金额 ≥ 5000 元才可以使用优惠券。
        - 额度限制：优惠券金额不得超过商品总价（即不得让抵扣后金额为负数）。
        - 不满足条件时，优惠券不生效。
      (3). 积分抵扣
        - 使用条件：商品总金额 ≥ 5000 元才可以使用积分抵扣。
        - 兑换比例：100 积分 = 1 元，积分只能整百抵扣（即实际抵扣金额 = score // 100）。
        - 额度限制：积分抵扣金额不得超过商品总价。
        - 不满足条件时，积分抵扣不生效。
      (4). 运费
        - 直接累加到最终金额上，无任何限制。
"""

# 传递的参数是元组
def result_price(*args, coupon = 0, score = 0, express = 0.0):
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    if coupon + score <= total_cost:
        # 优惠券扣减
        if total_cost >= 5000 and total_cost >= coupon:
            total_cost -= coupon
        # 积分抵扣
        if total_cost >= 5000 and total_cost >= score:
            total_cost -= coupon
        # 4. 添加运费
        total_cost += express
        return total_cost
    return total_cost

# 传递的参数是字典
def calc_order_cost(*args, coupon = 0, score = 0, express = 0.0):
    cart_price = [info["price"] * info["inventory"] for name, info in args]
    total_cart = sum(cart_price)
    if coupon + score <= total_cart:
        # 优惠券扣减
        if total_cart >= 5000 and total_cart >= coupon:
            total_cart -= coupon
        # 积分抵扣
        if total_cart >= 5000 and total_cart >= score:
            total_cart -= coupon
        # 4. 添加运费
        total_cart += express
        return total_cart
    return total_cart

# 测试
# total = result_price(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), coupon=10, score=4000, express=9.9)
# print(toresult_price

# total = result_price(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), coupon=10, score=4000, express=9.9)
# print(toresult_price

# total = result_price(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), express=9.9)
# print(total)

total01 = result_price(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1))
total02 = calc_order_cost(("鼠标", {"price": 188, "inventory": 2}),
                        ("键盘", {"price": 388, "inventory": 1}),
                        ("手机", {"price": 6999, "inventory": 1}))

print(total01)
print(total02)
