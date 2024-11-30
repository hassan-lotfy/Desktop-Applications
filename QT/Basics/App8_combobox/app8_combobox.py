import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from app8_converted_combobox import Ui_MainWindow

class my_app(QMainWindow):
    def __init__(self):
        # super will init the current class with all atts and methods from QMainWindow
        # if we inherit instead of using super, the constructor will not be called
        super(my_app,self).__init__()

        # init UI from QT designer UI converted file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # add items to the combobox
        cb_clubs = self.ui.cb_clubs
        cb_clubs.addItem("Real Madrid")
        cb_clubs.addItem("Barcelona")
        cb_clubs.addItem("Liverpool")

        # self.ui.cb_clubs.currentIndexChanged.connect(self.selected_index)
        #cb_clubs.currentIndexChanged.connect(self.selected_index)
        # link function to be executed when a new item is selected inside the combobox
        cb_clubs.currentIndexChanged[str].connect(self.selected_index_text)

        # link functions to buttons
        self.ui.btn_get.clicked.connect(self.get_clicked)
        self.ui.btn_load.clicked.connect(self.load_clicked)
        self.ui.btn_clear.clicked.connect(self.clear_clicked)

    # when get is clicked, will display the selected item from the combobox
    def get_clicked(self):
        #self.ui.label.setText(str(self.ui.cb_clubs.currentIndex()))
        text = self.ui.cb_clubs.currentText()
        self.ui.label.setText(text)

    # when load is clicked, will upload PSG and BVB teams to the combobox menu
    def load_clicked(self):
        football_teams = ["PSG", "BVB"]
        self.ui.cb_clubs.addItems(football_teams)

    # when clear is clicked, will clear all items inside the combobox menu
    def clear_clicked(self):
        self.ui.cb_clubs.clear()



    #def selected_index(self, index):
        #print(index)

    # when index changes, function will display the new selected item
    def selected_index_text(self, str):
        print(str)



def create_app():
    # instantiate app class
    app = QtWidgets.QApplication(sys.argv)
    # instantiate window
    win = my_app()
    # show the window
    win.show()
    sys.exit(app.exec_())

create_app()
