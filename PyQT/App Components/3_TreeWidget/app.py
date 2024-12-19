import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow
import xml.etree.ElementTree as ET

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # init UI from QT Designer converted file (interface.py)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ### method 1 to parse ###
        # # open the file ( will parse it as string)
        # file = open('my_xml.xml','r').read()
        ## get root element
        #root = ET.fromstring(xml_file)

        ### method 2 to parse ###
        # parse the xml file
        tree = ET.parse('my_xml.xml')
        # get root
        root = tree.getroot()

        # form the tree in the application UI from the parsed XML file
        self.form_tree(root)

        # link functions when any element is selected in the tree
        self.ui.treeWidget.itemClicked.connect(self.element_selected) # displaying selected item
        self.ui.treeWidget.itemClicked.connect(self.element_parents_path) # displaying parents' path


    # function to form the app UI from xml file
    def form_tree(self,root):

        # we can use more than 1 column (as table columns) but in our case we use only 1 for normal hierarchical tree
        self.ui.treeWidget.setColumnCount(1)

        # get main tag
        tree_parent = QtWidgets.QTreeWidgetItem([root.tag])
        # add the main tag on top of tree
        self.ui.treeWidget.addTopLevelItem(tree_parent)

        """ function takes the tree_parent in our treeWidget, and root (xml root) and
            add children to the tree_parent based on the xml content from root """
        def display_tree(tree_parent, element):
            # loop on children of parent
            for subelement in element:
                # add each child to our treeWidget
                child = QtWidgets.QTreeWidgetItem([subelement.tag])
                tree_parent.addChild(child)
                # check if the child has children inside or not, if yes loop on them also
                if len(subelement) > 0:
                    display_tree(child, subelement)

        # loop on parent's children and add them to our tree
        display_tree(tree_parent,root)

    # function to check the selected element inside the treeWidget and display it
    def element_selected(self):
        # get selected item from treeWidget
        item = self.ui.treeWidget.currentItem()
        # print the selected item (from column 0)
        print(item.text(0))

    # function to get parents path for selected item and display it
    def element_parents_path(self):
        # get selected item from treeWidget
        item = self.ui.treeWidget.currentItem()
        path = ""
        def get_parent(item, path):
        # check if current child has parent or not
            if item.parent() is None: # top parent is reached, return
                return path
            else: # there is parent, search upward parents
                path = item.parent().text(0) + r"/" +  path
                return get_parent(item.parent(), path)

        path = get_parent(item, path)
        print(path)




def app_create():
    app = QApplication(sys.argv)
    # windows indexes
    index = {}
    # add widget to contain multiple pages (login and register)
    widget = QtWidgets.QStackedWidget()
    # instantiate windows (pages)
    main_window = MainWindow()
    # add the pages to the widget
    widget.addWidget(main_window)
    index[main_window] = 0
    # set window size
    widget.setFixedWidth(680)
    widget.setFixedHeight(550)
    widget.show()
    sys.exit(app.exec_())

app_create()

