"""
    1. 完成如下条件判断的需求
    - 需求1：根据用户输入的数字，判断该数字是奇数还是偶数。
    - 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）。
    - 需求3：根据用户输入的数字，判断该数字是正数还是负数还是0 。
    - 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了, 否则就是不及格）。
"""
# 1 ~ 3 实现
number01 = int(input("请输入一个数字: "))
if number01 % 2 != 0:
    print("这个数是奇数")
else:
    print("这个数是偶数")
if number01 > 0:
    print("这个数是正数")
elif number01 < 0:
    print("这个数是负数")
else:
    print("这个数是 0 ")

# 5. 判断分数是否及格
score = int(input("请输入考试分数: "))
if score >= 60:
    print("成绩合格")
else:
    print("成绩不合格")

"""
    1. 根据输入的考试成绩，判断成绩等级。
      1. 大于等于85分为优秀
      2. 60-85分为及格
      3. 否则就是不及格
  """
exam_score = int(input("请输入期末考试分数: "))
if exam_score >= 85:
    print("成绩评定为: 优秀")
elif exam_score >= 60:
    print("成绩评定为: 及格")
else:
    print("成绩评定为: 不及格")

"""
    3. 接收用户输入百分制分数（整数），按照规则判定等级并输出：
      1. 90 ~ 100：优秀
      2. 80 ~ 89：良好
      3. 70 ~ 79：中等
      4. 60 ~ 69：及格
      5. 0 ~ 59：不及格
      6. 分数小于 0 或 大于 100：输出「分数输入有误」
"""
final_score = int(input("请输入最终考试分数: "))
if final_score < 100 or final_score > 0:
    if final_score >= 90:
        print("成绩评定为: 优秀")
    elif final_score >= 80:
        print("成绩评定为: 良好")
    elif final_score >= 70:
        print("成绩评定为: 中等")
    elif final_score >= 60:
        print("成绩评定为: 及格")
    else:
        print("成绩评定为: 不及格")
else:
    print("分数输入有误~")

"""
    4. 购物折扣计算
      根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
      - 金额 >= 500: 8折
      - 300 <= 金额 < 500: 9折  
      - 100 <= 金额 < 300: 95折
      - 金额 < 100: 无折扣
"""
total_price = float(input("请输入购物总额: "))
if total_price >= 500:
    print(f"需要支付的金额: {total_price * 0.8}")
elif total_price >= 300:
    print(f"需要支付的金额: {total_price * 0.9}")
elif total_price >= 100:
    print(f"需要支付的金额: {total_price * 0.95}")
else:
    print(f"需要支付的金额: {total_price}")

"""
    5. 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
      北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，
      用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
      阶梯电价规则：
        第一档：2880度以下，电费单价元/度
        第二档：2880-4800度，电费单价0.5383元/度
        第三档：4800度以上，电费单价0.7883元/度
"""
battery_level = float(input("请输入用电量: "))
battery_price = 0.0
if battery_level >= 2880:
    if battery_level >= 4800:
        print(f"{battery_price} = {(battery_level - 4800) * 0.7883 + 1406.304 + 1033.536}")
    # 电量小于4800
    else:print(f"{battery_price} = {(battery_level - 2880) * 0.5383 + 1406.304}")
# 电量小于2880
else:
    print(f"{battery_price} = {battery_level * 0.4883}")


"""
    6. 接收用户输入的月份（1-12），判断该月份所属的季节
      - 春季：3、4、5
      - 夏季：6、7、8
      - 秋季：9、10、11
      - 冬季：12、1、2
"""
month = int(input("请输入月份: "))
match month:
    case 3 | 4 | 5:
        print(f"{month}为: 春季")
    case 6 | 7 | 8:
        print(f"{month}为: 夏季")
    case 9 | 10 | 11:
        print(f"{month}为: 秋季")
    case 12 | 1 | 2:
        print(f"{month}为: 冬季")
    case _:
        print("输入有误")