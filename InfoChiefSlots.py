from InfoChief import Ui_w_InfoChief
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem, QFileDialog
import mysql.connector
import csv

class InfoChief(QtWidgets.QMainWindow, Ui_w_InfoChief):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.btn_GetData.clicked.connect(self.GetChiefInfo)
            self.btn_SaveData.clicked.connect(self.SaveToFile)
    
    def GetChiefInfo(self):
        infoFromDB = self.SendQueryAllEnterprises(self.DBINST)
        self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.rowcount}",3000)
    
    
    def SendQueryAllEnterprises(self,dbInstance):
        cursor = dbInstance.cursor()
        cursor.execute("SELECT * FROM test.managers;")
        columns = []
        row = cursor.fetchone()
        rowCount = 0
        #вычисление количества строк из запроса и создание массива со значениями для ячеек
        while row is not None:
             columns.append(QTableWidgetItem(str(row[0])))
             columns.append(QTableWidgetItem(row[1]))
             columns.append(QTableWidgetItem(row[2]))
             columns.append(QTableWidgetItem(str(row[3])))
             rowCount+=1
             print(row)
             row=cursor.fetchone()
        cursor.close()
        self.tw_ViewChieves.setRowCount(rowCount)
        row = 0
        col = 0
        for j in columns:
            if col==4:
                col=0
                row+=1
            self.tw_ViewChieves.setItem(row,col,j)
            col+=1

        print("Успешно выведено")
        return cursor
    
    def SaveToFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV (*.csv)")
        if filename:
            self.CollectFromQTW(filename=filename)
        self.statusBar().showMessage(f"Данные успешно сохранены в файл: {filename}",3000)


    def CollectFromQTW(self,filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(self.tw_ViewChieves.rowCount()):
                row_data = []
                for column in range(self.tw_ViewChieves.columnCount()):
                    item = self.tw_ViewChieves.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)