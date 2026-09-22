class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand  # 品牌(公有属性)
        self.model = model  # 型号(公有属性)
        self.color = color  # 颜色(公有属性)
        self.__owner = owner  # 拥有者(私有属性)

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.__owner} : {self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')


# 燃油车
class FuelCar(Car):
   pass


if __name__ == '__main__':
    car = FuelCar("特斯拉" , "model3" ,"蓝色" , "张三" )
    print(car.brand)
    car.start()

    # 父类的所有成员(属性和方法)都可以继承 , 但是无法使用
    # print(car.__owner)
