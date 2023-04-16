# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MWlvXslC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 738)
        MainWindow.setMinimumSize(QSize(847, 628))
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u" #centralwidget{\n"
"background-color:#0D1B2A;\n"
"}\n"
"\n"
"#act_ChangeUser{\n"
"	background-color:blue;\n"
"	color:white;\n"
"}\n"
"\n"
".QPushButton{\n"
"	background-color:#293241;\n"
"	color:#E0E1DD;\n"
"}\n"
"#statusbar{\n"
"background-color:#293241;\n"
"color:#E0E1DD;\n"
"}\n"
"\n"
"#menubar{\n"
"color:black;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#toolbar{\n"
"	\n"
"	background-color:black;\n"
"border:none;	\n"
"}\n"
"")
        self.act_Exit = QAction(MainWindow)
        self.act_Exit.setObjectName(u"act_Exit")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/multiply.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_Exit.setIcon(icon1)
        self.act_FindEnterprise = QAction(MainWindow)
        self.act_FindEnterprise.setObjectName(u"act_FindEnterprise")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_FindEnterprise.setIcon(icon2)
        self.act_ChangeUser = QAction(MainWindow)
        self.act_ChangeUser.setObjectName(u"act_ChangeUser")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/user-account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_ChangeUser.setIcon(icon3)
        self.act_AddUser = QAction(MainWindow)
        self.act_AddUser.setObjectName(u"act_AddUser")
        self.act_AddUser.setEnabled(True)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_AddUser.setIcon(icon4)
        self.act_AddUser.setVisible(True)
        self.act_DeleteUser = QAction(MainWindow)
        self.act_DeleteUser.setObjectName(u"act_DeleteUser")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/remove-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_DeleteUser.setIcon(icon5)
        self.act_InfoIndustry = QAction(MainWindow)
        self.act_InfoIndustry.setObjectName(u"act_InfoIndustry")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/industry.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_InfoIndustry.setIcon(icon6)
        self.act_InfoServices = QAction(MainWindow)
        self.act_InfoServices.setObjectName(u"act_InfoServices")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/repair-tool.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_InfoServices.setIcon(icon7)
        self.act_InfoCity = QAction(MainWindow)
        self.act_InfoCity.setObjectName(u"act_InfoCity")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_InfoCity.setIcon(icon8)
        self.act_InfoContact = QAction(MainWindow)
        self.act_InfoContact.setObjectName(u"act_InfoContact")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/notebook-of-contacts.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_InfoContact.setIcon(icon9)
        self.act_InfoChief = QAction(MainWindow)
        self.act_InfoChief.setObjectName(u"act_InfoChief")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/chief-executive-officer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_InfoChief.setIcon(icon10)
        self.act_Backup = QAction(MainWindow)
        self.act_Backup.setObjectName(u"act_Backup")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/cloud-storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_Backup.setIcon(icon11)
        self.act_CreateSQL = QAction(MainWindow)
        self.act_CreateSQL.setObjectName(u"act_CreateSQL")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.act_CreateSQL.setIcon(icon12)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(512, 512))
        self.label.setMouseTracking(False)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"#label{\n"
"	color:#415A77;\n"
"}")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setPixmap(QPixmap(u":/newPrefix/icons/myAsciiAr2t.png"))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setAutoFillBackground(True)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setEnabled(True)
        self.menu_3.setAcceptDrops(False)
        self.menu_3.setAutoFillBackground(False)
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menuSQL = QMenu(self.menubar)
        self.menuSQL.setObjectName(u"menuSQL")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setMaximumSize(QSize(16777215, 40))
        self.toolBar.setIconSize(QSize(20, 25))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menuSQL.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.act_ChangeUser)
        self.menu.addSeparator()
        self.menu.addAction(self.act_Exit)
        self.menu_2.addAction(self.act_FindEnterprise)
        self.menu_2.addAction(self.act_InfoIndustry)
        self.menu_2.addAction(self.act_InfoServices)
        self.menu_2.addAction(self.act_InfoCity)
        self.menu_2.addAction(self.act_InfoContact)
        self.menu_2.addAction(self.act_InfoChief)
        self.menu_3.addAction(self.act_AddUser)
        self.menu_3.addAction(self.act_DeleteUser)
        self.menu_5.addAction(self.act_Backup)
        self.menuSQL.addAction(self.act_CreateSQL)
        self.toolBar.addAction(self.act_FindEnterprise)
        self.toolBar.addAction(self.act_InfoIndustry)
        self.toolBar.addAction(self.act_InfoServices)
        self.toolBar.addAction(self.act_InfoCity)
        self.toolBar.addAction(self.act_InfoContact)
        self.toolBar.addAction(self.act_InfoChief)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_AddUser)
        self.toolBar.addAction(self.act_DeleteUser)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_CreateSQL)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_Backup)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.act_Exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.act_FindEnterprise.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0438", None))
        self.act_ChangeUser.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.act_AddUser.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.act_DeleteUser.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.act_InfoIndustry.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f\u0445", None))
        self.act_InfoServices.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0443\u0441\u043b\u0443\u0433\u0430\u0445", None))
        self.act_InfoCity.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0433\u043e\u0440\u043e\u0434\u0430\u0445", None))
        self.act_InfoContact.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430\u0445", None))
        self.act_InfoChief.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u0445", None))
        self.act_Backup.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.act_CreateSQL.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0440\u043e\u0441", None))
#if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u0430\u044f \u043a\u043e\u043f\u0438\u044f", None))
        self.menuSQL.setTitle(QCoreApplication.translate("MainWindow", u"SQL-\u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

