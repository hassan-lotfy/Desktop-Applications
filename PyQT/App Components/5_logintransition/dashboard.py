# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 501)
        MainWindow.setStyleSheet("background-color: #F9F6F0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wdgt_sidebar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdgt_sidebar.sizePolicy().hasHeightForWidth())
        self.wdgt_sidebar.setSizePolicy(sizePolicy)
        self.wdgt_sidebar.setMinimumSize(QtCore.QSize(140, 0))
        self.wdgt_sidebar.setStyleSheet("QWidget#wdgt_sidebar {\n"
"    background-color: #8B6E4E ;  /* Calm purple color */\n"
"\n"
"   /* border-bottom-left-radius: 15px;*/\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.wdgt_sidebar.setObjectName("wdgt_sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wdgt_sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_1 = QtWidgets.QFrame(self.wdgt_sidebar)
        self.frame_1.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_1.setStyleSheet("background-color: transparent;\n"
"padding-bottom: 2 px;")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setStyleSheet("background-color:transparent;\n"
"color:White;\n"
"font: bold 16px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame_1)
        self.line = QtWidgets.QFrame(self.wdgt_sidebar)
        self.line.setStyleSheet("background-color: 0xffffff;\n"
"padding-bottom: 10px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.wdgt_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 25))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_home = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_home.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"    color:white;\n"
"    font: bold 14px;\n"
"    text-align: left;  /* Aligns the text to the left */\n"
"\n"
"}\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: #8B5E3C;  /* Lighter shade for hover */\n"
"}\n"
"\n"
"/* Clicked (pressed) effect */\n"
"QPushButton:pressed {\n"
"    background-color: #6A3E26;  /* Darker shade for click effect */\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(16, 16))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)
        self.btn_users = QtWidgets.QPushButton(self.frame)
        self.btn_users.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_users.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"    color:white;\n"
"    font: bold 14px;\n"
"    text-align: left;  /* Aligns the text to the left */\n"
"\n"
"}\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: #8B5E3C;  /* Lighter shade for hover */\n"
"}\n"
"\n"
"/* Clicked (pressed) effect */\n"
"QPushButton:pressed {\n"
"    background-color: #6A3E26;  /* Darker shade for click effect */\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_users.setIcon(icon1)
        self.btn_users.setObjectName("btn_users")
        self.verticalLayout_4.addWidget(self.btn_users)
        self.btn_products = QtWidgets.QPushButton(self.frame)
        self.btn_products.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_products.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"    color:white;\n"
"    font: bold 14px;\n"
"    text-align: left;  /* Aligns the text to the left */\n"
"\n"
"}\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: #8B5E3C;  /* Lighter shade for hover */\n"
"}\n"
"\n"
"/* Clicked (pressed) effect */\n"
"QPushButton:pressed {\n"
"    background-color: #6A3E26;  /* Darker shade for click effect */\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/cart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_products.setIcon(icon2)
        self.btn_products.setObjectName("btn_products")
        self.verticalLayout_4.addWidget(self.btn_products)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.wdgt_sidebar)
        self.wdgt_mainPages = QtWidgets.QStackedWidget(self.centralwidget)
        self.wdgt_mainPages.setStyleSheet("")
        self.wdgt_mainPages.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wdgt_mainPages.setObjectName("wdgt_mainPages")
        self.pg_home = QtWidgets.QWidget()
        self.pg_home.setStyleSheet("background-color: #F5F5DC")
        self.pg_home.setObjectName("pg_home")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pg_home)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.pg_home)
        self.label_2.setStyleSheet("color: black;\n"
"font: bold 18px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.wdgt_mainPages.addWidget(self.pg_home)
        self.pg_users = QtWidgets.QWidget()
        self.pg_users.setStyleSheet("background-color: #F5F5DC")
        self.pg_users.setObjectName("pg_users")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pg_users)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.pg_users)
        self.label_3.setStyleSheet("color: black;\n"
"font: bold 18px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.wdgt_mainPages.addWidget(self.pg_users)
        self.pg_products = QtWidgets.QWidget()
        self.pg_products.setStyleSheet("background-color: #F5F5DC")
        self.pg_products.setObjectName("pg_products")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pg_products)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.pg_products)
        self.label_4.setStyleSheet("color: black;\n"
"font: bold 18px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.wdgt_mainPages.addWidget(self.pg_products)
        self.horizontalLayout.addWidget(self.wdgt_mainPages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_users.setText(_translate("MainWindow", "Users"))
        self.btn_products.setText(_translate("MainWindow", "Products"))
        self.label_2.setText(_translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "Users"))
        self.label_4.setText(_translate("MainWindow", "Products"))
import resources_rc
