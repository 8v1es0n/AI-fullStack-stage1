"""
多继承: 一个子类继承了多个父类
"""


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

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料...')


# 华为智驾
class HuaweiAiDriving:
    """华为AI智能驾驶"""

    def __init__(self, version="V1.0"):
        self.version = version

    def run(self):
        print(f'使用华为AI智能驾驶系统{self.version}正在行驶...')


# 问界汽车 --> 演示多继承
# 注意:当一个类继承了多个父类时，默认优先使用第一个父类中的同名属性或方法，可以使用类名.__mro__属性或类名.mro()方法查看调用顺序
class WenJieCar(Car, HuaweiAiDriving):
    def __init__(self, brand, model, color, owner, version):
        Car.__init__(self, brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

    def __repr__(self):
        return f"{self.brand} {self.model} {self.__owner} {self.version}"

    def run(self):
        HuaweiAiDriving.run(self)


# MRO: Method Resolution Order --> 方法解析顺序
if __name__ == '__main__':
    car = WenJieCar("问界", "M9", "金色", "杨幂", "2.0")

    print(car)
    car.run()

    print(WenJieCar.mro())
