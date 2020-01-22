class Robot:
    def __init__(self):
        self.command_list = ['справа_свободно', 'слева_свободно', 'сверху_свободно', 'снизу_свободно', 'вправо',
                             'вверх', 'вниз', 'влево',
                             'закрась', 'закрашено', 'очисть']
        self.field = []
        for i in range(0, 13):
            if i == 0 or i == 12:
                self.field.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
            else:
                self.field.append([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1])
        self.pos = [5, 5]
        self.field[self.pos[0], self.pos[1]] = 1

    def right_vacant(self):
        return self.pos[0] + 1 != -1

    def left_vacant(self):
        return self.pos[0] - 1 != -1

    def up_vacant(self):
        return self.pos[1] - 1 != -1

    def down_vacant(self):
        return self.pos[1] + 1 != -1

    def move_up(self):
        self.pos[1] -= 1

    def move_down(self):
        self.pos[1] += 1

    def move_right(self):
        self.pos[0] += 1

    def move_left(self):
        self.pos[0] -= 1

    def paint(self):
        self.field[self.pos[0], self.pos[1]] = 2

    def clean(self):
        self.field[self.pos[0], self.pos[1]] = 0

    def is_painted(self):
        return self.field[self.pos[0], self.pos[1]] == 2


