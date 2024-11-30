import sys
from PyQt5 import QtWidgets
from app11_converted_listwidget import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStudents()
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_edit.clicked.connect(self.edit)
        self.ui.btn_remove.clicked.connect(self.remove)
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)
        self.ui.btn_sort.clicked.connect(self.sort)
        self.ui.btn_exit.clicked.connect(self.exit)



    def loadStudents(self):
        self.ui.listWidget.addItems(["Hassan", 'Amr', 'Basma'])
        #self.ui.listWidget.setCurrentRow(1) # second item is initially selected

    def add(self):
        current_index = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "New Item", "Item Name")
        if text and ok is not None:
            self.ui.listWidget.insertItem(current_index,text)
        else: # if no item is selected, insert at the beginning
            self.ui.listWidget.insertItem(0, text)

    def edit(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)

        # currentRow() returns 0 by default if nothing selected, so we check using selectedIndexes
        selected_items = self.ui.listWidget.selectedIndexes()

        if len(selected_items) != 0:

            text, ok = QInputDialog.getText(self, "Edit Item", "New Item Name")
            if text and ok is not None:
                item.setText(text)
        else:  # warning message
            QMessageBox.warning(self, "Error", "No item is selected")

    def remove(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)

        # currentRow() returns 0 by default if nothing selected, so we check using selectedIndexes
        selected_items = self.ui.listWidget.selectedIndexes()
        if len(selected_items) != 0:
            box_answer = QMessageBox.question(self, 'Remove Item', 'Do you want to remove this item?',
                                 QMessageBox.Yes | QMessageBox.No)#, QMessageBox.No)
            if box_answer == QMessageBox.Yes:
                here = self.ui.listWidget.takeItem(current_index)
        else: # warning message
            QMessageBox.warning(self,"Error", "No item is selected")

    def up(self):
        current_index = self.ui.listWidget.currentRow()
        if current_index > 0:
            # store in item, then delete it
            item = self.ui.listWidget.takeItem(current_index)
            # re-insert at the selected index
            self.ui.listWidget.insertItem(current_index -1, item)
            # select the shifted item to allow user multiple ups without re-selecting the item
            self.ui.listWidget.setCurrentItem(item)

    def down(self):
        current_index = self.ui.listWidget.currentRow()
        # check if index is at most right before the last element
        if current_index < self.ui.listWidget.count() - 1:
            # store in item, then delete it
            item = self.ui.listWidget.takeItem(current_index)
            # re-insert at the selected index
            self.ui.listWidget.insertItem(current_index + 1, item)
            # select the shifted item to allow user multiple ups without re-selecting the item
            self.ui.listWidget.setCurrentItem(item)

    def sort(self):
        # sorting by initials
        self.ui.listWidget.sortItems()

    def exit(self):
        question = QMessageBox.question(self, "Exit", "Do You want to Exit?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if question == QMessageBox.Yes:
            quit()

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()


