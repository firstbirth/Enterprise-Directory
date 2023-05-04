from CreateBackup import Ui_w_CreateBackup
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
import mysql.connector
from datetime import datetime
import subprocess, os


class ViewBackupMenu(QtWidgets.QMainWindow, Ui_w_CreateBackup):
    def __init__(self, DBINSTANCE):
        super().__init__()
        self.setupUi(self)
        self.DBINST = DBINSTANCE
        self.btn_CreateBckp.clicked.connect(self.SaveBackup)

    def SaveBackup(self):
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        backupFile = f"{self.le_BackupName.text()}_{now}.sql"
        backupPath = os.path.join(os.getcwd(), "backups")
        os.makedirs(backupPath, exist_ok=True)
        backupFile = os.path.join(backupPath, backupFile)
        password = self.le_Password.text()
        with open(backupFile, 'w') as f:
            subprocess.run(["mysqldump", "-u", "root", f"-p{password}", "test"], stdout=f, stdin=subprocess.PIPE)
        self.statusBar().showMessage(f"Резерваня копия '{self.le_BackupName.text()}' создана!",3000)

        
