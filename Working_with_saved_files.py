from Robot import Robot
from Turtle import Turtle
from Calculator import Calculator
from Blueprinter import Blueprinter

op_dict = {'Робот': Robot(), 'Черепаха': Turtle(), 'Вычислитель': Calculator(), 'Чертежник': Blueprinter()}


class MySyntaxError(SyntaxError):
    pass


def formatted_command(s):
    i = 0
    res = ''
    while s[i] != '(':
        res += s[i]
    return res


def function_argument(s):
    i = 0
    while s[i] != '(':
        i += 1

    i += 1
    i1 = i
    while s[i] != ')':
        i += 1
    i2 = i
    res = eval(s[i1:i2 + 1])
    return res


def compiling_txt(file_name):
    file = open(file_name, 'rt', encoding='utf-8')
    l = file.readlines()
    operator = l[0]
    for i in range(1, len(l)):
        if formatted_command(l[i]) in op_dict[operator].command_list:
            pass
        else:
            raise MySyntaxError('')
