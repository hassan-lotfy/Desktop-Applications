from app7_converted_radio import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.egypt.toggled.connect(self.selected)
        self.ui.england.toggled.connect(self.selected)
        self.ui.ksa.toggled.connect(self.selected)
        self.ui.germany.toggled.connect(self.selected)

        self.ui.engineer.toggled.connect(self.selected)
        self.ui.doctor.toggled.connect(self.selected)
        self.ui.teacher.toggled.connect(self.selected)
        self.ui.trainer.toggled.connect(self.selected)

        self.ui.btn_get.clicked.connect(self.clicked)

    def selected(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())
            self.ui.lbl_result.setText(rb.text())

    def clicked(self):
        text = ''
        countries_items = self.ui.box_country.findChildren(QtWidgets.QRadioButton)
        for item in countries_items:
            if item.isChecked():
                text += f"Country: {item.text()}, "
                break

        jobs_items = self.ui.box_job.findChildren(QtWidgets.QRadioButton)
        for item in jobs_items:
            if item.isChecked():
                text += f"Job: {item.text()}"
                break

        self.ui.lbl_result.setText(text)


def create_app():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()








def create_app():
    app = QApplication()
    win = my_app()
    win.show()
    sys.exit(app.exec_())

