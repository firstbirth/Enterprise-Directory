from MainWindow import Ui_MainWindow
from PySide6 import QtWidgets
import mysql.connector
import AuthWindowSlots
import InfoEnterpriseSlots
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, DBINSTANCE):
        super().__init__()
        self.setupUi(self)
        self.act_Exit.triggered.connect(self.close)
        self.act_ChangeUser.triggered.connect(self.ChangeUser)
        self.DBOBJ = DBINSTANCE
        self.act_FindEnterprise.triggered.connect(self.openview)

        
    def ChangeUser(self):
        self.DBOBJ.close()
        self.close()
        a = AuthWindowSlots.AuthWindow()
        a.show()
        a.exec()
        self.DBOBJ = a.DBINST

    def openview(self):
        a = InfoEnterpriseSlots.InfoEnterprise(DBINSTANCE=self.DBOBJ)
        a.show()
        a.exec()
    # def SendQuery(self):
    #     cursor = self.DBOBJ.cursor()
    #     cursor.execute("SELECT * FROM test.new_table;")
    #     for FirstColumb in cursor:
    #         print("{}".format(FirstColumb))

    #     # cursor.close()
    #     self.DBOBJ.close()