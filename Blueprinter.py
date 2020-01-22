class Blueprinter:
    def __init__(self):
        self.command_list = ['сместись', 'сместись_на_вектор', 'подними_перо', 'опусти_перо']
        self.pos = [0, 0]
        self.f = True

    def moveto(self, x, y):
        self.pos = [x, y]

    def vector_move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def up(self):
        self.f = False

    def down(self):
        self.f = True
