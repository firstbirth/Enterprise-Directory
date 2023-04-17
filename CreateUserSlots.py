from CreateUser import Ui_CreateUser
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
import mysql.connector


class CreateUser(QtWidgets.QMainWindow, Ui_CreateUser):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.btn_CreateUser.clicked.connect(self.CreateUser)
            self.User.setChecked(True)
    
    def CreateUser(self):
        cursor = self.DBINST.cursor()
        if self.User.isChecked:
             
            cursor.execute(f"USE test;\
                            CREATE USER '{self.le_Login.text()}'@'localhost' IDENTIFIED BY '{self.le_Password.text()}';\
                            GRANT SELECT ON test.* TO '{self.le_Login.text()}'@'localhost';")
            self.statusBar().showMessage(f"Создан новый пользователь: {self.le_Login.text()}",3000)
        
        elif self.Admin.isChecked:
            cursor.execute(f"USE test;\
                            CREATE USER '{self.le_Login.text()}'@'localhost' IDENTIFIED BY '{self.le_Password.text()}';\
                            GRANT DBA ON test.* TO '{self.le_Login.text()}'@'localhost';")
            self.statusBar().showMessage(f"Создан новый администратор: {self.le_Login.text()}",3000)
        
