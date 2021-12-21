import os
from PyQt5 import QtWidgets, QtCore


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.terminal)
        user = os.path.expanduser("~")

        try:
            os.chdir(user)
            os.chdir("MetaxIDE")
            print("sdds")
        except os.error:
            print("Plus")
            os.chdir(user)
            os.mkdir("MetaxIDE")
            os.chdir("MetaxIDE")

        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setFixedSize(1500, 250)
        self.setContentsMargins(0, 0, 0, 0)