import json
import os
import runfile
from PyQt5.QtWidgets import QInputDialog, QWidget, QMessageBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        usr_path = os.path.expanduser('~')
        exe = 0o777
        os.chdir(usr_path)
        try:
            os.chdir("MetaxIDE")
        except os.error:
            print("Metax IDE node found")
            os.mkdir("MetaxIDE")
            os.chdir("MetaxIDE")

        metax_path = usr_path + "/MetaxIDE"
        os.chdir(metax_path)
        try:
            os.mkdir("json_file")
            os.chdir("json_file")
        except os.error:
            os.chdir("json_file")

        if os.path.exists(metax_path + "/json_file/json_file.json"):
            pass
        else:
            f = open("json_file.json", "w")
            user_name = usr_path[6:]
            x = {
                "user": str(user_name),
                "root": {
                    "new_project": {
                        "file": "56672071-cd23-439b-a9aa-a07dca933900"
                    }
                }
            }
            y = json.dumps(x)
            json.dump(x, f)
            f.close()

        # *****************************************************************
        self.path = os.path.expanduser("~") + "/MetaxIDE/json_file/json_file.json"

    def save(self, body):
        f = open("json_file.json", "r")
        test = json.load(f)
        self.opens_json = test
        self.prog_list = list(self.opens_json["root"].keys())
        text, ok = QInputDialog.getText(self, 'Input dialog', "Isert Project Name:\n" + str(self.prog_list))
        if ok:
            if text in self.prog_list:
                file_list = list(self.opens_json["root"][text].keys())
                files, ok = QInputDialog.getText(self, "File List", "Insert File Name\n" + str(file_list))
                if ok:
                    if files in file_list:
                        uuid = self.opens_json["root"][text][files]
                        runfile.update_file(body, uuid)
                    else:
                        uuid = runfile.save_file(body)
                        new_files = {files: uuid}
                        self.opens_json["root"][text].update(new_files)
                        f = open("json_file.json", "w")
                        json.dump(self.opens_json, f)
                        f.close()
                        
            else:

                files, ok = QInputDialog.getText(self, "New File", "Insert New File name\n")
                uuid = runfile.save_file(body)
                new_files = {files: uuid}
                new_prog = {text: new_files}
                self.opens_json["root"].update(new_prog)
                f = open("json_file.json", "w")
                json.dump(self.opens_json, f)
                f.close()
    def open(self):
        f = open("json_file.json", "r")
        opens_json1 = json.load(f)
        prog_list2 = list(opens_json1["root"].keys())
        text, ok = QInputDialog.getText(self, 'input dialog', str(prog_list2))
        if ok:
            if text in prog_list2:
                file_list = list(opens_json1["root"][text].keys())
                files, ok = QInputDialog.getText(self, "File List", str(file_list))
                if ok:
                    if files in file_list:
                        uuid = opens_json1["root"][text][files]
                        text = runfile.get(uuid)
                        return text
                    else:
                        nod_founnd = QMessageBox()
                        nod_founnd.setWindowTitle("Files")
                        nod_founnd.setText("Error 404 File Not Found\n")
            else:
                print("Error")