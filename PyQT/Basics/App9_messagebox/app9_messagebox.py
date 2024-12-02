import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from app9_converted_messagebox import Ui_MainWindow


class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()

        # init UI from QT Designer UI converted file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.show_message_box)


    def show_message_box(self):
        # create the message box UI
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Close")
        msg.setText("Press Ok to confirm")
        # we might set warning sign (with warning sound), question sign..etc
        #msg.setIcon(QMessageBox.Question)
        msg.setIcon(QMessageBox.Warning)
        # bitwise OR to pass 1 argument activating OK, Cancel and Ignore
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # Cancel will be selected by default as box appears
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setDetailedText("This dialogue box to confirm if you want to exit the app or not")

        # we can use connect method when a button is pressed, or save the pressed button then process

        msg.buttonClicked.connect(self.clicked)

        # stores the clicked button
        msg_result = msg.exec_()

        # the pressed button code is stored in msg_result
        print(msg_result)
        if msg_result == QMessageBox.Ok:
            print("Ok is pressed")
        elif msg_result == QMessageBox.Cancel:
            print("Cancel is pressed")
        else:
            print("Ignore is pressed")

    # function to display the message box and define its content and buttons
    def show_message_box2(self):
        msg_result = QMessageBox.question(self, 'Close', 'Press OK to Confirm',
                    QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)

        if msg_result == QMessageBox.Ok:
            QtWidgets.qApp.quit()
        else:
            print("Cancellation not confirmed")


    # function to be executed when a button is clicked from the message box (Ok, Cancel, ..)
    def clicked(self, i):
        if (i.text() == "OK"):
            QtWidgets.qApp.quit()
        elif (i.text() == "Cancel"):
            print("cancelled")
        else:
            print("ignored")



def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())


create_app()
