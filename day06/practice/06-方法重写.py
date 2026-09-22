class Car:
    def __init__(self, c_color, c_brand, c_name):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name

    def start(self):  # 启动
        print(f'{self.brand} {self.name} 正在启动...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.name} 停止行驶...')

    def charge(self):
        print(f'{self.brand} {self.name} 正在补充燃料...')


# 子类
class FuelCar(Car):  # 油车类

    # 什么时候需要方法重写:当父类的方法满足不了子类，子类需要把方法重写
    def charge(self):
        # 调用父类中的方法
        Car.charge(self)
        print(f"{self.brand} {self.name} 正在加油 . . .")


if __name__ == '__main__':
    # 创建子类对象
    car = FuelCar("白色", "特斯拉", "model X")
    # 使用子类对象调用方法，先找子类是否存在，如果子类不存在找父类
    car.charge()
