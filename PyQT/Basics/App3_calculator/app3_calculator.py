import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):

    def __init__(self):
        # init the class with QMainWindow methods
        super(Calculator,self).__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("calculator.jpg"))
        self.setGeometry(500,200,350,450)
        self.initUI()

    def initUI(self):
        # labels number1, number2
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number 1")
        self.lbl_number1.move(10,10)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number 2")
        self.lbl_number2.move(10, 30)

        # text fields for number1, number2
        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(60, 20)
        self.txt_number1.resize(100,20)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(60, 40)
        self.txt_number2.resize(100, 20)

        # buttons, add subtract multiply divide
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("ADD")
        self.btn_add.move(125,100)


        self.btn_sub= QtWidgets.QPushButton(self)
        self.btn_sub.setText("SUBTRACT")
        self.btn_sub.move(125,150)


        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText("MULTIPLY")
        self.btn_mul.move(125, 200)


        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("DIVIDE")
        self.btn_div.move(125, 250)


        # label result
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: NA")
        self.lbl_result.move(150,300)

        # link functions to be executed when buttons are pressed
        self.btn_add.clicked.connect(self.calculate)
        self.btn_sub.clicked.connect(self.calculate)
        self.btn_mul.clicked.connect(self.calculate)
        self.btn_div.clicked.connect(self.calculate)

    def calculate(self):
        # check the clicked button using sender method
        btn = self.sender() # using btn = self.sender.text() will give error
        btn = btn.text()
        print(btn)

        # get the inputs from line edits
        num1 = int(self.txt_number1.text())
        num2 = int(self.txt_number2.text())

        # perform the calculation and display the result
        if btn == "ADD":
            self.lbl_result.setText(f"result: {num1+num2}")
        elif btn == "SUBTRACT":
            self.lbl_result.setText(f"result: {num1-num2}")
        elif btn == "MULTIPLY":
            self.lbl_result.setText(f"result: {num1*num2}")
        else: # DIVIDE
            self.lbl_result.setText(f"result: {num1/num2}")






def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()