# напиши здесь код для второго экрана приложения
from final_win import *
from instr import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

app = QApplication([])

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def timer_event(self):
        self.time = self.time.addSecs(1)
        if self.time.toString("hh:mm:ss") == f'00:00:{self.endtime}':
            self.timer.stop()
            self.time = QTime(0, 0, 0)
        self.timer_text.setText(self.time.toString("<b>hh:mm:ss<b>"))

    def test1_start(self):
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.endtime = '15'
    def test2_start(self):
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.endtime = '45'
    def test3_start(self):
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.endtime = '15'

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.timer_event)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(QLabel(txt_name), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintname), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_age), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintage), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.test1_but = QPushButton(txt_starttest1)
        self.l_line.addWidget(self.test1_but, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.test2_but = QPushButton(txt_starttest2)
        self.l_line.addWidget(self.test2_but, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.test3_but = QPushButton(txt_starttest3)
        self.l_line.addWidget(self.test3_but, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hinttest3), alignment=Qt.AlignLeft)
        self.but_sendresults = QPushButton(txt_sendresults)
        self.l_line.addWidget(self.but_sendresults, alignment=Qt.AlignCenter)
        self.timer_text = QLabel('<b>00:00:00<b>')
        self.timer_text.setFont(QtGui.QFont('Times', 30))
        self.r_line.addWidget(self.timer_text, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.test1_but.clicked.connect(self.test1_start)
        self.test2_but.clicked.connect(self.test2_start)
        self.test3_but.clicked.connect(self.test3_start)
        self.but_sendresults.clicked.connect(self.next)
    def next(self):
        self.hide()
        self.final = finalWin()
        
test = TestWin()
app.exec_()