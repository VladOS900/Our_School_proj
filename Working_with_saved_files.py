from Turtle import Turtle
from Calculator import Calculator
from Blueprinter import Blueprinter
from Fileik import Failik
import tkinter
import copy
import os
from PhotoEdit import *
import PIL.ImageOps
from PIL import Image

# -------------------------------------------------------------------------------------------------------
op_dict = {'Черепаха': Turtle(), 'Вычислитель': Calculator(0, 1), 'Чертежник': Blueprinter(),
           'Файлик': Failik(), 'Редактор': PhotoEdit()}
main = tkinter.Tk()
variables = {}


# ---------------------------------------------------------------------------------------------------
class MySyntaxError(SyntaxError):
    pass


# ----------------------------------------------------------------------------------------------------
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
    return no_space_string(res)


def complicated_argument(s):
    s1 = function_argument(s)
    res = []
    i = 0
    while s1[i] != ',':
        i += 1
    try:
        res.append(eval(s1[:i]))
    except Exception:
        res.append(s1[:i])
    i += 1
    try:
        res.append(eval(s1[i:]))
    except Exception:
        res.append(s1[i:])
    return res


def cycle_body(l, i1):
    balance = 0
    cycle_begin = 0
    cycle_end = 0
    l1 = []
    for i in range(i1, len(l) + 1):
        if balance == 0 and cycle_begin != cycle_end:
            l1 = l[(cycle_begin + 1): cycle_end]
            l1.insert(0, cycle_end + 1)
            break
        if 'нц' in l[i]:
            cycle_begin = i
            balance += 1
        if 'кц' in l[i]:
            cycle_end = i
            balance -= 1
    return l1


def norm(a):
    if isinstance(a, int):
        return a
    elif isinstance(a, Calculator):
        a1 = Calculator(a.a, a.b)
        for i in range(1, min(a1.a, a1.b) + 1):
            if a1.a % i == 0 and a1.b % i == 0:
                a1.a //= i
                a1.b //= i
        return a1
    elif isinstance(a, str):
        return a


# --------------------------------------------------------------------------------------------------------


def sign_split(s, sign):
    balance = 0
    f = False
    i1 = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            balance -= 1
        if s[i] == ')':
            balance += 1
        if s[i] in sign and balance == 0:
            i1 = i
            f = True
            break
    if not f:
        return [False, None, None, None]
    else:
        return [True, s[i1], s[:i1], s[i1 + 1:]]


def expression(s):
    l = sign_split(s, '+-')
    if l[0]:
        if l[1] == '+':
            return expression(l[2]) + item(l[3])
        elif l[1] == '-':
            return expression(l[2]) - item(l[3])
    else:
        return item(s)


def item(s):
    l = sign_split(s, '*/')
    if l[0]:
        if l[1] == '/':
            return expression(l[2]) / factor(l[3])
        elif l[1] == '*':
            return expression(l[2]) * factor(l[3])
    else:
        return factor(s)


def factor(s):
    if s[0] == '(':
        return expression(s[1:len(s) - 1])
    elif s[0] == '-':
        return -1 * expression(s[1:])
    else:
        try:
            return variables[s]
        except Exception:
            return int(s)

    # -------------------------------------------------------------------------------------------------------


def xs(x):
    return x + 400


def ys(y):
    return -y + 400


def coords(canvas):
    for i in range(1, 40):
        canvas.create_line(i * 20, 0, i * 20, 800, fill='white')
    for j in range(0, 820, 20):
        canvas.create_line(0, j, 800, j, fill='white')
    canvas.create_line(400, 0, 400, 800, fill='red', width=3)
    canvas.create_line(0, 400, 800, 400, fill='red', width=3)


# -------------------------------------------------------------------------------------------------------
def compiling_txt(file_name):
    global output
    flag = False
    output = open('output.txt', 'wt', encoding='utf-8')
    canvas = tkinter.Canvas(height=800, width=800, bg='blue')
    file = open(file_name, 'rt', encoding='utf-8')
    l = file.readlines()
    for i in range(len(l)):
        if l[i][-1] == '\n':
            l[i] = l[i][:len(l[i]) - 1]
    operator = no_space_string(l[0])
    if operator in op_dict:
        flag = True
    f = False
    if flag:
        op = op_dict[operator]
        for i in range(1, len(l)):
            t = formatted_command(l[i])
            if (t in op.command_list) or ('нц' in t) or ('пока' in t) or ('кц' in t) or ('=' in t) or (
                    'ввод' in t) or ('вывод' in t):
                f = True
            else:
                f = False
                os.chdir('')
                output.write('Синтаксическая ошибка в строке {}: {}\n'.format(i, t))
    else:
        f = False
        output.write('Синтаксическая ошибка в строке 0: некорректный оператор\n')
    if f:
        op = l[0]
        if op == 'Чертежник':
            op = Blueprinter()
        elif op == 'Черепаха':
            op = Turtle()
        elif op == 'Вычислитель':
            op = Calculator(0, 1)
        elif op == 'Файлик':
            op = Failik()
        elif op == 'Редактор':
            op = PhotoEdit()
        core_alg(l[1:], op, canvas)
        if isinstance(op, Turtle) or isinstance(op, Blueprinter):
            canvas.pack()
            main.mainloop()
    print('Программа успешно завершена\n', file=output)
    output.close()


