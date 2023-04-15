# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerWCQJCS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"multiply.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        icon1 = QIcon()
        icon1.addFile(u"correct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiontest.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuopen = QMenu(self.menubar)
        self.menuopen.setObjectName(u"menuopen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menuopen.addAction(self.actiontest)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.menuopen.setTitle(QCoreApplication.translate("MainWindow", u"open", None))
    # retranslateUi
    

