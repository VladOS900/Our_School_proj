import os
import getpass
from pathlib import Path
import shutil


class FileError(BaseException):
    pass


class NameError(BaseException):
    pass


class Failik:
    def __init__(self):
        self.command_list = ['переименовать', 'создать_папку', 'создать_файл', 'удалить_папку', 'удалить_файл',
                             'перейти_в_папку', 'записать_файл']
        self.user_name = getpass.getuser()
        s = os.getcwd()
        os.chdir(s)

    #        if os.name == 'posix':
    #            homedir = os.path.expanduser("~")
    #            os.chdir('{}/Desktop'.format((homedir)))
    #        elif os.name == 'nt':
    #            homedir = os.path.expanduser("~")
    #            try:
    #                os.chdir(homedir + '\\Рабочий стол')
    #            except:
    #                try:
    #                    os.chdir(homedir + '\\Desktop')
    #                except:
    #                   pass

    #                    os.chdir('C:\\Users\\vlgan\\PS Codes')
    #                    print('Не удалось найти рабочий стол, результат сохранен в папку: C:\\Users\\vlgan\\PS Codes')

    def rename(self, old_name, new_name):
        try:
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                return 'Папка {} переименована в {}'.format(old_name, new_name)
            elif os.path.exists(new_name):
                raise NameError
            else:
                raise FileError
        except FileError:
            return 'Такой папки или файла не существует'
        except NameError:
            return 'Папка с именем {} уже существует'.format(new_name)

    def mkdir(self, name):
        try:
            if os.path.isdir(name):
                raise FileError
            else:
                os.mkdir(name)
                return 'Папка с именем {} создана'.format(name)
        except FileError:
            return 'Такая папка уже существует, создайте ее под другим именем'

    def cd(self, name):
        try:
            full_name = str(Path(name).resolve())
            if os.path.isdir(full_name):
                os.chdir(full_name)
                return 'Вы перешли в папку с именем {}'.format(name)
            else:
                raise FileError
        except FileError:
            return "Такой папки не существует, в которую вы хотите перейти"

    def mkfile(self, name):
        try:
            if os.path.isfile(name):
                raise FileError
            else:
                file = open(name, 'w')
                file.close()
                return 'Файл с именем {} создан'.format(name)
        except FileError:
            return 'Такой файл уже существует, создайте под другим именем'

    def writefile(self, name, text):
        try:
            if not os.path.isfile(name):
                raise FileError
            else:
                file = open(name, 'wt', encoding='utf-8')
                file.write(text)
                file.close()
                return 'Файл c именем {} изменен'.format(name)
        except FileError:
            return 'Такого файла не существует, попробуйте создать его, прежде чем записывать'

    def rmfile(self, name):
        try:
            if os.path.isfile(name):
                os.remove(name)
                return 'Файл с именем {} удален'.format(name)
            elif os.path.isdir(name):
                raise NameError
            else:
                raise FileError
        except FileError:
            return 'Такого файла не существует'
        except NameError:
            return 'Это не файл, а папка, удаляйте его с помощью команды УДАЛИ_ПАПКУ'

    def rmdir(self, name):
        try:
            if os.path.isdir(name):
                shutil.rmtree(name)
                return 'Папка с именем {} удалена'.format(name)
            elif os.path.isfile(name):
                raise NameError
            else:
                raise FileError
        except FileError:
            return 'Такой папки не существует'
        except NameError:
            return 'Это не папка, а файл, удаляйте его с помощью команды УДАЛИ_ФАЙЛ'
