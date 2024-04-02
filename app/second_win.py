# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

app = QApplication([])

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(QLabel(txt_name), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintname), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_age), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintage), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QPushButton(txt_starttest1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QPushButton(txt_starttest2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QPushButton(txt_starttest3), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest3), alignment=Qt.AlignLeft)
        self.r_line.addWidget(QLabel('<b>ЗДЕСЬ БУДЕТ ТАЙМЕР<b>'), alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        pass

test = TestWin()
app.exec_()