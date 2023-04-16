# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoEnterprisemGNngU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_w_InfoEnterprise(object):
    def setupUi(self, w_InfoEnterprise):
        if not w_InfoEnterprise.objectName():
            w_InfoEnterprise.setObjectName(u"w_InfoEnterprise")
        w_InfoEnterprise.resize(1085, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_InfoEnterprise.sizePolicy().hasHeightForWidth())
        w_InfoEnterprise.setSizePolicy(sizePolicy)
        w_InfoEnterprise.setMinimumSize(QSize(1085, 0))
        w_InfoEnterprise.setMaximumSize(QSize(1085, 16777215))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        w_InfoEnterprise.setWindowIcon(icon)
        w_InfoEnterprise.setStyleSheet(u"#centralwidget{\n"
"background-color:#0D1B2A;\n"
"}\n"
"\n"
".QPushButton{\n"
"	background-color:#293241;\n"
"	color:#E0E1DD;\n"
"}\n"
"#statusbar{\n"
"background-color:#293241;\n"
"}\n"
"\n"
"#menubar{\n"
"color:black;\n"
"font-weight:bold;\n"
"}\n"
"\n"
".QGroupBox{\n"
"	color:#E0E1DD\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"	background-color:#1b263b;\n"
"}\n"
"\n"
"#statusbar{\n"
"	color:#E0E1DD;\n"
"}")
        self.centralwidget = QWidget(w_InfoEnterprise)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_ViewEnterprise = QTableWidget(self.groupBox)
        if (self.tw_ViewEnterprise.columnCount() < 9):
            self.tw_ViewEnterprise.setColumnCount(9)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/verified.png", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        __qtablewidgetitem.setIcon(icon1);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/signature.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon2);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/location.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon3);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/industry.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon4);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/house.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon5);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/employees.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setIcon(icon6);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/notebook-of-contacts.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setIcon(icon7);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/chief-executive-officer.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setIcon(icon8);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/product-description.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setIcon(icon9);
        self.tw_ViewEnterprise.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tw_ViewEnterprise.rowCount() < 1):
            self.tw_ViewEnterprise.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_ViewEnterprise.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_ViewEnterprise.setItem(0, 8, __qtablewidgetitem18)
        self.tw_ViewEnterprise.setObjectName(u"tw_ViewEnterprise")
        self.tw_ViewEnterprise.setRowCount(1)
        self.tw_ViewEnterprise.setColumnWidth(0,100)
        self.tw_ViewEnterprise.setColumnWidth(1,140)
        self.tw_ViewEnterprise.setColumnWidth(2,140)
        self.tw_ViewEnterprise.setColumnWidth(3,100)
        self.tw_ViewEnterprise.setColumnWidth(4,100)
        self.tw_ViewEnterprise.setColumnWidth(5,140)
        self.tw_ViewEnterprise.setColumnWidth(6,100)
        self.tw_ViewEnterprise.setColumnWidth(7,100)
        self.tw_ViewEnterprise.setColumnWidth(8,150)
        self.tw_ViewEnterprise.setColumnWidth(8,100)
        self.tw_ViewEnterprise.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tw_ViewEnterprise)

        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_GetData = QPushButton(self.centralwidget)
        self.btn_GetData.setObjectName(u"btn_GetData")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_GetData.sizePolicy().hasHeightForWidth())
        self.btn_GetData.setSizePolicy(sizePolicy1)
        self.btn_GetData.setMinimumSize(QSize(29, 0))
        self.btn_GetData.setMaximumSize(QSize(200, 16777215))
        self.btn_GetData.setAutoFillBackground(False)
        self.btn_GetData.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btn_GetData)

        self.btn_SaveData = QPushButton(self.centralwidget)
        self.btn_SaveData.setObjectName(u"btn_SaveData")

        self.horizontalLayout_2.addWidget(self.btn_SaveData)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        w_InfoEnterprise.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_InfoEnterprise)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 22))
        w_InfoEnterprise.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_InfoEnterprise)
        self.statusbar.setObjectName(u"statusbar")
        w_InfoEnterprise.setStatusBar(self.statusbar)

        self.retranslateUi(w_InfoEnterprise)

        QMetaObject.connectSlotsByName(w_InfoEnterprise)
    # setupUi

    def retranslateUi(self, w_InfoEnterprise):
        w_InfoEnterprise.setWindowTitle(QCoreApplication.translate("w_InfoEnterprise", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_InfoEnterprise", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0438", None))
        ___qtablewidgetitem = self.tw_ViewEnterprise.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("w_InfoEnterprise", u"Enterprise_ID", None));
        ___qtablewidgetitem1 = self.tw_ViewEnterprise.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("w_InfoEnterprise", u"Enterprise_Name", None));
        ___qtablewidgetitem2 = self.tw_ViewEnterprise.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("w_InfoEnterprise", u"Enterprise_City", None));
        ___qtablewidgetitem3 = self.tw_ViewEnterprise.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("w_InfoEnterprise", u"Industry_ID", None));
        ___qtablewidgetitem4 = self.tw_ViewEnterprise.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("w_InfoEnterprise", u"Address", None));
        ___qtablewidgetitem5 = self.tw_ViewEnterprise.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("w_InfoEnterprise", u"Employee_Count", None));
        ___qtablewidgetitem6 = self.tw_ViewEnterprise.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("w_InfoEnterprise", u"Contact_ID", None));
        ___qtablewidgetitem7 = self.tw_ViewEnterprise.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("w_InfoEnterprise", u"Manager", None));
        ___qtablewidgetitem8 = self.tw_ViewEnterprise.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("w_InfoEnterprise", u"Description", None));
        ___qtablewidgetitem9 = self.tw_ViewEnterprise.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u2116", None));

        __sortingEnabled = self.tw_ViewEnterprise.isSortingEnabled()
        self.tw_ViewEnterprise.setSortingEnabled(False)
        self.tw_ViewEnterprise.setSortingEnabled(__sortingEnabled)

        self.btn_GetData.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.btn_SaveData.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

