# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app8_combobox.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_clubs = QtWidgets.QComboBox(self.centralwidget)
        self.cb_clubs.setGeometry(QtCore.QRect(70, 90, 141, 31))
        self.cb_clubs.setObjectName("cb_clubs")
        self.btn_get = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.btn_get.setObjectName("btn_get")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.btn_load.setObjectName("btn_load")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(100, 280, 75, 23))
        self.btn_clear.setObjectName("btn_clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 70, 221, 231))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
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
        self.btn_get.setText(_translate("MainWindow", "get"))
        self.btn_load.setText(_translate("MainWindow", "load"))
        self.btn_clear.setText(_translate("MainWindow", "clear"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
