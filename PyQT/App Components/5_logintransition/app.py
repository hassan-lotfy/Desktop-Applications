from PyQt5.uic.Compiler.qtproxies import QtGui

from dashboard import Ui_MainWindow
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QAction
from PyQt5 import QtWidgets
from login import Ui_Dialog_Login
from PyQt5.QtCore import QPropertyAnimation, QSize, QTimer, QEasingCurve
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

database = {"username": "password"}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # init UI from QT Designer converted file (interface.py)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # assign indexes for main pages (based on the UI file order)
        self.pg_home_index = 0
        self.pg_users_index = 1
        self.pg_products_index = 2

        self.ui.btn_home.clicked.connect(self.sidebar_button_clicked)
        self.ui.btn_users.clicked.connect(self.sidebar_button_clicked)
        self.ui.btn_products.clicked.connect(self.sidebar_button_clicked)


    def sidebar_button_clicked(self):
        # Get the sender button that triggered the event
        button = self.sender()
        # check the pressed button, and open the corresponding page
        if button == self.ui.btn_home:
            self.ui.wdgt_mainPages.setCurrentIndex(self.pg_home_index)
        elif button == self.ui.btn_users:
            self.ui.wdgt_mainPages.setCurrentIndex(self.pg_users_index)
        elif button == self.ui.btn_products:
            self.ui.wdgt_mainPages.setCurrentIndex(self.pg_products_index)




class LoginWindow(QDialog):
    def __init__(self, main_widget):
        super(LoginWindow, self).__init__()
        # init UI from QT Designer converted file (interface.py)
        self.ui = Ui_Dialog_Login()
        self.ui.setupUi(self)

        # create widget variable to login to the main dashboard
        self.main_widget = main_widget


        # Add icon inside username and password line edits
        self.ui.txt_username.addAction(QIcon("icons.ico/user.ico"), QLineEdit.LeadingPosition)
        self.ui.txt_password.addAction(QIcon("icons.ico/lock.ico"), QLineEdit.LeadingPosition)
        # hide password (*****)
        self.ui.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # add function to login button
        self.ui.btn_login.clicked.connect(self.login_clicked)
        # pressing enter inside username or password will perform click login button action
        self.ui.txt_username.returnPressed.connect(self.ui.btn_login.click)
        self.ui.txt_password.returnPressed.connect(self.ui.btn_login.click)


    def login_clicked(self):
        username = self.ui.txt_username.text()

        # search for username
        username_found = False
        for key in database:

            if key == username: # if username is found, check the password
                username_found = True
                password = self.ui.txt_password.text()
                if database[key] == password: # if password is correct, login to dashboard

                    self.main_widget.setCurrentIndex(1)
                    self.main_widget.showMaximized()
                    break

                else: # print password incorrect error
                    self.ui.lbl_loginerror.setText("Invalid Password")
                    break

        if username_found == False:
            self.ui.lbl_loginerror.setText("Invalid username")

    def focus_username(self):
        self.ui.txt_username.setFocus()

    def set_tab_jumps(self):
        # Set tab order: from username -> password -> login button
        widgets = [self.ui.txt_username, self.ui.txt_password, self.ui.btn_login]
        for i in range(len(widgets)-1):
            self.setTabOrder(widgets[i],widgets[i+1])

    def setup(self):
        self.focus_username()
        self.set_tab_jumps()

def app_create():
    app = QApplication(sys.argv)

    # windows indexes
    # add widget to contain multiple pages (login and register)
    main_widget = QtWidgets.QStackedWidget()

    # instantiate windows (pages)
    login_window = LoginWindow(main_widget)
    main_window = MainWindow()

    # add the pages to the widget
    main_widget.addWidget(login_window)
    main_widget.addWidget(main_window)

    main_widget.setWindowTitle("Courses Hub")
    main_widget.show()

    # setup initial focus and pressing tab jumps order
    login_window.setup()

    sys.exit(app.exec_())

app_create()