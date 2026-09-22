class Car:
    # 类属性 (所有实例对象共享的)
    wheel = 4  # 轮胎数量
    tax_rate = 0.1  # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_owner):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.__owner = c_owner  # 拥有者

    def start(self):  # 启动
        print(self.__owner)
        print(f'{self.brand} {self.name} 正在启动...')
        self.__control_fuel()

    def stop(self):  # 停止
        print(f'{self.brand} {self.name} 停止行驶...')

    # 控制燃油分配
    # 私有方法只能在本类方法中使用, 外界无法访问
    def __control_fuel(self):
        print(f'{self.brand} {self.name} 控制燃油分配...')


if __name__ == '__main__':
    car = Car("白色", "夏利", "小优", "王刚")
    car.start()