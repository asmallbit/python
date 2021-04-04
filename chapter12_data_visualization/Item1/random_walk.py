from random import choice

#生成随机漫步数据的类
class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points
        #所有随机漫步都起始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        #不断漫步,知道列表到达指定的长度
        while len(self.x_values)<self.num_points:

            #决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            #拒绝原地漫步
            if x_step==0 and y_step==0:
                continue
            
            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            #记录漫步后的值
            self.x_values.append(next_x)
            self.y_values.append(next_y)


