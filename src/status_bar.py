from PyQt5 import QtWidgets 
from PyQt5 import QtCore
from PyQt5.QtGui import QKeySequence

class Status_bar:
    def __init__(self, object):
        self.status_bar = QtWidgets.QStatusBar(object)
        self.status_bar.setObjectName("statusbar")