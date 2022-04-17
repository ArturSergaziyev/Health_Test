from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QMessageBox,QHBoxLayout,QRadioButton)

app = QApplication([]) #Создать само преложение
my_win = QWidget() #создать главное окно
my_win.setWindowTitle('Вопросы')
 #Вывести главное окно\

question=QLabel('В каком в году родился Никита?')
btn_answer1=QRadioButton('2002')
btn_answer2=QRadioButton('2009')
btn_answer3=QRadioButton('2015')
btn_answer4=QRadioButton('2018')

layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()

layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4,alignment=Qt.AlignCenter)

layout_main=QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

msg = QMessageBox()
msg.setIcon(QMessageBox.Critical)
msg.setText("Ошбка")
msg.setInformativeText('Проверка Ошибки')
msg.setWindowTitle("Error")
msg.exec_()

my_win.setLayout(layout_main)

my_win.show()
app.exec_()
