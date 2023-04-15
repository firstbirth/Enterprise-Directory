import sys
from PySide6 import QtWidgets as qtw

from AuthWindowSlots import AuthWindow

DATABASE_INSTANCE = None

if __name__ =="__main__":
    app = qtw.QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    app.exec()
    DATABASE_INSTANCE = window.DBINST
    print("ok")
