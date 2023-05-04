from DeleteUsers import Ui_w_DeleteUsers
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
import mysql.connector


class DeleteUsers(QtWidgets.QMainWindow, Ui_w_DeleteUsers):
    def __init__(self, DBINSTANCE):
        super().__init__()
        self.setupUi(self)
        self.DBINST = DBINSTANCE
        self.btn_DelUser.clicked.connect(self.DeleteUser)
        self.LoadComboBoxUsers(self.cmbx_Users)


    def LoadComboBoxUsers(self, qcombo):
        qcombo.clear()
        cursor = self.DBINST.cursor()
        cursor.execute("SELECT User FROM mysql.user WHERE User NOT LIKE 'mysql.%' AND User <> 'root';")
        IDs = cursor.fetchall()
        for i in IDs:
            qcombo.addItem(f"{str(i[0])}")
        cursor.close()
        return qcombo
        
    def DeleteUser(self):
        userName = self.cmbx_Users.currentText()
        cursor = self.DBINST.cursor()
        cursor.execute(f"DROP USER {userName}@'localhost';")
        self.DBINST.commit()
        cursor.close()
        self.statusBar().showMessage(f"Пользователь {userName} удален!",3000)
        self.LoadComboBoxUsers(self.cmbx_Users)

        
