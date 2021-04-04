from random import randint

#表示骰子的类
class Die():
    
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        #返回1~6的一个随机值
        return randint(1, self.num_sides)