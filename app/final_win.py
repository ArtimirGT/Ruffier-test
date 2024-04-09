# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

class finalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.r_index = '0'
        self.age = 0
        self.set_appear()
        self.initUI()
        self.show()
    def get_index(self, r_index, age):
        self.r_index = r_index
        self.age = age
        self.index_text.setText(txt_index + self.r_index)
        self.result_text.setText(txt_workheart + get_result(float(self.r_index), get_offset(int(self.age))))
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.index_text = QLabel(txt_index + self.r_index)
        self.main_layout.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.result_text = QLabel(txt_workheart + get_result(float(self.r_index), get_offset(int(self.age))))
        self.main_layout.addWidget(self.result_text, alignment= Qt.AlignCenter)
        self.setLayout(self.main_layout)
    