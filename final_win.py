from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,
QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QMessageBox, QRadioButton)
from intr import *

class TestWin2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('ФИНАЛЬНЫЙ ОКНО')
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
