# 鸭子类型 - 多态体现
class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Duck:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Pig:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')
