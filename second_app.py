from PyQt5.QtCore import Qt , QTime , QTimer
from PyQt5.QtWidgets import (QApplication,QWidget,
QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QMessageBox, QRadioButton)
from intr import *
from final_win import TestWin2

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('ВТОРОЕ ОКНО')
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.Label_name=QLabel("Введите ФИО")
        self.line_l_f_name=QLineEdit('Ф.И.О')

        self.label_age=QLabel('Полных лет')
        self.line_age=QLineEdit('лет')

        self.Label_inst_i=QLabel(instr_1)

        self.btn_test_1=QPushButton('Начать первый тест')
        self.line_bpm_1=QLineEdit('Введите количество ударов в минуту')
        self.check_res=QPushButton('Узнать резуьтат')
        self.text_timer=QLabel("00:00:00")
        self.layout_v_l=QVBoxLayout()
        self.layout_v_r=QVBoxLayout()
        self.total_layout=QHBoxLayout()
        self.layout_v_l.addWidget(self.Label_name)
        self.layout_v_l.addWidget(self.line_l_f_name)
        self.layout_v_l.addWidget(self.label_age)
        self.layout_v_l.addWidget(self.line_age)
        self.layout_v_l.addWidget(self.Label_inst_i)
        self.layout_v_l.addWidget(self.line_bpm_1)
        self.layout_v_l.addWidget(self.text_timer)
        self.layout_v_l.addWidget(self.btn_test_1)
        self.layout_v_l.addWidget(self.check_res,alignment = Qt.AlignRight)
        
        self.setLayout(self.layout_v_l)

    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()

    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def connects(self):
        self.btn_test_1.clicked.connect(self.timer_test)
        #self.check_res.clicked.connect(self.next_click)


    def next_click(self):
        pass
        
