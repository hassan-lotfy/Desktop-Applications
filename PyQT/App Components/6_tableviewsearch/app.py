from PyQt5 import QtWidgets, QtGui, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from interface import Ui_MainWindow  # Import the generated UI class
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Load the UI

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configure table scrolling behavior for smoother scrolling
        self.ui.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ui.tableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        # set scrolling step when < > arrow is pressed
        horizontal_scrollbar = self.ui.tableView.horizontalScrollBar()
        horizontal_scrollbar.setSingleStep(2)

        # Create a model
        self.model = QStandardItemModel() # fill data in this model then put it in the table
        # Initialize and set up the model for the table view
        self.setup_table_data()
        # table UI edit
        self.setup_table_view()

        self.ui.txt_search.addAction(QIcon("searchhh.ico"), QtWidgets.QLineEdit.LeadingPosition)

        # filter values when text changes inside search lable
        self.ui.txt_search.textChanged.connect(self.filter)
        # list to store filtered rows indexes (hidden) to show them after search ends
        self.hidden_rows = []

    # function: fill the model with data, bend it to the table
    def setup_table_data(self):

        # Set column headers
        self.model.setHorizontalHeaderLabels(["Name", "Age", "Country"])
        #model.setVerticalHeaderLabels(["Number1", "Number2, "Number3"])

        data = [["Alice", "25", "USA"], ["Hoda", "22", "Egypt"],["Hassan", "23", "Greek"],["Ramy", "35", "Syria"]
                ,["Basma", "20", "Croatia"],["Esraa", "25", "UK"]]

        # Populate the model with data
        for i, list in enumerate(data):
            for j, element in enumerate(list):
                self.model.setItem(i,j,QStandardItem(element))

        # Attach the model to the table view
        self.ui.tableView.setModel(self.model)


    # function for cells coloring
    def setup_table_view(self):
        pass
        # 1 row in dark grey, and the following in light grey
        for col in range(self.model.columnCount()):
            for row in range(self.model.rowCount()):
                item = self.model.item(row, col)
                if row % 2 == 0:  # Alternate column coloring
                    item.setBackground(QtGui.QColor("#eeeeee"))
                else:
                    item.setBackground(QtGui.QColor("#dadada"))

    # function to filter table based on search
    def filter(self):

        # first show the hidden elements from previous search
        for row in self.hidden_rows:
            self.ui.tableView.showRow(row)

        input_text = self.ui.txt_search.text()
        # loop on the table to find the data, if found in any cell keep the row, else hide the row
        for row in range(self.model.rowCount()):
            text_found_flag = False
            # search for the text in the row
            for col in range(self.model.columnCount()):
                item = self.model.item(row, col)
                cell_text = item.text()
                # if text is found, highlight and set flag to keep the row
                if input_text.lower() in cell_text.lower():

                    text_found_flag = True
            # if not found in the row, hide the row and store it the hidden rows list
            if text_found_flag == False:
                self.ui.tableView.hideRow(row)
                self.hidden_rows.append(row)


# Main application execution
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())