import sys
from PySide6.QtWidgets import QApplication
from AuthWindowSlots import AuthWindow
from MainWindowSlots import Ui_MainWindow

DATABASE_INSTANCE = None


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    app.exec()
    DATABASE_INSTANCE = window.DBINST

    print("ok")
