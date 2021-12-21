import sys
import os
import metax_run

from PyQt5 import QtWidgets
from first_page import Ui_MainWindow1
from second_page import Ui_MainWindow


# **************************************************************************************************
# ******                              Run MEtax IN your pc                               ***********
# **************************************************************************************************

metax_run.run_metax()
# **************************************************************************************************
# ******                                    Start App                                    ***********
# **************************************************************************************************

app = QtWidgets.QApplication(sys.argv)
app.aboutToQuit.connect(lambda: kill_metax())
first = QtWidgets.QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(first)
first.show()


def openSecond():
    global second_page
    second_page = QtWidgets.QMainWindow()
    second_page.setObjectName("Metax IDE")
    Ui_MainWindow(second_page)
    # second_page.lastWindowclosed
    # app.aboutToQuit.connect(myExitHandler
    first.close()
    second_page.show()


def openfile():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)

    first.close()
    MainWindow.show()
    ui.open_file(True)
def kill_metax():
    os.system("pkill metax")

ui.newProject.clicked.connect(openSecond)
ui.openProject.clicked.connect(openfile)
sys.exit(app.exec_())
