# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app6_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_hobby = QtWidgets.QPushButton(self.centralwidget)
        self.get_hobby.setGeometry(QtCore.QRect(130, 330, 121, 41))
        self.get_hobby.setObjectName("get_hobby")
        self.group_hobby = QtWidgets.QGroupBox(self.centralwidget)
        self.group_hobby.setGeometry(QtCore.QRect(110, 40, 191, 261))
        self.group_hobby.setObjectName("group_hobby")
        self.widget = QtWidgets.QWidget(self.group_hobby)
        self.widget.setGeometry(QtCore.QRect(10, 20, 171, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Cinema = QtWidgets.QCheckBox(self.widget)
        self.Cinema.setTristate(False)
        self.Cinema.setObjectName("Cinema")
        self.verticalLayout.addWidget(self.Cinema)
        self.Reading = QtWidgets.QCheckBox(self.widget)
        self.Reading.setTristate(False)
        self.Reading.setObjectName("Reading")
        self.verticalLayout.addWidget(self.Reading)
        self.Running = QtWidgets.QCheckBox(self.widget)
        self.Running.setTristate(False)
        self.Running.setObjectName("Running")
        self.verticalLayout.addWidget(self.Running)
        self.lbl_hobby = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hobby.setGeometry(QtCore.QRect(90, 400, 231, 16))
        self.lbl_hobby.setObjectName("lbl_hobby")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.get_hobby.setText(_translate("MainWindow", "Get"))
        self.group_hobby.setTitle(_translate("MainWindow", "GroupBox"))
        self.Cinema.setText(_translate("MainWindow", "Cinema"))
        self.Reading.setText(_translate("MainWindow", "Reading"))
        self.Running.setText(_translate("MainWindow", "Running"))
        self.lbl_hobby.setText(_translate("MainWindow", "hobby"))
