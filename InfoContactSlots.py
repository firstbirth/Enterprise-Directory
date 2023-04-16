from InfoContact import Ui_w_InfoContact
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
import mysql.connector

class InfoContacts(QtWidgets.QMainWindow, Ui_w_InfoContact):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.btn_GetData.clicked.connect(self.GetContactInfo)
    
    
    def GetContactInfo(self):
        infoFromDB = self.SendQueryAllEnterprises(self.DBINST)
        self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.rowcount}",3000)
    
    
    def SendQueryAllEnterprises(self,dbInstance):
        cursor = dbInstance.cursor()
        cursor.execute("SELECT * FROM test.contacts;")
        columns = []
        row = cursor.fetchone()
        rowCount = 0
        #вычисление количества строк из запроса и создание массива со значениями для ячеек
        while row is not None:
             columns.append(QTableWidgetItem(str(row[0])))
             columns.append(QTableWidgetItem(row[1]))
             columns.append(QTableWidgetItem(row[2]))
             columns.append(QTableWidgetItem(row[3]))
             columns.append(QTableWidgetItem(row[4]))
             rowCount+=1
             print(row)
             row=cursor.fetchone()
        cursor.close()
        self.tw_ViewContacts.setRowCount(rowCount)
        row = 0
        col = 0
        for j in columns:
            if col==5:
                col=0
                row+=1
            self.tw_ViewContacts.setItem(row,col,j)
            col+=1

        print("Успешно выведено")
        return cursor