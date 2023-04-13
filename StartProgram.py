import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtUiTools

from mainw import Ui_MainWindow


from AuthWindow import Ui_Form


class LoginForm(qtw.QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.setFocus()
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.setOK)
    
    def setOK(self):
        self.lb_message.setText("ok")

if __name__ =="__main__":
    app = qtw.QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())
    # app = qtw.QApplication(sys.argv)
    # window = QtUiTools.QUiLoader().load("au.ui")
    # window.show()
    # sys.exit(app.exec_())