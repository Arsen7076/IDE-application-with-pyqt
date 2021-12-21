import sys

from terminal import *
from make_json import Example
from code_edit import *

from file_menu import File_menu
from folder_place import Folder_place
from tool_bar import Tool_bar


def close_editor():
    close = QtWidgets.QMessageBox.question(None, "QUIT?", "Are you sure want to STOP and EXIT?",
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if close == QtWidgets.QMessageBox.Yes:
        os.system("pkill metax")
        sys.exit()
    else:
        pass

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        MainWindow.setObjectName("Metax IDE")
        MainWindow.showMaximized()
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout_2.setObjectName("verticalLayout_2")

        # **************************************************************************************************
        # ******                                 Code editor text editor                         **********
        # **************************************************************************************************
        self.code_edit = CodeEditor()
        # self.term = EmbTerminal()

        self.code_tabs = QtWidgets.QTabWidget()
        self.code_tabs.addTab(self.code_edit, "New")
        # self.code_tabs.addTab(self.term, "New")
        self.code_list = [self.code_edit]
        self.vertical_layout_2.addWidget(self.code_tabs)

        # **************************************************************************************************
        # ******                                 Menu Bar and functions                          ***********
        # **************************************************************************************************

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("Menu Bar")
        self.menubar.setVisible(True)
        self.menu_now = File_menu(self.menubar)

        #####
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        # self.statusbar = Status_bar(MainWindow)
        # MainWindow.addStatusBar(self.statusbar.status_bar)
        
        # **************************************************************************************************
        # ******                                 Toll Bar                                        **********
        # **************************************************************************************************

        
        self.toolBar = Tool_bar(MainWindow)

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar.tool_bar)
        # **************************************************************************************************
        # ******                                 Terminal                                          **********
        # **************************************************************************************************

        # Console
        self.new_dock = QDockWidget("Term")
        self.terminal = EmbTerminal()

        self.new_dock.setWidget(self.terminal)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.new_dock)

        # **************************************************************************************************
        # ******                                 Folder Place and show                            **********
        # **************************************************************************************************


        self.widget = QDockWidget("Folder place")
        self.tree = Folder_place()
        self.widget.setWidget(self.tree.treeView)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.widget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # **************************************************************************************************
        # ******                                        Metax                                    ***********
        # **************************************************************************************************

        self.metax = Example


        self.menu_now.open_file.triggered.connect(lambda: self.open_file(True))
        self.menu_now.save.triggered.connect(lambda: self.save_file())
        self.menu_now.new_file.triggered.connect(lambda: self.new_file())
        self.menu_now.help.triggered.connect(lambda: self.about())
        self.menu_now.close_file.triggered.connect(lambda: self.close_file())
        self.menu_now.close_editor.triggered.connect(lambda: close_editor())
        self.tree.treeView.doubleClicked.connect(self.on_item_clicked)
        self.menu_now.newTerm.triggered.connect(lambda: self.open_terminal())
        self.menu_now.clossTerm.triggered.connect(lambda: self.close_terminal())
        self.menu_now.metax_update.triggered.connect(lambda: self.metax_save())
        self.menu_now.metax_save.triggered.connect(lambda: self.metax_save())
        self.menu_now.metax_get.triggered.connect(lambda: self.metax_open())
        
        # **************************************************************************************************
        # ******                                 File Manu Functions                          **************
        # **************************************************************************************************

    def on_item_clicked(self):
        if self.tree.getFileItem().endswith(".py"):
            with open(self.tree.getPath(), "r") as f:
                txt = f.read()
                self.code_edit.clear()
                self.code_edit.insertPlainText(txt)
            with open(self.tree.getPath(), "w") as f:
                index = self.code_tabs.currentIndex()
                input = self.code_list[index].toPlainText()
                f.write(input)
        else:
            self.tree.treeView.update()


    def open_file(self, al):
        if al:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None, "OPen File", "",
                                                      "All Files (*);;Python Files (*.py)", options=options)
            if fileName:
                self.code_edit.clear()
                with open(fileName, "r") as f:
                    text = f.read()
                    new_page = CodeEditor()
                    new_page.insertPlainText(text)

                    self.code_tabs.addTab(new_page, fileName)
                    self.code_list.append(new_page)

    # **************************************************************************************************
    # ******                                 Terminal Manu Functions                          **********
    # **************************************************************************************************
    def ran(self):
        codes = self.code_edit.toPlainText()
        with open('runfile.py', 'w') as f:
            f.write(codes)
        result = "python3  runfile.py"

    def new_file(self):
        new_file = CodeEditor()
        self.code_tabs.addTab(new_file, "New File")
        self.code_list.append(new_file)

    def about(self):
        ms = QMessageBox()
        ms.setWindowTitle("Authors")
        ms.setText("This program  made in PONTEM LAB\nAddress: Shrjancik Tunel 7/1\nAuthors`\nTsolak Musikyan\n"
                   "Arsen Margaryan\nHayk Vardazaryan\nVahe Sedrakyan\nDavit Chaloyan\nXachik Hoxinyan")
        ms.exec_()

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "SAVE FILE", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            with open(fileName, "w") as f:
                text = self.code_edit.toPlainText()
                f.write(text)
                f.close()

    def close_file(self):
        if self.code_edit == "":
            pass
        else:
            asks = QMessageBox.question(None, "New File", "Change file without save or no",
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            if asks == QMessageBox.Yes:
                self.code_edit.clear()
            elif asks == QMessageBox.No:
                self.save_file()
            else:
                pass

            self.code_tabs.removeTab(self.code_tabs.currentIndex())

    def close_terminal(self):
        self.new_dock.hide()

    def open_terminal(self):
        self.new_dock.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Metax IDE", "Metax IDE"))
        self.menubar.setWindowTitle(_translate("MainWindow", "menubar"))

    def metax_save(self):

        text = self.code_edit.toPlainText()
        self.metax.save(self.metax(), text)

    def metax_open(self):
        text = self.metax.open(self.metax())
        self.code_edit.insertPlainText(text)
