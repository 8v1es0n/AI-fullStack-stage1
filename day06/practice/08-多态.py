# from unittest import case
#
#
# class Car:
#     def charge(self):
#         print('正在补充燃料...')
#
#
# class FuelCar(Car):
#     def charge(self):
#         print('燃油汽车正在加油 ...')
#
#
# class ElectricCar(Car):
#     def charge(self):
#         print('电动汽车正在充电...')



class Animal():
    def eat(self):
        print("吃东西 . . .")

class Dog(Animal):
    def eat(self):
        print("吃骨头 . . .")

class Cat(Animal):
    def eat(self):
        print("吃小鱼 . . .")

def use_animals(animal: Animal):
    animal.eat()

if __name__ == '__main__':
    use_animals(Cat())
    use_animals(Dog())