import sys
from pickle import FALSE

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from ui_login import Ui_LoginWindow
from ui_register import Ui_RegisterWindow
#from PyQt5.uic import loadUi

# database for initially registered accounts
data_base = {"hassan@email.com": "password"}

# login page
class Login(QMainWindow):
    # take widget as parameter, to switch pages in case register is clicked
    def __init__(self, widget):
        super(Login,self).__init__()
        # loadUI method disadvantage: variables (UI elements) name will not be predicted by IDE while typing
        #loadUi("login.ui", self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        # reference the widget
        self.widget = widget

        # assign function to buttons
        self.ui.btn_login_signin.clicked.connect(self.clicked_signin)
        self.ui.btn_login_register.clicked.connect(self.clicked_register)


        # make password appear as ****
        self.ui.txt_login_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    # function to check credentials and print login successful on console if valid credentials entered
    def clicked_signin(self):
        # fetch user input: email and password
        current_email = self.ui.txt_login_email.text()
        current_password = self.ui.txt_login_pass.text()

        # check if email is inside database, if found verify pass is correct
        found = False
        for key in data_base:
            if key == current_email and data_base[key] == current_password:
                found = True

        if found is True:
            print("login successful")
        else:
            print("Invalid username or password")

    # function to switch to login page if register is clicked
    def clicked_register(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


# register page
class Register(QMainWindow):
    def __init__(self,widget):
        super(Register,self).__init__()
        #loadUi("login.ui", self)
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        # reference the widget
        self.widget = widget

        # assign functions to buttons when clicked
        self.ui.btn_register_signup.clicked.connect(self.clicked_signup)
        self.ui.btn_register_login.clicked.connect(self.clicked_login)

        # make password appear as ****
        self.ui.txt_register_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.txt_register_repass.setEchoMode(QtWidgets.QLineEdit.Password)

    # function to validate input email, verify that two passwords match, and add the account to database
    def clicked_signup(self):
        email = self.ui.txt_register_email.text()
        password = self.ui.txt_register_pass.text()
        repassword = self.ui.txt_register_repass.text()
        # verify that two passwords match
        if password == repassword:
            data_base[email] = password
            print("registered successfully")
            self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        else:
            print("passwords don't match")

    # function to switch to login page if login is clicked
    def clicked_login(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)



def app_create():
    app = QApplication(sys.argv)

    # add widget to contain multiple pages (login and register)
    widget = QtWidgets.QStackedWidget()

    # instantiate windows (pages)
    login_window = Login(widget)
    register_window = Register(widget)

    # add the pages to the widget
    widget.addWidget(login_window)
    widget.addWidget(register_window)

    # set window size
    widget.setFixedWidth(420)
    widget.setFixedHeight(375)

    widget.show()

    sys.exit(app.exec_())

app_create()
