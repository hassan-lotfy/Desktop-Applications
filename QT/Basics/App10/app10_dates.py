import sys
from PyQt5 import QtWidgets
from app10_converted_dates import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

# used popUp feature for dates in Qt designer tool
# set default date value at the beginning also from the tool

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        # init UI from QT designer converted file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # link functions to be executed when buttons are clicked
        self.ui.btn_startEnd.clicked.connect(self.clicked_startToEnd)
        self.ui.btn_startCurrent.clicked.connect(self.clicked_startToCurrent)

    # function to display days from start date to end date
    def clicked_startToEnd(self):
        start = self.ui.D_start.date()
        end = self.ui.D_end.date()
        diff = start.daysTo(end)
        print(diff)
        self.ui.lbl_startEnd.setText("Number of days between start \n"
                                     f"date and end Date is: {diff}")


    # function to display days from start date to current date
    def clicked_startToCurrent(self):
        start = self.ui.D_start.date()
        current = QDate.currentDate()
        diff = start.daysTo(current)

        self.ui.lbl_startCurrent.setText("Number of days between start\n "
                                         f"date and current Date is: {diff}")


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()


