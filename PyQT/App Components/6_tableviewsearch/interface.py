# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 513)
        MainWindow.setMinimumSize(QtCore.QSize(554, 513))
        MainWindow.setMaximumSize(QtCore.QSize(554, 513))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 87, 241, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_search = QtWidgets.QLineEdit(self.frame)
        self.txt_search.setObjectName("txt_search")
        self.verticalLayout.addWidget(self.txt_search)
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tableView.setStyleSheet("/* table background and text colors */\n"
"QTableView{\n"
"    background-color:#f0f0f0;\n"
"    color:black;\n"
"}\n"
"/* items hover */\n"
"QTableView::item:hover {\n"
"    background-color: #e5ffef;  /* Color when hovering over a cell */\n"
"}\n"
"/* selected items color and text color when selected*/\n"
"QTableView::item:selected {\n"
"    background-color: #e5ffef;  /* Color when hovering over a cell */\n"
"    color:black;\n"
"}\n"
"\n"
"/* first row and first column coloring */\n"
"QHeaderView::section {\n"
"    background-color: darkgrey;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    /*padding:5px;*/ /* to increase main row column size */\n"
"}\n"
"\n"
"/* scrollbar background and size */\n"
"QScrollBar:horizontal {\n"
"    background: lightgrey; \n"
"    height: 10px; /* height of bar */\n"
"} \n"
"QScrollBar:vertical {\n"
"    background: lightgrey;  \n"
"    width: 10px;\n"
"}\n"
"\n"
"/* slider color and slider edges radius to make it curvy*/\n"
"QScrollBar::handle:horizontal, QScrollBar::handle:vertical {\n"
"    background: darkgrey;  \n"
"    border-radius: 5px;\n"
"}\n"
"/* add scrollbar buttons to right and left */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #FF6347;  /* Distinct color */\n"
"    width: 20px;          /* Adequate width */\n"
"    height: 20px;         /* Adequate height */\n"
"    border: 1px solid #000; /* Border to make them more visible */\n"
"    subcontrol-origin: margin; /* Ensure they appear inside the scrollbar */\n"
"}")
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        self.menuitem = QtWidgets.QMenu(self.menubar)
        self.menuitem.setObjectName("menuitem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionitem2 = QtWidgets.QAction(MainWindow)
        self.actionitem2.setObjectName("actionitem2")
        self.actionitem3 = QtWidgets.QAction(MainWindow)
        self.actionitem3.setObjectName("actionitem3")
        self.actionitem4 = QtWidgets.QAction(MainWindow)
        self.actionitem4.setObjectName("actionitem4")
        self.actionitem5 = QtWidgets.QAction(MainWindow)
        self.actionitem5.setObjectName("actionitem5")
        self.actionitem6 = QtWidgets.QAction(MainWindow)
        self.actionitem6.setObjectName("actionitem6")
        self.menuitem.addAction(self.actionitem2)
        self.menuitem.addSeparator()
        self.menuitem.addAction(self.actionitem3)
        self.menuitem.addAction(self.actionitem4)
        self.menuitem.addSeparator()
        self.menuitem.addAction(self.actionitem5)
        self.menuitem.addAction(self.actionitem6)
        self.menubar.addAction(self.menuitem.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuitem.setTitle(_translate("MainWindow", "item"))
        self.actionitem2.setText(_translate("MainWindow", "item2"))
        self.actionitem3.setText(_translate("MainWindow", "item3"))
        self.actionitem4.setText(_translate("MainWindow", "item4"))
        self.actionitem5.setText(_translate("MainWindow", "item5"))
        self.actionitem6.setText(_translate("MainWindow", "item6"))
