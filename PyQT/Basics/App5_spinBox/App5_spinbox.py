from app5_converted_spinbox import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        # setup UI from QT Designer file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set minimum and maximum values to the spinbox
        self.ui.spinBox.setMinimum(2)
        self.ui.spinBox.setMaximum(12)

        # link spinBox value change to a function
        self.ui.spinBox.valueChanged.connect(self.display)

        # link function to push button
        self.ui.pushButton.clicked.connect(self.clicked)

    # function to display "value changed" when spinbox value changes
    def display(self):
        print("value changed")

    # function to display the spinBox value on label when button is pressed
    def clicked(self):
        self.ui.label.setText(str(self.ui.spinBox.value()))


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
    widget.setFixedWidth(440)
    widget.setFixedHeight(462)
    widget.show()
    sys.exit(app.exec_())

app_create()