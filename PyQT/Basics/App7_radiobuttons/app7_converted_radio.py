# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app7_radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box_country = QtWidgets.QGroupBox(self.centralwidget)
        self.box_country.setGeometry(QtCore.QRect(50, 50, 120, 141))
        self.box_country.setObjectName("box_country")
        self.widget = QtWidgets.QWidget(self.box_country)
        self.widget.setGeometry(QtCore.QRect(20, 27, 99, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.egypt = QtWidgets.QRadioButton(self.widget)
        self.egypt.setObjectName("egypt")
        self.verticalLayout.addWidget(self.egypt)
        self.england = QtWidgets.QRadioButton(self.widget)
        self.england.setObjectName("england")
        self.verticalLayout.addWidget(self.england)
        self.ksa = QtWidgets.QRadioButton(self.widget)
        self.ksa.setObjectName("ksa")
        self.verticalLayout.addWidget(self.ksa)
        self.germany = QtWidgets.QRadioButton(self.widget)
        self.germany.setObjectName("germany")
        self.verticalLayout.addWidget(self.germany)
        self.box_job = QtWidgets.QGroupBox(self.centralwidget)
        self.box_job.setGeometry(QtCore.QRect(290, 50, 120, 141))
        self.box_job.setObjectName("box_job")
        self.layoutWidget = QtWidgets.QWidget(self.box_job)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 27, 99, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.engineer = QtWidgets.QRadioButton(self.layoutWidget)
        self.engineer.setObjectName("engineer")
        self.verticalLayout_2.addWidget(self.engineer)
        self.doctor = QtWidgets.QRadioButton(self.layoutWidget)
        self.doctor.setObjectName("doctor")
        self.verticalLayout_2.addWidget(self.doctor)
        self.teacher = QtWidgets.QRadioButton(self.layoutWidget)
        self.teacher.setObjectName("teacher")
        self.verticalLayout_2.addWidget(self.teacher)
        self.trainer = QtWidgets.QRadioButton(self.layoutWidget)
        self.trainer.setObjectName("trainer")
        self.verticalLayout_2.addWidget(self.trainer)
        self.btn_get = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get.setGeometry(QtCore.QRect(180, 190, 101, 51))
        self.btn_get.setObjectName("btn_get")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(110, 280, 241, 31))
        self.lbl_result.setObjectName("lbl_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
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
        self.box_country.setTitle(_translate("MainWindow", "Country"))
        self.egypt.setText(_translate("MainWindow", "Egypt"))
        self.england.setText(_translate("MainWindow", "England"))
        self.ksa.setText(_translate("MainWindow", "KSA"))
        self.germany.setText(_translate("MainWindow", "Germany"))
        self.box_job.setTitle(_translate("MainWindow", "Job"))
        self.engineer.setText(_translate("MainWindow", "Engineer"))
        self.doctor.setText(_translate("MainWindow", "Doctor"))
        self.teacher.setText(_translate("MainWindow", "Teacher"))
        self.trainer.setText(_translate("MainWindow", "Trainer"))
        self.btn_get.setText(_translate("MainWindow", "Get"))
        self.lbl_result.setText(_translate("MainWindow", "Result"))
