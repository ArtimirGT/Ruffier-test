from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *

app = QApplication([])

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apeer()
        self.initUI()
        self.connects()
        self.show()
    
    def set_apeer(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(QLabel(txt_hello), alignment = Qt.AlignLeft)
        self.v_line.addWidget(QLabel(txt_instruction), alignment = Qt.AlignLeft)
        self.v_line.addWidget(QPushButton(txt_next), alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)

    def connects(self):
        pass


test = MainWin()
app.exec_()