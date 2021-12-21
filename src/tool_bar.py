from PyQt5 import QtWidgets, QtGui
import webbrowser

from PyQt5.QtWidgets import QLineEdit


class Tool_bar:
    def __init__(self, parent_object):
        self.tool_bar = QtWidgets.QToolBar(parent_object)
        self.tool_bar.setObjectName("toolBar")
        self.tool_bar.setStyleSheet("background-color: rgb(40, 40, 40);")

        # **************************************************************************************************
        # ******                                 Google Search                                   ***********
        # **************************************************************************************************

        self.layout = QLineEdit()

        self.tool_bar.addWidget(self.layout)
        self.tool_bar.addSeparator()
        self.google = self.tool_bar.addAction("Google Search")
        self.layout.setFixedWidth(250)
        self.layout.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.google.triggered.connect(lambda: self.google_search())
        self.tool_bar.addSeparator()

        # **************************************************************************************************
        # ******                                 Github Search                                   ***********
        # **************************************************************************************************


        self.layout2 = QLineEdit()
        self.layout2.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.tool_bar.addWidget(self.layout2)
        self.tool_bar.addSeparator()
        self.github = self.tool_bar.addAction("Git search")
        self.layout2.setFixedWidth(250)
        self.github.triggered.connect(lambda: self.git_find())

    def google_search(self):
        query = self.layout.text()
        webbrowser.open("https://www.google.com/search?q=" + query)

    def git_find(self):
        query = self.layout2.text()
        webbrowser.open("https://github.com/search?q=" + query)
