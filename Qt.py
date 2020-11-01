from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QFontDialog, QLabel, QVBoxLayout
from Working_with_saved_files import *
from PyQt5.QtGui import QPixmap, QMovie
import sys
import os

# Текст и статичные файлы
s = os.path.abspath('')
os.chdir(s)

count = 1
style_textEdit = "background-color: rgb(255, 163, 71); color: rgb(0, 0, 0); border: 7px solid rgb(74, 35, 10)"
style_action = """
QMenu {
    background-color: #ABABAB;   
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
}
QMenu::item:selected { 
    background-color: #654321;
    color: rgb(255,255,255);
}
"""
style_menu = """
QMenuBar {
    background-color: rgb(74, 35, 10)
}
QMenuBar::item {
    spacing: 2px;           
    padding: 2px 5px;
    margin: 2px 5px;
    background-color: rgb(74, 35, 10);
    color: rgb(200,200,200);  
    border-radius: 2px;
}
QMenuBar::item:selected {    
    background-color: rgb(163, 108, 72);
}
QMenuBar::item:pressed {
    background: rgb(163, 108, 72);
}
"""
style_listwidg = """
QListWidget {
  background-color: rgb(255, 163, 71);
  color: rgb(0, 0, 0);
  border: 7px solid rgb(74, 35, 10)
}

QListWidget::item:selected {
  background-color: rgb(163, 108, 72);
}
"""
documentation = open('documentation', 'r', encoding='UTF-8').read()
texts = []
for i in range(0, 6):
    textik = open('text{}'.format(i), 'r', encoding='UTF-8').readlines()
    texts.append(''.join(textik))


# Код
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1060, 910)
        MainWindow.setMaximumSize(1060, 910)
        MainWindow.setMinimumSize(1060, 910)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 98, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(255, 98, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 701, 1061, 151))
        self.textBrowser.setStyleSheet(style_textEdit)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 591, 671))
        self.textEdit.setTabletTracking(False)
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setStyleSheet(style_textEdit)
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.textEdit.setFont(font)
        self.textBrowser.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(650 - 20, 30, 391 + 20, 251 - 13))
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listWidget.setStyleSheet(style_listwidg)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 310, 401, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("panda.jpg"))
        self.label.setObjectName("label")
        self.label.setStyleSheet("border: 5px solid rgb(74, 35, 10)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 27))
        self.menubar.setStyleSheet(style_menu)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setObjectName("menu")
        self.menu.setStyleSheet(style_action)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_2.setObjectName("menu_2")
        self.menu_2.setStyleSheet(style_action)
        self.menu_4 = QtWidgets.QMenu(self.menu_2)
        self.menu_4.setObjectName("menu_4")
        self.menu_4.setStyleSheet(style_action)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_3.setStyleSheet(style_action)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction('Load', MainWindow)
        self.action_2.setCheckable(False)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.opening_file)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.file_save)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setCheckable(False)
        self.action_4.setObjectName("action_4")
        self.action_4.triggered.connect(self.documentWindow)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setCheckable(False)
        self.action_5.setObjectName("action_5")
        self.action_5.triggered.connect(self.start_program)
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_8.triggered.connect(self.font_choice)
        self.actionPandeMode = QtWidgets.QAction(MainWindow)
        self.actionPandeMode.setCheckable(True)
        self.actionPandeMode.setObjectName("actionPandeMode")
        self.actionPandeMode.toggled.connect(self.panda_mode)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menu_4.addAction(self.action_8)
        self.menu_2.addAction(self.actionPandeMode)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PandaScript"))
        self.textBrowser.setHtml(_translate("MainWindow", "<span>Output will be here</span>"))
        self.textEdit.setHtml(_translate("MainWindow", "<span>Code will be here</span>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Вступление"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Примеры Кода"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Документация: Черепаха"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Документация: Чертежник"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Документация: Вычислитель"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Документация: Файлик"))
        self.listWidget.itemClicked.connect(self.openWindow)
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Документация: Картиночка"))
        self.listWidget.itemClicked.connect(self.openWindow)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("MainWindow", "Файлы"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_4.setTitle(_translate("MainWindow", "Шрифт"))
        self.menu_3.setTitle(_translate("MainWindow", "Запустить программу"))
        self.action_2.setText(_translate("MainWindow", "Открыть..."))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
        self.action_4.setText(_translate("MainWindow", "Документация"))
        self.action_5.setText(_translate("MainWindow", "Запустить"))
        self.action_8.setText(_translate("MainWindow", "Тип"))
        self.actionPandeMode.setText(_translate("MainWindow", "PandаMode"))

    def openWindow(self, item):
        self.widget = QtWidgets.QWidget()
        row = self.listWidget.row(item)
        self.widget.setWindowTitle(f'{item.text()}')
        self.widget.setGeometry(500, 100, 600, 800)
        self.widget.setStyleSheet("background-color:white;")

        self.lbl = QtWidgets.QTextBrowser()
        self.lbl.setFontPointSize(20)
        self.lbl.setGeometry(500, 100, 600, 800)
        self.lbl.setText(texts[row])

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.widget.setLayout(self.vbox)
        self.widget.show()

    def documentWindow(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setWindowTitle('Документация')
        self.widget.setGeometry(500, 100, 600, 800)
        self.widget.setStyleSheet("background-color:white;")
        self.lbl = QtWidgets.QTextBrowser()
        self.lbl.setFontPointSize(20)
        self.lbl.setGeometry(500, 100, 600, 800)
        self.lbl.setText(documentation)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.widget.setLayout(self.vbox)
        self.widget.show()

    def file_save(self):
        try:
            name = QFileDialog.getSaveFileName(self, 'Save File')
            file = open(name[0], 'w', encoding='UTF-8')
            text = self.textEdit.toPlainText()
            try:
                text = text.replace('Code will be here\n', '')
            except:
                pass
            file.write(text)
            file.close()
        except:
            pass

    def start_program(self):
        os.chdir(s)
        file = open('programm', 'w', encoding='UTF-8')
        text = self.textEdit.toPlainText()
        try:
            text = text.replace('Code will be here\n', '')
        except:
            pass
        file.write(text)
        file.close()
        try:
            compiling_txt('programm')
        except:
            pass
        os.chdir(s)
        file2 = open('output.txt', 'r', encoding='UTF-8')
        text2 = file2.read()
        self.textBrowser.setText(text2)
        file2.close()
        os.remove('programm')
        os.remove('output.txt')

    def opening_file(self):
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(name[0], 'r', encoding='UTF-8')
            with file:
                try:
                    text = file.read()
                    self.textEdit.setText(text)
                except:
                    self.textEdit.setText("Ага! баловаться решил и всякую бяку открывать вместо кода?) Не получится")
        except:
            pass

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            font.setPointSize(20)
            font.setBold(True)
            self.textEdit.setFont(font)
            self.textBrowser.setFont(font)

    def panda_mode(self):
        global count
        count += 1
        if count % 2 == 0:
            self.gif = QMovie('resized.gif')
            self.label.setMovie(self.gif)
            self.gif.start()
        else:
            self.label.setPixmap(QtGui.QPixmap("panda.jpg"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
