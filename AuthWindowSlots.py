from AuthWindow import Ui_Authorization
from PySide6 import QtWidgets
import mysql.connector
from MainWindowSlots import MainWindow


class AuthWindow(QtWidgets.QDialog, Ui_Authorization):
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.lineEdit.setFocus()
            self.pb_cancel.clicked.connect(self.close)
            self.pb_ok.clicked.connect(self.ConnectToDB)
            self.DBINST = None
    
    
    def ConnectToDB(self):
        try:
            dbConnection = mysql.connector.connect(
                host="localhost",
                user=self.lineEdit.text(),
                passwd=self.lineEdit_2.text())
            
            print("Sucessfully connected to DB username: {0} \nConnection ID: {1}".format(
                dbConnection._user, dbConnection.connection_id))
            self.lb_message.setText("Соединение с БД установлено!")
            self.DBINST =  dbConnection
            self.close()

            second_window = MainWindow(DBINSTANCE=self.DBINST)
            second_window.show()
            second_window.exec()
            
        except mysql.connector.Error as errorMessage:
            self.lb_message.setText("Error has occurred: {}".format(errorMessage.msg))
 