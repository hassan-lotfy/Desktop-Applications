import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import app4_converted_calc
from app4_converted_calc import Ui_MainWindow


class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        # create subclass inside my_app
        self.ui = Ui_MainWindow()
        # init the ui for this subclass to our app
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.calculate)
        self.ui.btn_sub.clicked.connect(self.calculate)
        self.ui.btn_mul.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)

    def calculate(self):
        btn = self.sender()
        btn = btn.text()
        print(btn)
        result = 0

        if btn == "+":
            result = int(self.ui.txt_num1.toPlainText()) + int(self.ui.txt_num2.toPlainText())
        elif btn == "-":
            result = int(self.ui.txt_num1.toPlainText()) - int(self.ui.txt_num2.toPlainText())
        elif btn == "*":
            result = int(self.ui.txt_num1.toPlainText()) * int(self.ui.txt_num2.toPlainText())
        else: # "/"
            result = int(self.ui.txt_num1.toPlainText()) / int(self.ui.txt_num2.toPlainText())

        self.ui.lbl_result.setText(f"Result: {result}")



def app():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()