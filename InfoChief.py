# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoChiefgqlCtG.ui'
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

class Ui_w_InfoChief(object):
    def setupUi(self, w_InfoChief):
        if not w_InfoChief.objectName():
            w_InfoChief.setObjectName(u"w_InfoChief")
        w_InfoChief.resize(800, 421)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_InfoChief.sizePolicy().hasHeightForWidth())
        w_InfoChief.setSizePolicy(sizePolicy)
        w_InfoChief.setMinimumSize(QSize(800, 0))
        w_InfoChief.setMaximumSize(QSize(1020, 16777215))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        w_InfoChief.setWindowIcon(icon)
        w_InfoChief.setStyleSheet(u"#centralwidget{\n"
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
        self.centralwidget = QWidget(w_InfoChief)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_ViewChieves = QTableWidget(self.groupBox)
        if (self.tw_ViewChieves.columnCount() < 4):
            self.tw_ViewChieves.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_ViewChieves.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_ViewChieves.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_ViewChieves.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_ViewChieves.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_ViewChieves.setObjectName(u"tw_ViewChieves")
        self.tw_ViewChieves.setFrameShape(QFrame.StyledPanel)
        self.tw_ViewChieves.setFrameShadow(QFrame.Sunken)
        self.tw_ViewChieves.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_ViewChieves.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tw_ViewChieves.setShowGrid(True)
        self.tw_ViewChieves.setGridStyle(Qt.SolidLine)
        self.tw_ViewChieves.setRowCount(0)
        self.tw_ViewChieves.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_ViewChieves.horizontalHeader().setDefaultSectionSize(100)
        self.tw_ViewChieves.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tw_ViewChieves)


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

        w_InfoChief.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_InfoChief)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        w_InfoChief.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_InfoChief)
        self.statusbar.setObjectName(u"statusbar")
        w_InfoChief.setStatusBar(self.statusbar)

        self.retranslateUi(w_InfoChief)

        QMetaObject.connectSlotsByName(w_InfoChief)
    # setupUi

    def retranslateUi(self, w_InfoChief):
        w_InfoChief.setWindowTitle(QCoreApplication.translate("w_InfoChief", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u0445", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_InfoChief", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0443\u0441\u043b\u0443\u0433\u0430\u0445", None))
        ___qtablewidgetitem = self.tw_ViewChieves.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("w_InfoChief", u"Manager_ID", None));
        ___qtablewidgetitem1 = self.tw_ViewChieves.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("w_InfoChief", u"Name", None));
        ___qtablewidgetitem2 = self.tw_ViewChieves.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("w_InfoChief", u"Phone", None));
        ___qtablewidgetitem3 = self.tw_ViewChieves.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("w_InfoChief", u"Start date", None));
        self.btn_GetData.setText(QCoreApplication.translate("w_InfoChief", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.btn_SaveData.setText(QCoreApplication.translate("w_InfoChief", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

