import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow
#from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #loadUi("login.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        table_width = self.ui.tableWidget.width()
        self.ui.tableWidget.setColumnWidth(0, int(table_width/2))
        self.ui.tableWidget.setColumnWidth(1, int(table_width/2))

        self.load_data()

        # Configure table scrolling behavior for smoother scrolling
        self.ui.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ui.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        # set scrolling step when < > arrow is pressed
        horizontal_scrollbar = self.ui.tableWidget.horizontalScrollBar()
        horizontal_scrollbar.setSingleStep(2)

    def load_data(self):
        # assume this is out fetched data base
        students = [ {"name": "Hassan", "school": "Al Shark", "city": "Cairo"},
                     {"name": "Amr", "school": "Pioneers", "city": "Alex"},
                     {"name": "Basma", "school": "NA", "city": "Giza"}]
        row = 0
        self.ui.tableWidget.setRowCount(len(students))
        for row, student in enumerate(students):  # row will be the index of the current iteration
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student["name"]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student["school"]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student["city"]))



def app_create():
    app = QApplication(sys.argv)

    # windows indexes
    index = {}

    # add widget to contain multiple pages (login and register)
    widget = QtWidgets.QStackedWidget()

    # instantiate windows (pages)
    main_window = MainWindow()

    # add the pages to the widget
    widget.addWidget(main_window)
    index[main_window] = 0


    # set window size
    widget.setFixedWidth(680)
    widget.setFixedHeight(550)

    widget.show()

    sys.exit(app.exec_())

app_create()
