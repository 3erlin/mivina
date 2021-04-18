import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui     import *
#from PyQt5.QtCore    import *
from PyQt5 import QtCore, QtGui, QtWidgets
#from mainwindow_ui import Ui_MainWindow
#from dialog_ui     import Ui_Dialog
#from PySide2.QtWidgets import *
#from PySide2.QtGui     import *
#from PySide2.QtCore    import *
#from PyQt5.QtWidgets import QApplication, QMainWindow
from kark import Ui_MainWindow
from reg  import Ui_MainWindow2
#from desk import Ui_MainWindow1

class map(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(centralWidget)
        gridLayout.addWidget(self.ui.label, 1, 0)
        gridLayout.addWidget(self.ui.label_3, 0, 2)
        gridLayout.addWidget(self.ui.label_2, 0, 0)
        gridLayout.addWidget(self.ui.label_4, 1, 2)
        gridLayout.addWidget(self.ui.pushButton,1 , 2)
        gridLayout.addWidget(self.ui.pushButton_2, 1, 0)

    def maps(self):
        self.hide()
        self.maaps=map()
        self.maaps.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