# ________________________________________________________________________________
def core_alg(l, op, canvas):
    global main, variables
    if isinstance(op, Blueprinter):
        coords(canvas)
        crd = op.pos()
        i = 0
        while i < len(l):
            t = formatted_command(l[i])
            if t == 'сместись_в_точку':
                args = complicated_argument(l[i])
                point1 = copy.deepcopy(op.pos())
                op.moveto(args[0], args[1])
                point2 = copy.deepcopy(op.pos())
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]), fill='black',
                                       width=2)
                crd = op.pos()

            elif t == 'сместись_на_вектор':
                args = complicated_argument(l[i])
                point1 = copy.deepcopy(op.pos())
                op.vector_move(args[0], args[1])
                point2 = copy.deepcopy(op.pos())
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]), fill='black',
                                       width=2)
                crd = op.pos()
            elif t == 'подними_перо':
                op.up()
            elif t == 'опусти_перо':
                op.down()
            elif 'нц' in t:
                cycle = cycle_body(l, i)
                for j in range(int(function_argument(l[i]))):
                    core_alg(cycle[1:], op, canvas)
                i = int(cycle[0]) - 1

            i += 1

    elif isinstance(op, Turtle):
        i = 0
        while i < len(l):
            t = formatted_command(l[i])
            if t == 'вперед':
                point1 = copy.deepcopy(op.pos())
                op.forward(function_argument(l[i]))
                point2 = copy.deepcopy(op.pos())
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]))
            elif t == 'назад':
                point1 = copy.deepcopy(op.pos())
                op.backwards(function_argument(l[i]))
                point2 = copy.deepcopy(op.pos())
                if op.f:
                    canvas.create_line(xs(point1[0]), ys(point1[1]), xs(point2[0]), ys(point2[1]))
            elif t == 'вправо':
                op.right(function_argument(l[i]))
            elif t == 'влево':
                op.left(function_argument(l[i]))
            elif t == 'подними_хвост':
                op.up()
            elif t == 'опусти_хвост':
                op.down()
            elif 'нц' in t:
                cycle = cycle_body(l, i)
                for j in range(int(function_argument(l[i]))):
                    core_alg(cycle[1:], op, canvas)
                i = int(cycle[0]) - 2
            i += 1
    elif isinstance(op, Calculator):
        i = 0
        while i < len(l):
            t = formatted_command(l[i])
            l[i] = no_space_string(l[i])
            if t == 'вывод':
                a = function_argument(l[i])
                if a in variables:
                    output.write(str(norm(variables[a])) + "\n")
                else:
                    output.write(str(norm(expression(a))) + "\n")
            elif 'дробь' in t:
                args = complicated_argument(l[i])
                i1 = l[i].index('=')
                k = l[i][:i1]
                if args[0] in variables:
                    args[0] = variables[args[0]]
                if args[1] in variables:
                    args[1] = variables[args[1]]
                variables[k] = Calculator(args[0], args[1])
            elif '=' in t:
                i1 = l[i].index('=')
                l1 = l[i][i1 + 1:]
                t1 = expression(l1)
                variables[l[i][:i1]] = t1
            elif 'нц' in t:
                cycle = cycle_body(l, i)
                for j in range(expression(function_argument(l[i]))):
                    core_alg(cycle[1:], op, canvas)
                i = int(cycle[0]) - 1
            i += 1

    elif isinstance(op, Failik):
        i = 0
        while i < len(l):
            t = formatted_command(l[i])
            l[i] = no_space_string(l[i])
            if 'переименовать' in t:
                names = complicated_argument(l[i])
                print(op.rename(names[0], names[1]), file=output)
            if 'создать_папку' in t:
                name = function_argument(l[i])
                print(op.mkdir(name), file=output)
            if 'создать_файл' in t:
                name = function_argument(l[i])
                print(op.mkfile(name), file=output)
            if 'удалить_папку' in t:
                name = function_argument(l[i])
                print(op.rmdir(name), file=output)
            if 'удалить_файл' in t:
                name = function_argument(l[i])
                print(op.rmfile(name), file=output)
            if 'перейти_в_папку' in t:
                name = function_argument(l[i])
                print(op.cd(name), file=output)
            if 'записать_файл' in t:
                name = complicated_argument(l[i])
                print(op.writefile(name[0], name[1]), file=output)

    elif isinstance(op, PhotoEdit):
        i = 0
        while i < len(l):
            t = formatted_command(l[i])
            if t == 'открыть':
                img_name = function_argument(l[0])
                image = Image.open(img_name)

            elif t == "повернуть":
                angle = int(function_argument(l[i]))
                image = image.rotate(angle)

            elif t == "яркость":
                brightness = float(function_argument(l[i]))
                image1 = Image.new('RGB', image.size)
                for x in range(image.size[0]):
                    for y in range(image.size[1]):
                        r, g, b = image.getpixel((x, y))

                        red = int(r * brightness)
                        red = min(255, max(0, red))

                        green = int(g * brightness)
                        green = min(255, max(0, green))

                        blue = int(b * brightness)
                        blue = min(255, max(0, blue))

                        image1.putpixel((x, y), (red, green, blue))
                image = image1


            elif t == "негатив":
                image = PIL.ImageOps.invert(image)

            elif t == "отразить_верт":
                image = image.transpose(Image.FLIP_LEFT_RIGHT)

            elif t == "отразить_гор":
                image = image.transpose(Image.FLIP_TOP_BOTTOM)

            elif t == "уменьшить":
                w = int(function_argument(l[i]))
                new_w = image.size[0] // w
                image.thumbnail((new_w, new_w), Image.ANTIALIAS)
            i += 1
        image.save('new_' + img_name)
        i += 1
