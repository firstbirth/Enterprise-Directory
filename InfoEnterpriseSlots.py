from InfoEnterprise import Ui_w_InfoEnterprise
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
import mysql.connector

class InfoEnterprise(QtWidgets.QMainWindow, Ui_w_InfoEnterprise):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.tw_ViewEnterprise.rowCount
            self.btn_GetData.clicked.connect(self.GetEnterpriseInfo)
            
   

    def GetEnterpriseInfo(self):
        infoFromDB = self.SendQueryAllEnterprises(self.DBINST)
        columns = []
        for i in range(10):
             columns.append(QTableWidgetItem())
        # self.tw_ViewEnterprise.setRowCount(1)
        for FirstColumb in infoFromDB:
            i=0
            for Sec in FirstColumb:
                # print("{}".format(Sec))
                toCol = str(Sec)
                # print(FirstColumb[0])
                columns[i].setText(toCol)
                self.tw_ViewEnterprise.setItem(0,i, columns[i])
                # print(f"{toCol} должен быть добавлен в {i} колонку")
                i+=1

            self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.arraysize}")
    def SendQueryAllEnterprises(self,dbInstance):

        cursor = dbInstance.cursor()

        cursor.execute("SELECT * FROM test.enterprises;")
        dbInstance.commit
        return cursor

    
