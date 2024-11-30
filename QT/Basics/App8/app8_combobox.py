import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from app8_converted_combobox import Ui_MainWindow

class my_app(QMainWindow):
    def __init__(self):
        # super will init the current class with all atts and methods from QMainWindow
        # if we inherit instead of using super, the constructor will not be called
        super(my_app,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        cb_clubs = self.ui.cb_clubs
        cb_clubs.addItem("Real Madrid")
        cb_clubs.addItem("Barcelona")
        cb_clubs.addItem("Liverpool")

        # self.ui.cb_clubs.currentIndexChanged.connect(self.selected_index)
        #cb_clubs.currentIndexChanged.connect(self.selected_index)
        cb_clubs.currentIndexChanged[str].connect(self.selected_index_text)

        self.ui.btn_get.clicked.connect(self.get_clicked)
        self.ui.btn_load.clicked.connect(self.load_clicked)
        self.ui.btn_clear.clicked.connect(self.clear_clicked)


    def get_clicked(self):
        #self.ui.label.setText(str(self.ui.cb_clubs.currentIndex()))
        text = self.ui.cb_clubs.currentText()
        self.ui.label.setText(text)

    def load_clicked(self):
        football_teams = ["PSG", "BVB"]
        self.ui.cb_clubs.addItems(football_teams)

    def clear_clicked(self):
        self.ui.cb_clubs.clear()



    #def selected_index(self, index):
        #print(index)

    def selected_index_text(self, str):
        print(str)



def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()
