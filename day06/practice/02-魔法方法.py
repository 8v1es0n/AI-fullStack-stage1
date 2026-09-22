class Car:
    # 构造方法
    def __init__(self, brand, color, price):
        print("Hello")
        self.c_brand = brand
        self.c_color = color
        self.c_price = price

    # 打印对象时, 根据返回的代码打印信息, 兼容字符串和容器
    def __repr__(self):
        return f"{self.c_brand} {self.c_color} {self.c_price}"

    # 当使用 == 时, 对比两个对象, 此魔法方法执行
    def __eq__(self, other):
        return self.c_brand == other.c_brand and self.c_color == other.c_color and self.c_price == other.c_price

    # 比较对象大小时, 不带 = 用 lt 不用考虑 > 或 <
    def __lt__(self, other):
        return self.c_price < other.c_price

    # 比较对象大小时, 带 = 用 le 不用考虑 >= 或 <=
    def __le__(self, other):
        return self.c_price <= other.c_price

c_1 = Car("宝马", "red", 100)
c_2 = Car("宝莱", "red", 50)

car_list = [c_1, c_2]
print(car_list)

print(c_1 == c_2)
print(c_1 >= c_2)
print(c_1 < c_2)