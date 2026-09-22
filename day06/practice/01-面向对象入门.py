"""
    类的定义
    class 类名:
       def __init__(self , 参数列表):
            self.属性名 = 属性值
            self.属性名 = 属性值
            ....
"""
class Car:
    # 构造方法
    def __init__(self, brand, color, price):
        print("Hello")
        self.c_brand = brand
        self.c_color = color
        self.c_price = price

    # 实例方法
    def running(self, name):
        print(f"{name} 正在开着 {self.c_brand}, {self.c_color}, {self.c_price} 的车飞速行驶")

    def stop(self, name):
        print(f"{name} 把 {self.c_brand}, {self.c_color}, {self.c_price} 的车停进车库")


if __name__ == '__main__':

    c_1 = Car("宝马", "red", 100)
    print(c_1.c_brand, c_1.c_color, c_1.c_price)

    print(c_1.__dict__)
    c_1.running("刘亦菲")
    c_1.stop("张伟")