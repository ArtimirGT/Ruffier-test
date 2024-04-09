# напиши здесь код основного приложения и первого экрана
from instr import *
from second_win import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout

class mainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QVBoxLayout()
        self.h_line.setContentsMargins(20, 20, 20, 20)
        self.h_line.addWidget(QLabel(txt_hello), alignment=Qt.AlignLeft)
        self.h_line.addWidget(QLabel(txt_instruction), alignment=Qt.AlignLeft)
        self.next_but = QPushButton(txt_next)
        self.h_line.addWidget(self.next_but, alignment=Qt.AlignCenter)
        self.setLayout(self.h_line)
    def connects(self):
        self.next_but.clicked.connect(self.next)
    def next(self):
        self.hide()
        self.test = testWin()