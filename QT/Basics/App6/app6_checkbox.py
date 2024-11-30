"""
code: pyuic5 app6_checkbox.ui -o app6_converted_checkbox.py
"""

from app6_converted_checkbox import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Cinema.stateChanged.connect(self.show_state)
        self.ui.Reading.stateChanged.connect(self.show_state)
        self.ui.Running.stateChanged.connect(self.show_state)

        self.ui.get_hobby.clicked.connect(self.get_hobby)

    def get_hobby(self):
        # will find all checkboxes inside, use QWidget to find all kind of buttons inside
        checked_boxes_string = ""
        items_hobby = self.ui.group_hobby.findChildren(QtWidgets.QCheckBox)
        for item_hobby in items_hobby:
            if item_hobby.isChecked():
                checked_boxes_string += item_hobby.text() + " "
        self.ui.lbl_hobby.setText(checked_boxes_string)


    # value parameter is being passed automatically by stateChanged.connect method
    def show_state(self,value):
        # print(value) # 2 checked, 0 unchecked
        # print(self.ui.Cinema.isChecked()) # True, False
        # print(self.ui.Cinema.text()) # prints the button name that is checked or unchecked
        cb = self.sender()
        print(cb.text()) # the sender name
        print(cb.isChecked()) # True checked False unchecked

def app_create():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app_create()

