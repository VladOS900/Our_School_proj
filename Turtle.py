from math import pi, sin, cos


class Turtle:
    def __init__(self):
        self.alpha = pi / 2
        self.pos_ = [0, 0]
        self.f = True
        self.command_list = ['вперед', 'назад', 'вправо', 'влево', 'опусти_хвост', 'подними_хвост']

    def right(self, beta):
        beta = float(beta)
        self.alpha -= beta * pi / 180

    def left(self, beta):
        beta = float(beta)
        self.alpha += beta * pi / 180

    def forward(self, a):
        a = float(a)
        self.pos_ = [self.pos_[0] + a * cos(self.alpha), self.pos_[1] + a * sin(self.alpha)]

    def backwards(self, a):
        a = float(a)
        self.pos_ = [self.pos_[0] - a * cos(self.alpha), self.pos_[1] - a * sin(self.alpha)]

    def up(self):
        self.f = False

    def down(self):
        self.f = True

    def f(self):
        return self.f

    def pos(self):
        return self.pos_
