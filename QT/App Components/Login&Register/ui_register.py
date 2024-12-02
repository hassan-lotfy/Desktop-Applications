# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(420, 375)
        RegisterWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("font: bold 18pt \"Calibre\"; color:rgb(231, 231, 231)")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_register_email = QtWidgets.QLabel(self.frame_2)
        self.lbl_register_email.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.lbl_register_email.setStyleSheet("font: bold 16px; color:rgb(204, 0, 0)")
        self.lbl_register_email.setObjectName("lbl_register_email")
        self.txt_register_email = QtWidgets.QLineEdit(self.frame_2)
        self.txt_register_email.setGeometry(QtCore.QRect(170, 10, 181, 20))
        self.txt_register_email.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.txt_register_email.setPlaceholderText("")
        self.txt_register_email.setObjectName("txt_register_email")
        self.lbl_register_pass = QtWidgets.QLabel(self.frame_2)
        self.lbl_register_pass.setGeometry(QtCore.QRect(30, 40, 101, 21))
        self.lbl_register_pass.setStyleSheet("font: bold 16px; color:rgb(204, 0, 0)")
        self.lbl_register_pass.setObjectName("lbl_register_pass")
        self.txt_register_pass = QtWidgets.QLineEdit(self.frame_2)
        self.txt_register_pass.setGeometry(QtCore.QRect(170, 40, 181, 20))
        self.txt_register_pass.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.txt_register_pass.setPlaceholderText("")
        self.txt_register_pass.setObjectName("txt_register_pass")
        self.txt_register_repass = QtWidgets.QLineEdit(self.frame_2)
        self.txt_register_repass.setGeometry(QtCore.QRect(170, 70, 181, 20))
        self.txt_register_repass.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.txt_register_repass.setPlaceholderText("")
        self.txt_register_repass.setObjectName("txt_register_repass")
        self.lbl_register_repass = QtWidgets.QLabel(self.frame_2)
        self.lbl_register_repass.setGeometry(QtCore.QRect(30, 70, 121, 21))
        self.lbl_register_repass.setStyleSheet("font: bold 16px; color:rgb(204, 0, 0)")
        self.lbl_register_repass.setObjectName("lbl_register_repass")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_register_signup = QtWidgets.QPushButton(self.frame_4)
        self.btn_register_signup.setMaximumSize(QtCore.QSize(60, 22))
        self.btn_register_signup.setStyleSheet("font: 14px;\n"
"background-color: rgb(235, 235, 235);")
        self.btn_register_signup.setObjectName("btn_register_signup")
        self.horizontalLayout.addWidget(self.btn_register_signup)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 131, 20))
        self.label_4.setMaximumSize(QtCore.QSize(200, 20))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.btn_register_login = QtWidgets.QPushButton(self.frame_5)
        self.btn_register_login.setGeometry(QtCore.QRect(220, 10, 40, 16))
        self.btn_register_login.setMaximumSize(QtCore.QSize(50, 20))
        self.btn_register_login.setBaseSize(QtCore.QSize(0, 0))
        self.btn_register_login.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    text-decoration: underline;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: lightblue;\n"
"}")
        self.btn_register_login.setObjectName("btn_register_login")
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.label.setText(_translate("RegisterWindow", "Register"))
        self.lbl_register_email.setText(_translate("RegisterWindow", "Email"))
        self.lbl_register_pass.setText(_translate("RegisterWindow", "Password"))
        self.lbl_register_repass.setText(_translate("RegisterWindow", "Re-Password"))
        self.btn_register_signup.setText(_translate("RegisterWindow", "Sign Up"))
        self.label_4.setText(_translate("RegisterWindow", "Already have an account?"))
        self.btn_register_login.setText(_translate("RegisterWindow", "Login"))