import random

"""
- 需求：猜数字小游戏
  1. 系统随机生成一个随机数
  2. 用户根据提示猜数字，并将所猜的数字输入系统
  3. 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
  4. 如果猜对，系统自动退出，游戏结束
"""

#  1. 生成一个随机数
random_number = random.randint(1, 100)

#  2. 用户输入一个数字
print("输入要求: 1 ~ 100 之间的整数")
start = 1
end = 100

# 循环
while True:
    user_number = int(input("请输入: "))

    # 判断数字大小
    if user_number > random_number:
        print(f"您输入的数字: {user_number} 大了")
        end = user_number
        print(f"当前的可选范围: {start} ~ {end - 1}")
    elif user_number < random_number:
        print(f"您输入的数字: {user_number} 小了")
        start = user_number
        print(f"当前的可选范围: {start + 1} ~ {end}")
    else:
        print("您中奖了! 您中大奖了!!!")
        break
