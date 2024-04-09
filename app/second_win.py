# напиши здесь код для второго экрана приложения
from final_win import *
from instr import *
from PyQt5 import QtCore, QtMultimedia
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

class testWin(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.playing = 0
        self.player1 = QtMultimedia.QMediaPlayer()
        self.player2 = QtMultimedia.QMediaPlayer()
        self.micro = QtMultimedia.QMediaPlayer()
        self.microwave = QtCore.QUrl.fromLocalFile('microwave.mp3')
        self.tick_sound = QtCore.QUrl.fromLocalFile('single-tick-sound.mp3')
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def timer_event(self):
        self.time = self.time.addSecs(-1)
        if self.time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()
            self.time = QTime(0, 0, 0)
            self.micro.play()
            self.playing = 0
        self.timer_text.setText(self.time.toString("<b>hh:mm:ss<b>"))
        if self.x == 1 and self.playing:
            self.player1.play()
            self.x *= -1
        elif self.playing:
            self.player2.play()
            self.x *= -1

    def test1_start(self):
        self.time = QTime(0, 0, 15)
        self.timer.start(1000)
        self.playing = 1
        self.x = 1
        self.player2.play()
        self.timer_text.setText(self.time.toString("<b>hh:mm:ss<b>"))
    def test2_start(self):
        self.time = QTime(0, 0, 45)
        self.timer.start(1000)
        self.playing = 1
        self.x = 1
        self.player2.play()
        self.timer_text.setText(self.time.toString("<b>hh:mm:ss<b>"))
    def test3_start(self):
        self.time = QTime(0, 1, 0)
        self.timer.start(1000)
        self.playing = 1
        self.x = 1
        self.player2.play()
        self.timer_text.setText(self.time.toString("<b>hh:mm:ss<b>"))

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.player1.setMedia(QtMultimedia.QMediaContent(self.tick_sound))
        self.player2.setMedia(QtMultimedia.QMediaContent(self.tick_sound))
        self.micro.setMedia(QtMultimedia.QMediaContent(self.microwave))
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.timer_event)
        self.h_line = QHBoxLayout()
        self.h_line.setContentsMargins(20, 20, 20, 20)
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(QLabel(txt_name), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintname), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_age), alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLineEdit(txt_hintage), alignment=Qt.AlignLeft)
#test1
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.test1_but = QPushButton(txt_starttest1)
        self.l_line.addWidget(self.test1_but, alignment=Qt.AlignLeft)
        self.test1_line = QLineEdit(txt_hinttest1)
        self.l_line.addWidget(self.test1_line, alignment=Qt.AlignLeft)
#test2
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.test2_but = QPushButton(txt_starttest2)
        self.l_line.addWidget(self.test2_but, alignment=Qt.AlignLeft)
        self.test2_line = QLineEdit(txt_hinttest2)
#test3
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.test3_but = QPushButton(txt_starttest3)
        self.l_line.addWidget(self.test3_but, alignment=Qt.AlignLeft)
        self.test3_line = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.test2_line, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3_line, alignment=Qt.AlignLeft)

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
        self.r_index = str(4 * (int(self.test1_line.text()) + int(self.test2_line.text()) + int(self.test3_line.text()))/10)
        self.final = finalWin()
        self.final.get_index(self.r_index)