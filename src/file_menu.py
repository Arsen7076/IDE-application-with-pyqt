from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *


class File_menu:
    def __init__(self, menubar):
        self.file_menu = menubar.addMenu("&File")


        # **************************************************************************************************
        # ******                                 New File                                        ***********
        # **************************************************************************************************
        self.new_file = self.file_menu.addAction("New File")
        self.new_file.setShortcut(QKeySequence.New)

        # **************************************************************************************************
        # ******                                 Open File                                       ***********
        # **************************************************************************************************
        self.open_file = self.file_menu.addAction("Open File")
        self.open_file.setShortcut(QKeySequence.Open)
        self.file_menu.addSeparator()

        # **************************************************************************************************
        # ******                                    Save                                         ***********
        # **************************************************************************************************
       
        self.save = self.file_menu.addAction("Save")
        self.save.setShortcut(QKeySequence.Save)

        # **************************************************************************************************
        # ******                                    Save as                                      ***********
        # **************************************************************************************************

        save_as = self.file_menu.addAction("Save AS")
        save_as.setShortcut(QKeySequence.SaveAs)
        # **************************************************************************************************
        # ******                                    Metaxx                                       ***********
        # **************************************************************************************************


        self.file_menu.addSeparator()
        self.metax_save = self.file_menu.addAction("Save in Metax")
        self.metax_get = self.file_menu.addAction("Get in Metax")
        self.metax_update = self.file_menu.addAction("Update")
        self.metax_save.setShortcut(Qt.CTRL + Qt.Key_M + Qt.Key_S)
        self.metax_get.setShortcut(Qt.CTRL + Qt.Key_M + Qt.Key_O)
        self.metax_update.setShortcut(QKeySequence.Print)
        self.file_menu.addSeparator()
        self.close_file = self.file_menu.addAction("Close File")

        # **************************************************************************************************
        # ******                                 Close File                                      ***********
        # **************************************************************************************************

        self.close_file.setShortcut(QKeySequence.Close)

        # **************************************************************************************************
        # ******                                 Close Editor                                    ***********
        # **************************************************************************************************

        self.close_editor = self.file_menu.addAction("Close Editor")
        self.close_editor.setShortcut(Qt.ALT + Qt.Key_Q)

        # **************************************************************************************************
        # ******                                 Create Terminal Menu                            ***********
        # **************************************************************************************************

        self.terminalMenu = menubar.addMenu("&Terminal")
        self.newTerm = self.terminalMenu.addAction("New Terminal")
        self.newTerm.setShortcut(Qt.CTRL + Qt.Key_T)
        self.clossTerm = self.terminalMenu.addAction("Close Terminal")
        self.clossTerm.setShortcut(Qt.CTRL + Qt.Key_T + Qt.SHIFT)

        # **************************************************************************************************
        # ******                                 Make Help                                       ***********
        # **************************************************************************************************

        self.help = menubar.addAction("Help")

        self.help.setShortcut(QKeySequence.HelpContents)

    def about(self):
        ms = QMessageBox()
        ms.setWindowTitle("About Author")
        ms.setText("This program  made in PONTEM LAB\nAddress: Shrjancik Tunel 7/1\nAuthors`\nTsolak Musikyan\n"
                   "Arsen Margaryan\nHayk Vardazaryan\nVahe Sedrakyan\nDavit Chaloyan\nXachik Hoxinyan")
