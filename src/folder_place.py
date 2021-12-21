from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtWidgets import *


class Folder_place(QFileSystemModel):

    def __init__(self):
        super().__init__()
        self.treeView = QtWidgets.QTreeView()
        self.treeView.setStyleSheet("QTreeView{background: #191c22; color:white}\n"
                                    "\n"
                                    "QTreeView::item::hover{border-left:2px solid white; background:#5a616f}\n"
                                    "QTreeView::item::selected{border-left:3px solid  rgb(0, 208, 255);color:white}\n"
                                    "QTreeView::item {border-left: 1px solid #5a616f}")
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropOverwriteMode(True)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        self.exp = QFileSystemModel()
        self.exp.setRootPath((QDir.rootPath()))
        self.path = "/home"  # // PFAD FUER DEN EXPLORER
        self.treeView.setModel(self.exp)
        self.treeView.setIconSize(QSize(20, 20))
        self.treeView.setRootIndex(self.exp.index(self.path))
        self.treeView.setSortingEnabled(True)
        for i in range(1, self.treeView.model().columnCount()):
            self.treeView.header().hideSection(i)
        self.exp.setReadOnly(False)
        self.treeView.setSelectionMode(self.treeView.SingleSelection)
        self.treeView.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeView.setDragEnabled(True)
        self.treeView.setAcceptDrops(True)
        self.treeView.setDropIndicatorShown(True)

        # **************************************************************************************************
        # ******                                 Get Folder Name                                 ***********
        # **************************************************************************************************
    def getFolderName(self):
        txt, ok = QInputDialog.getText(self, "Folder", "Name", QLineEdit.Normal)
        if txt and ok != "":
            return txt

        # **************************************************************************************************
        # ******                                    Get Path                                     ***********
        # **************************************************************************************************


    def getPath(self):
        indexItem = self.exp.index(self.treeView.currentIndex().row(), 0, self.treeView.currentIndex().parent())
        filepath = self.exp.filePath(indexItem)
        return filepath

        # **************************************************************************************************
        # ******                                    Open File                                    ***********
        # **************************************************************************************************

    def getDirectory(self):
        indexItem = self.treeView.currentIndex().parent()
        return self.exp.filePath(indexItem)

        # **************************************************************************************************
        # ******                                    Name return                                  ***********
        # **************************************************************************************************
    def getFileItem(self):
        indexItem = self.exp.index(self.treeView.currentIndex().row(), 0, self.treeView.currentIndex().parent())
        return self.exp.fileName(indexItem)



    def treeMedia_doubleClicked(self, index):
        item = self.treeView.model().item(index.row(), index.column())
        strData = item.data(0).toPyObject()
        print('' + str(strData))
