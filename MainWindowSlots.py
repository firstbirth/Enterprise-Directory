from MainWindow import Ui_MainWindow
from PySide6 import QtWidgets
import mysql.connector
import AuthWindowSlots
import InfoEnterpriseSlots
import InfoIndustrySlots
import InfoServiceSlots
import InfoCitySlots
import InfoContactSlots
import InfoChiefSlots

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, DBINSTANCE):
        super().__init__()
        self.setupUi(self)
        self.act_Exit.triggered.connect(self.close)
        self.act_ChangeUser.triggered.connect(self.ChangeUser)
        self.DBOBJ = DBINSTANCE
        self.act_FindEnterprise.triggered.connect(self.OpenView)
        self.act_InfoIndustry.triggered.connect(self.OpenIndustry)
        self.act_InfoServices.triggered.connect(self.OpenServices)
        self.act_InfoCity.triggered.connect(self.OpenCity)
        self.act_InfoContact.triggered.connect(self.OpenContacts)
        self.act_InfoChief.triggered.connect(self.OpenChieves)
        self.statusBar().showMessage(f"Успешная авторизация: {self.DBOBJ.user}",3000)

    def ChangeUser(self):
        self.DBOBJ.close()
        self.close()
        a = AuthWindowSlots.AuthWindow()
        a.show()
        a.exec()
        self.DBOBJ = a.DBINST

    def OpenView(self):
        a = InfoEnterpriseSlots.InfoEnterprise(DBINSTANCE=self.DBOBJ)
        print(self.DBOBJ)
        a.show()
        a.exec()

    def OpenIndustry(self):
        window = InfoIndustrySlots.InfoIndustry(DBINSTANCE=self.DBOBJ)
        print(self.DBOBJ)
        window.show()
        window.exec()

    def OpenServices(self):
        window = InfoServiceSlots.InfoService(DBINSTANCE=self.DBOBJ)
        window.show()
        window.exec()

    def OpenCity(self):
        window = InfoCitySlots.InfoService(DBINSTANCE=self.DBOBJ)
        window.show()
        window.exec()

    def OpenContacts(self):
        window = InfoContactSlots.InfoContacts(DBINSTANCE=self.DBOBJ)
        window.show()
        window.exec()

    def OpenChieves(self):
        window = InfoChiefSlots.InfoChief(DBINSTANCE=self.DBOBJ)
        window.show()
        window.exec()
    # def SendQuery(self):
    #     cursor = self.DBOBJ.cursor()
    #     cursor.execute("SELECT * FROM test.new_table;")
    #     for FirstColumb in cursor:
    #         print("{}".format(FirstColumb))

    #     # cursor.close()
    #     self.DBOBJ.close()