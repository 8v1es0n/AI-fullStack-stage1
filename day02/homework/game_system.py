"""
7. 简单游戏指令系统开发
- 请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作(输出控制台)。
- 具体规则：
+-----------------------+-------------------------+
|        玩家输入       |        对应动作          |
+-----------------------+-------------------------+
| 上 / w / W            |      角色向上移动        |
| 下 / s / S            |      角色向下移动        |
| 左 / a / A            |      角色向左移动        |
| 右 / d / D            |      角色向右移动        |
| 跳 / " "(空格)        |        角色跳跃          |
| 攻击 / j / J          |      角色发动攻击        |
| 退出 / esc / ESC      |      角色退出游戏        |
+-----------------------+-------------------------+
"""
# 定义英雄坐标x, y
hero_x = 80
hero_y = 14

# 定义人物和炸弹标识
hero = "^"
boom = "※"

# 定义射线状态及终点坐标
ray_status = 0
ray_end_x = 1
ray_end_y = 1

# 随机生成炸弹坐标
import random
boom_x = random.randint(1, 160)
boom_y = random.randint(1, 26)

# 游戏循环进行入口
while True:
    # 与炸弹位置重合，游戏结束
    if hero_x == boom_x and hero_y == boom_y:
        print("---------- 英雄死亡，游戏结束 ----------")
        break

    # 绘制地图
    for fence_wide in range(27):   # 控制行
        if fence_wide == 0:
            print("---------------------------------------------------------------------------------", end="")
            print("---------------------------------------------------------------------------------")
        elif 0 < fence_wide < 26:
            for fence_length in range(162):  # 控制列
                if (0 < hero_x < 160) and (0 < hero_y < 26):
                    if fence_length == 0:
                        print("|", end="")
                    elif fence_length == 161:
                        print("|", end="\n")
                    elif fence_length == hero_x and fence_wide == hero_y:
                        print(hero, end="")
                    elif fence_length == boom_x and fence_wide == boom_y:
                        print(boom, end="")
                    elif ray_status == 0:
                        print(" ", end="")
                    elif (hero_x < fence_length < ray_end_x or hero_x > fence_length > ray_end_x) and fence_wide == hero_y:
                        print("-", end="")
                    elif (hero_y < fence_wide < ray_end_y or hero_y > fence_wide > ray_end_y) and fence_length == hero_x:
                        print("|", end="")
                    else:
                        print(" ", end="")
                else:
                    print("---------- 超出边界，游戏结束 ----------")
                    break

        else:
            print("---------------------------------------------------------------------------------", end="")
            print("---------------------------------------------------------------------------------")

    # 射线击中炸弹，游戏结束
    if (ray_end_x != 1 and ray_end_x != 160) or (ray_end_y != 1 and ray_end_y != 29):
        print("---------- 击中炸弹，游戏结束 ----------")
        break
    # 关闭射线
    ray_status = 0
    operations = input("请输入您的操作： ")

    # 定义操作变量
    o_w = 0
    o_a = 0
    o_s = 0
    o_d = 0

    # 判断是否退出
    if operations == "ESC" or operations == "esc":
        break

    # 空格实现随机传送
    if operations == " ":
        boom_x = random.randint(1, 160)
        boom_y = random.randint(1, 26)
        continue

    # 进行攻击
    if operations == "j" or operations == "J":
        match hero:
            # 朝向为右
            case ">":
                # 根据英雄和炸弹的坐标关系判断射线终点坐标
                if boom_y == hero_y and boom_x > hero_x:
                    ray_end_x = boom_x - 1
                    ray_end_y = hero_y
                else:
                    ray_end_x = 160
                    ray_end_y = hero_y

            # 朝向为左
            case "<":
                # 根据英雄和炸弹的坐标关系判断射线终点坐标
                if boom_y == hero_y and boom_x < hero_x:
                    ray_end_x = boom_x + 1
                    ray_end_y = hero_y
                else:
                    ray_end_x = 1
                    ray_end_y = hero_y

            # 朝向为下
            case "v":
                # 根据英雄和炸弹的坐标关系判断射线终点坐标
                if boom_x == hero_x and boom_y > hero_y:
                    ray_end_y = boom_x - 1
                    ray_end_x = hero_x
                else:
                    ray_end_y = 26
                    ray_end_x = hero_x

            # 朝向为上
            case "^":
                # 根据英雄和炸弹的坐标关系判断射线终点坐标
                if boom_x == hero_x and boom_y < hero_y:
                    ray_end_y = boom_x + 1
                    ray_end_x = hero_x
                else:
                    ray_end_y = 1
                    ray_end_x = hero_x
        # 射线开启
        ray_status = 1


    # 循环遍历输入的操作
    for operation in operations:
        if operation == "w" or operation == "W":
            o_w += 1
        if operation == "a" or operation == "A":
            o_a += 1
        if operation == "s" or operation == "S":
            o_s += 1
        if operation == "d" or operation == "D":
            o_d += 1

    # 更新英雄坐标
    hero_x += o_d - o_a
    hero_y += o_s - o_w

    # 确定英雄朝向
    if o_d - o_a > 0:
        hero = ">"
    elif o_d - o_a < 0:
        hero = "<"
    elif o_d - o_a == 0 and o_s - o_w > 0:
        hero = "v"
    else:
        hero = "^"