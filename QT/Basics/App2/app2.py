import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        # init instance from parent class with initial features till they are overriden
        super(my_window,self).__init__()
        self.setGeometry(0,0,500,400)
        self.setWindowTitle("Desktop Application 2")
        self.setToolTip("tool tip")
        self.setWindowIcon(QIcon("logo.webp"))
        # init GUI
        self.initUi()


    def initUi(self):
        # add self before variables to make them class attributes

        # labels
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Name: ")
        self.lbl_name.move(50, 50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname: ")
        self.lbl_surname.move(50, 90)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Result')
        self.lbl_result.move(200, 170)
        self.lbl_result.resize(400,32)

        # text fields
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200, 50)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200, 90)

        # save button
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(150, 140)

    def clicked(self):
        self.lbl_result.setText('Name: '+ self.txt_name.text() + '\n' + 'Surname: ' + self.txt_surname.text())

def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    # store exit code
    exit_code = app.exec_()
    # pass it to OS
    sys.exit(exit_code)

window()



