from InfoIndustry import Ui_w_InfoIndustry
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
import mysql.connector

class InfoIndustry(QtWidgets.QMainWindow, Ui_w_InfoIndustry):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.tw_ViewIndustry
            self.btn_GetData.clicked.connect(self.GetEnterpriseInfo)
   
    def GetEnterpriseInfo(self):
        infoFromDB = self.SendQueryAllEnterprises(self.DBINST)
      
        self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.rowcount}",3000)
    
    
    def SendQueryAllEnterprises(self,dbInstance):
        
        cursor = dbInstance.cursor()
        cursor.execute("SELECT * FROM test.industry;")
        columns = []
        row = cursor.fetchone()
        rowCount = 0
        #вычисление количества строк из запроса и создание массива со значениями для ячеек
        while row is not None:
             columns.append(QTableWidgetItem(str(row[0])))
             columns.append(QTableWidgetItem(row[1]))
             rowCount+=1
             print(row)
             row=cursor.fetchone()
        cursor.close()
        self.tw_ViewIndustry.setRowCount(rowCount)
        row = 0
        col = 0
        for j in columns:
            if col==2:
                col=0
                row+=1
            self.tw_ViewIndustry.setItem(row,col,j)
            col+=1

        print("Успешно выведено")
             
        # print("curs2", curs2)
        # print("cursor", cursor)
        # for pke in cursor: 
        #     print(cursor.rowcount)
        
        # print(len(infoFromDB))
        # for i in range(cursor.rowcount*2+1):
        #      columns.append(QTableWidgetItem())
    
        # self.tw_ViewIndustry.setRowCount(cursor.rowcount)
        
        #установка значений каждому объекту QTableWidget
        
        # row = 0
        # col = 0

        # while row<=7:
        #     counter=0
        #     if col ==2:
        #         col = 0
        #         row +=1
        #     self.tw_ViewIndustry.setItem()
        #     self.tw_ViewIndustry.setItem(row,col,columns[counter])
        #     col+=1



        # row = 0
        # col = 0
        # for FirstColumb1 in cursor: #(4, 'Нефтегазовая промышленность')
        #     for item in FirstColumb1: #4
        #          columns[]
        #          self.tw_ViewIndustry.setItem(0,1,__qtablevidgetitem)
        #     print("{}".format(FirstColumb1))
        
        # self.tw_ViewIndustry.
        return cursor
