import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import app4_converted_calc
from app4_converted_calc import Ui_MainWindow


class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()

        # init UI from QT Designer converted UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # link buttons to corresponding functions
        self.ui.btn_add.clicked.connect(self.calculate)
        self.ui.btn_sub.clicked.connect(self.calculate)
        self.ui.btn_mul.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)

    def calculate(self):
        # check the sender button
        btn = self.sender()
        btn = btn.text()
        print(btn)
        result = 0

        # perform calculation based on pressed button (sender)
        if btn == "+":
            result = int(self.ui.txt_num1.toPlainText()) + int(self.ui.txt_num2.toPlainText())
        elif btn == "-":
            result = int(self.ui.txt_num1.toPlainText()) - int(self.ui.txt_num2.toPlainText())
        elif btn == "*":
            result = int(self.ui.txt_num1.toPlainText()) * int(self.ui.txt_num2.toPlainText())
        else: # "/"
            result = int(self.ui.txt_num1.toPlainText()) / int(self.ui.txt_num2.toPlainText())

        # display result on UI label
        self.ui.lbl_result.setText(f"Result: {result}")



def app():
    # initiate app
    app = QApplication(sys.argv)
    # assign window
    win = my_app()
    # display the window in the app
    win.show()
    sys.exit(app.exec_())

app()