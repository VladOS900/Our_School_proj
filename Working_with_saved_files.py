from Robot import Robot
from Turtle import Turtle
from Calculator import Calculator
from Blueprinter import Blueprinter
import tkinter
import copy

# -------------------------------------------------------------------------------------------------------
op_dict = {'Робот': Robot(), 'Черепаха': Turtle(), 'Вычислитель': Calculator(), 'Чертежник': Blueprinter()}
main = tkinter.Tk()
canvas = tkinter.Canvas(height=800, width=800, bg='#006400')


# ---------------------------------------------------------------------------------------------------
class MySyntaxError(SyntaxError):
    pass


def no_space_string(s):
    s1 = ''
    for i in range(len(s)):
        if s[i] != ' ':
            s1 += s[i]
    return s1


def formatted_command(s):
    i = 0
    res = ''
    if '(' in s:
        while s[i] != '(':
            res += s[i]
            i += 1
        return no_space_string(res)
    else:
        return no_space_string(s)


def function_argument(s):
    i = 0
    while s[i] != '(':
        i += 1
    i += 1
    i1 = i
    while s[i] != ')':
        i += 1
    i -= 1
    i2 = i
    res = s[i1:i2 + 1]
    return res


def complicated_argument(s):
    s1 = function_argument(s)
    res = []
    i = 0
    while s1[i] != ',':
        i += 1
    res.append(eval(s1[:i]))
    i += 1
    res.append(eval(s1[i:]))
    return res


# -------------------------------------------------------------------------------------------------------
def xs(x):
    return x + 400


def ys(y):
    return -y + 400


def coords():
    global canvas
    for i in range(1, 40):
        canvas.create_line(i * 20, 0, i * 20, 800, fill='black')
    for j in range(0, 820, 20):
        canvas.create_line(0, j, 800, j)
    canvas.create_line(400, 0, 400, 800, fill='purple')
    canvas.create_line(0, 400, 800, 400, fill='purple')


# -------------------------------------------------------------------------------------------------------
def compiling_txt(file_name):
    file = open(file_name, 'rt', encoding='utf-8')
    l = file.readlines()
    for i in range(len(l)):
        if l[i][-1] == '\n':
            l[i] = l[i][:len(l[i]) - 1]
    operator = l[0]
    f = False
    for i in range(1, len(l)):
        if formatted_command(l[i]) in op_dict[operator].command_list:
            f = True
        else:
            f = False
            raise MySyntaxError('Синтаксическая ошибка')
    if f:
        core_alg(l)


def core_alg(l):
    global canvas, main
    operator = l[0]
    if operator == 'Чертежник':
        op = Blueprinter()
        coords()
        crd = op.pos
        pos = canvas.create_oval(xs(crd[0] - 2), ys(crd[1] - 2), xs(crd[0] + 2), ys(crd[1] + 2), fill='red')
        for i in range(len(l)):
            if formatted_command(l[i]) == 'сместись_в_точку':
                args = complicated_argument(l[i])
                point1 = copy.deepcopy(op.pos)
                op.moveto(args[0], args[1])
                point2 = copy.deepcopy(op.pos)
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]), fill='blue')
                canvas.delete(pos)
                crd = op.pos
                pos = canvas.create_oval(xs(crd[0] - 2), ys(crd[1] - 2), xs(crd[0] + 2), ys(crd[1] + 2), fill='red')

            elif formatted_command(l[i]) == 'сместись_на_вектор':
                args = complicated_argument(l[i])
                point1 = copy.deepcopy(op.pos)
                op.vector_move(args[0], args[1])
                point2 = copy.deepcopy(op.pos)
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]), fill='blue')
                canvas.delete(pos)
                crd = op.pos
                pos = canvas.create_oval(xs(crd[0] - 2), ys(crd[1] - 2), xs(crd[0] + 2), ys(crd[1] + 2), fill='red')
            elif formatted_command(l[i]) == 'подними_перо':
                op.up()
            elif formatted_command(l[i]) == 'опусти_перо':
                op.down()


    elif operator == 'Черепаха':
        pass
    elif operator == 'Вычислитель':
        pass
    elif operator == 'Робот':
        pass


compiling_txt('sample_file.txt')
canvas.pack()
main.mainloop()
