
import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *


class Window1(QWidget):
    def setupUi(self, Window1):
        Window1.setObjectName("MainWindow")
        Window1.resize(400, 500)
        Window1.setStyleSheet("background-color:gainsboro;")
        self.centralwidget = QWidget(Window1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 201, 201))
        self.label_2.setStyleSheet("QPushButton{\n"
                                   "background-color:222e;\n"
                                   "border:30;\n"
                                   "}\n"
                                   "QPushButton::{\n"
                                   "background-color:black;\n"
                                   "}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("reg1.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 201, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("reg2.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 2, 201, 201))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:222e;\n"
                                      "border:30;\n"
                                      "}\n"
                                      "QPushButton::pressed{\n"
                                      "background-color:black;\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 300, 201, 201))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color:222e;\n"
                                        "border:30;\n"
                                        "}\n"
                                        "QPushButton::pressed{\n"
                                        "background-color:black;\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 200, 141, 20))
        font = QtGui.QFont()
        font.setFamily("OpenDyslexicAlta")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 270, 71, 17))
        font = QtGui.QFont()
        font.setFamily("OpenDyslexicAlta")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 381, 20))
        font = QtGui.QFont()
        font.setFamily("OpenDyslexicAlta")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window1)
        QtCore.QMetaObject.connectSlotsByName(Window1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Администратор"))
        self.label_4.setText(_translate("MainWindow", "Клиент"))
        self.label_5.setText(_translate("MainWindow", "Авторизация                  пользователя"))


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def show_window_1(self):
        self.w1 = Window1()

        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    sys.exit(app.exec_())