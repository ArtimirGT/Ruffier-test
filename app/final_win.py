# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

class finalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(QLabel(txt_index), alignment= Qt.AlignCenter)
        self.main_layout.addWidget(QLabel(txt_title), alignment= Qt.AlignCenter)
        self.setLayout(self.main_layout)
    