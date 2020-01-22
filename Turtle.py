from math import pi, sin, cos


class Turtle:
    def __init__(self):
        self.alpha = pi / 2
        self.pos = [0, 0]
        self.f = True
        self.command_list = ['вперед', 'назад', 'вправо', 'влево', 'опусти_хвост', 'подними_хвост']

    def right(self, beta):
        self.alpha -= beta * pi / 180

    def left(self, beta):
        self.alpha += beta * pi / 180

    def forward(self, a):
        self.pos = [self.pos[0] + a * cos(self.alpha), self.pos[1] + a * sin(self.alpha)]

    def backwards(self, a):
        self.pos = [self.pos[0] - a * cos(self.alpha), self.pos[1] - a * sin(self.alpha)]

    def up(self):
        self.f = False

    def down(self):
        self.f = True
