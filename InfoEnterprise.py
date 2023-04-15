# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoEnterpriseZxrFRC.ui'
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
        w_InfoEnterprise.resize(1050, 476)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_InfoEnterprise.sizePolicy().hasHeightForWidth())
        w_InfoEnterprise.setSizePolicy(sizePolicy)
        w_InfoEnterprise.setMinimumSize(QSize(1020, 0))
        w_InfoEnterprise.setMaximumSize(QSize(1020, 16777215))
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
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_ViewEnterprise.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
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
        self.tw_ViewEnterprise.setFrameShape(QFrame.StyledPanel)
        self.tw_ViewEnterprise.setFrameShadow(QFrame.Sunken)
        self.tw_ViewEnterprise.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_ViewEnterprise.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tw_ViewEnterprise.setShowGrid(True)
        self.tw_ViewEnterprise.setGridStyle(Qt.SolidLine)
        self.tw_ViewEnterprise.setRowCount(1)
        self.tw_ViewEnterprise.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_ViewEnterprise.horizontalHeader().setDefaultSectionSize(100)
        self.tw_ViewEnterprise.setColumnWidth(7,150)
        self.verticalLayout.addWidget(self.tw_ViewEnterprise)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_GetData = QPushButton(self.groupBox)
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

        self.btn_SaveData = QPushButton(self.groupBox)
        self.btn_SaveData.setObjectName(u"btn_SaveData")

        self.horizontalLayout_2.addWidget(self.btn_SaveData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        w_InfoEnterprise.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_InfoEnterprise)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 22))
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
        ___qtablewidgetitem7.setText(QCoreApplication.translate("w_InfoEnterprise", u"Contact_Info_Manager", None));
        ___qtablewidgetitem8 = self.tw_ViewEnterprise.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("w_InfoEnterprise", u"Description", None));
        ___qtablewidgetitem9 = self.tw_ViewEnterprise.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u2116", None));

        __sortingEnabled = self.tw_ViewEnterprise.isSortingEnabled()
        self.tw_ViewEnterprise.setSortingEnabled(False)
        # ___qtablewidgetitem10 = self.tw_ViewEnterprise.item(0, 0)
        # ___qtablewidgetitem10.setText(QCoreApplication.translate("w_InfoEnterprise", u"1", None));
        # ___qtablewidgetitem11 = self.tw_ViewEnterprise.item(0, 1)
        # ___qtablewidgetitem11.setText(QCoreApplication.translate("w_InfoEnterprise", u"MyCompany", None));
        # ___qtablewidgetitem12 = self.tw_ViewEnterprise.item(0, 2)
        # ___qtablewidgetitem12.setText(QCoreApplication.translate("w_InfoEnterprise", u"1", None));
        # ___qtablewidgetitem13 = self.tw_ViewEnterprise.item(0, 3)
        # ___qtablewidgetitem13.setText(QCoreApplication.translate("w_InfoEnterprise", u"1", None));
        # ___qtablewidgetitem14 = self.tw_ViewEnterprise.item(0, 4)
        # ___qtablewidgetitem14.setText(QCoreApplication.translate("w_InfoEnterprise", u"asdasdasd", None));
        # ___qtablewidgetitem15 = self.tw_ViewEnterprise.item(0, 5)
        # ___qtablewidgetitem15.setText(QCoreApplication.translate("w_InfoEnterprise", u"21", None));
        # ___qtablewidgetitem16 = self.tw_ViewEnterprise.item(0, 6)
        # ___qtablewidgetitem16.setText(QCoreApplication.translate("w_InfoEnterprise", u"1", None));
        # ___qtablewidgetitem17 = self.tw_ViewEnterprise.item(0, 7)
        # ___qtablewidgetitem17.setText(QCoreApplication.translate("w_InfoEnterprise", u"1", None));
        # ___qtablewidgetitem18 = self.tw_ViewEnterprise.item(0, 8)
        # ___qtablewidgetitem18.setText(QCoreApplication.translate("w_InfoEnterprise", u"text", None));
        # self.tw_ViewEnterprise.setSortingEnabled(__sortingEnabled)

        self.btn_GetData.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.btn_SaveData.setText(QCoreApplication.translate("w_InfoEnterprise", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

