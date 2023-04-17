from InfoEnterprise import Ui_w_InfoEnterprise
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem, QFileDialog
import mysql.connector
import csv


class InfoEnterprise(QtWidgets.QMainWindow, Ui_w_InfoEnterprise):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.tw_ViewEnterprise.rowCount
            self.btn_GetData.clicked.connect(self.GetEnterpriseInfo)
            self.btn_SaveData.clicked.connect(self.SaveToFile)
   

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

            self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.rowcount}",3000)
    
    def SendQueryAllEnterprises(self,dbInstance):

        cursor = dbInstance.cursor()

        cursor.execute("SELECT * FROM test.enterprises;")
        dbInstance.commit
        return cursor


    def SaveToFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV (*.csv)")
        if filename:
            self.CollectFromQTW(filename=filename)
        self.statusBar().showMessage(f"Данные успешно сохранены в файл: {filename}",3000)


    def CollectFromQTW(self,filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(self.tw_ViewEnterprise.rowCount()):
                row_data = []
                for column in range(self.tw_ViewEnterprise.columnCount()):
                    item = self.tw_ViewEnterprise.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)
    
