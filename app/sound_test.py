from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from instr import *

app = QApplication([])

class sound(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QtMultimedia.QMediaPlayer()
        self.url = QtCore.QUrl.fromLocalFile('microwave.mp3')
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(200, 200)
        self.move(win_x, win_y)
    def initUI(self):
        self.player.setMedia(QtMultimedia.QMediaContent(self.url))
        self.h_line = QVBoxLayout()
        self.sound_but = QPushButton('sound')
        self.h_line.addWidget(self.sound_but, alignment=Qt.AlignCenter)
        self.setLayout(self.h_line)
    def connects(self):
        self.sound_but.clicked.connect(self.play_sound)
    def play_sound(self):
        print('sound')
        self.player.play()

s = sound()
app.exec_()