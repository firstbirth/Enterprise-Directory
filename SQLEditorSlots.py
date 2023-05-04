from SQLEditor import Ui_w_SQLEditor
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem, QPushButton
import mysql.connector


class SqlEditor(QtWidgets.QMainWindow, Ui_w_SQLEditor):
    def __init__(self, DBINSTANCE):
        super().__init__()
        self.setupUi(self)
        self.DBINST = DBINSTANCE
        self.cm_DB.activated.connect(self.FillComboFromDB)
        self.cm_Rows.activated.connect(self.GetSelectedID)
        self.btn_DeleteData.clicked.connect(self.DeleteDataDB)
        self.btn_AddData.clicked.connect(self.AddDataDB)
        self.rbtn_Insert.clicked.connect(self.OpenViewAdd)
        self.rbtn_Delete.clicked.connect(self.OpenViewDelete)
        self.lb_ID.hide()
        self.cm_Rows.hide()
        self.lb_CityName.hide()
        self.le_CityName.hide()
        self.btn_AddData.hide()
        self.btn_DeleteData.hide()

    def AddDataDB(self):
        cursor = self.DBINST.cursor()
        cursor.execute(f"INSERT INTO test.city (City_Name) VALUES('{self.le_CityName.text()}')")
        self.DBINST.commit()
        self.statusBar().showMessage("Город успешно добавлен в базу!",3000)
        self.le_CityName.clear()
    def OpenViewDelete(self):
        self.lb_CityName.hide()
        self.le_CityName.hide()
        self.btn_AddData.hide()
        self.lb_ID.show()
        self.cm_Rows.show()  
        self.btn_DeleteData.show()

    def OpenViewAdd(self):
        self.lb_ID.hide()
        self.cm_Rows.hide()  
        self.btn_DeleteData.hide()
        self.lb_CityName.show()
        self.le_CityName.show()
        self.btn_AddData.show()

    def FillComboFromDB(self):
        match self.cm_DB.currentText():
            case "city":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT * FROM test.city;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()
            case "industry":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT * FROM test.industry;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()
            case "enterprises":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT Enterprise_ID, Enterprise_Name FROM test.enterprises;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()
            case "contacts":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT Contact_ID, Email FROM test.contacts;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()
            case "managers":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT Manager_ID, Manager_Name FROM test.managers;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()
            case "services":
                self.cm_Rows.clear()
                cursor = self.DBINST.cursor()
                cursor.execute("SELECT * FROM test.services;")
                IDs = cursor.fetchall()
                for i in IDs:
                    self.cm_Rows.addItem(f"{str(i[0])} - {i[1]}")
                cursor.close()

        print(self.cm_Rows.currentText())            
    
    def GetSelectedID(self):
        return self.cm_Rows.currentText().split(" ")[0]

    def DeleteDataDB(self):
        if self.rbtn_Delete.isChecked:
            ID = self.GetSelectedID()
            print(ID)
            cursor = self.DBINST.cursor()
            match self.cm_DB.currentText():
                case "city":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (CityCode_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                case "contacts":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (Contact_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                case "enterprises":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (Enterprise_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                case "industry":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (Industry_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                case "managers":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (Manager_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                case "services":
                    cursor.execute(f"DELETE FROM test.{self.cm_DB.currentText()} WHERE (Service_ID = {ID});")
                    self.statusBar().showMessage(f"Информация успешно удалена! ID: {ID}")
                    self.DBINST.commit()
                    cursor.close()
                
    # def CreateUser(self):
    #     cursor = self.DBINST.cursor()
    #     if self.User.isChecked:
             
    #         cursor.execute(f"USE test;\
    #                         CREATE USER '{self.le_Login.text()}'@'localhost' IDENTIFIED BY '{self.le_Password.text()}';\
    #                         GRANT SELECT ON test.* TO '{self.le_Login.text()}'@'localhost';")
    #         self.statusBar().showMessage(f"Создан новый пользователь: {self.le_Login.text()}",3000)
        
    #     elif self.Admin.isChecked:
    #         cursor.execute(f"USE test;\
    #                         CREATE USER '{self.le_Login.text()}'@'localhost' IDENTIFIED BY '{self.le_Password.text()}';\
    #                         GRANT DBA ON test.* TO '{self.le_Login.text()}'@'localhost';")
    #         self.statusBar().showMessage(f"Создан новый администратор: {self.le_Login.text()}",3000)
        
