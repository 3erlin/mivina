# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
#from PySide2 import QtCore, QtGui
#from PySide2.QtWidgets import *
#from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1010, 0, 271, 721))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 180, 70, 70))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:22e2;\n"
                                      "border:30;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "background-color:222e\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.to_click)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 390, 70, 70))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
            "background-color:222e;\n"
            "border:30;\n"
            "}\n"
            "\n"
            "QPushButton::pressed{\n"
            "background-color:222e\n"
            "}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
     #   MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_5.clicked.connect(self.on_click)



        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.pushButton_6.clicked.connect(self.dostav)


    def on_click(self):
        img = Image.open('2.png')
        img.show()
        time.sleep(1)
        self.label.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("3.png"))
        self.label.setObjectName("label")
        self.label.show()
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 180, 70, 70))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "background-color:222e;\n"
                                        "border:30;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "background-color:222e\n"
                                        "}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.show()
        self.pushButton_7.clicked.connect(self.to_click)
    def to_click(self):
        img = Image.open('4.png')
        img.show()
        time.sleep(1)
        self.label.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("5.png"))
        self.label.setObjectName("label")
        self.label.show()
   # def dostav(self):


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


''''def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    s = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main() '''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time
from PIL import Image
#from PySide2 import QtCore, QtGui
#from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1010, 0, 271, 721))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 180, 70, 70))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:22e2;\n"
                                      "border:30;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "background-color:222e\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.to_click)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 390, 70, 70))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
            "background-color:222e;\n"
            "border:30;\n"
            "}\n"
            "\n"
            "QPushButton::pressed{\n"
            "background-color:222e\n"
            "}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
      #  MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_5.clicked.connect(self.on_click)



        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.pushButton_6.clicked.connect(self.dostav)


    def on_click(self):
        img = Image.open('2.png')
        img.show()
        time.sleep(1)
        self.label.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("3.png"))
        self.label.setObjectName("label")
        self.label.show()
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 180, 70, 70))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "background-color:222e;\n"
                                        "border:30;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "background-color:222e\n"
                                        "}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.show()
        self.pushButton_7.clicked.connect(self.to_click)
    def to_click(self):
        img = Image.open('4.png')
        img.show()
        time.sleep(1)
        self.label.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("5.png"))
        self.label.setObjectName("label")
        self.label.show()
   # def dostav(self):


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


'''def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    s = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()'''''
