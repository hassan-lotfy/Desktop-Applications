import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets

def  window():
    # create app
    app = QApplication(sys.argv)
    # app window
    win = QMainWindow()

    # X , Y coordinates in the screen,4 height, width of window
    win.setGeometry(700,100,400,400)

    # add title
    win.setWindowTitle("Turtle Code")
    # add pic beside window title (inside project directory)
    win.setWindowIcon(QIcon("logo.webp"))

    # add labels
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Name: ")
    lbl_name.move(50,50)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Surname: ")
    lbl_surname.move(50,90)

    # create text box in front of the label
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200,50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200,90)

    # create button to save name and surname

    # function to be called when button is clicked
    def clicked():
        print(txt_name.text())
        print(txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")

    btn_save.clicked.connect(clicked)
    btn_save.move(150,140)

    # to show the Gui window
    win.show()
    app.exec_()
    # use sys.exit to get return code
    sys.exit()


window()






