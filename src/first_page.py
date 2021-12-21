from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
import os

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(71, 89, 88);\n"
                                 "border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newProject = QtWidgets.QPushButton(self.centralwidget)
        self.newProject.setGeometry(QtCore.QRect(260, 358, 281, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.newProject.setFont(font)
        self.newProject.setStyleSheet("background-color: rgb(13, 241, 227);\n"
"border-radius: 10px;")
        self.newProject.setObjectName("newProject")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 100, 211, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Images/metaxIde.png"))
        self.label.setObjectName("label")
        self.openProject = QtWidgets.QPushButton(self.centralwidget)
        self.openProject.setGeometry(QtCore.QRect(260, 430, 281, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.openProject.setFont(font)
        self.openProject.setStyleSheet("background-color: rgb(13, 241, 227);\n"
"border-radius: 10px;")
        self.openProject.setObjectName("openProject")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 530, 161, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Images/pontem.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Metax IDE", "Metax IDE"))
        self.newProject.setText(_translate("MainWindow", "NEW PROJECT"))
        self.openProject.setText(_translate("MainWindow", "OPEN PROJECT"))
