# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SQLEditorAfkRdD.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import icons_rc

class Ui_w_SQLEditor(object):
    def setupUi(self, w_SQLEditor):
        if not w_SQLEditor.objectName():
            w_SQLEditor.setObjectName(u"w_SQLEditor")
        w_SQLEditor.resize(1020, 486)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_SQLEditor.sizePolicy().hasHeightForWidth())
        w_SQLEditor.setSizePolicy(sizePolicy)
        w_SQLEditor.setMinimumSize(QSize(1020, 0))
        w_SQLEditor.setMaximumSize(QSize(1020, 16777215))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        w_SQLEditor.setWindowIcon(icon)
        w_SQLEditor.setStyleSheet(u"#centralwidget{\n"
"background-color:#0D1B2A;\n"
"}\n"
"\n"
".QLabel{\n"
"color:#E0E1DD;\n"
"}\n"
".QRadioButton{\n"
"color:#E0E1DD;\n"
"}\n"
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
        self.centralwidget = QWidget(w_SQLEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gbx_ChooseOption = QGroupBox(self.groupBox)
        self.gbx_ChooseOption.setObjectName(u"gbx_ChooseOption")
        self.gridLayout = QGridLayout(self.gbx_ChooseOption)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rbtn_Insert = QRadioButton(self.gbx_ChooseOption)
        self.rbtn_Insert.setObjectName(u"rbtn_Insert")

        self.gridLayout.addWidget(self.rbtn_Insert, 0, 0, 1, 1)

        self.rbtn_Delete = QRadioButton(self.gbx_ChooseOption)
        self.rbtn_Delete.setObjectName(u"rbtn_Delete")

        self.gridLayout.addWidget(self.rbtn_Delete, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gbx_ChooseOption, 0, 0, 1, 1)

        self.cm_DB = QComboBox(self.groupBox)
        self.cm_DB.addItem("")
        self.cm_DB.addItem("")
        self.cm_DB.addItem("")
        self.cm_DB.addItem("")
        self.cm_DB.addItem("")
        self.cm_DB.addItem("")
        self.cm_DB.setObjectName(u"cm_DB")

        self.gridLayout_2.addWidget(self.cm_DB, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.lt_Actions = QVBoxLayout()
        self.lt_Actions.setObjectName(u"lt_Actions")
        self.lb_ID = QLabel(self.centralwidget)
        self.lb_ID.setObjectName(u"lb_ID")

        self.lt_Actions.addWidget(self.lb_ID)

        self.cm_Rows = QComboBox(self.centralwidget)
        self.cm_Rows.setObjectName(u"cm_Rows")

        self.lt_Actions.addWidget(self.cm_Rows)

        self.lb_CityName = QLabel(self.centralwidget)
        self.lb_CityName.setObjectName(u"lb_CityName")

        self.lt_Actions.addWidget(self.lb_CityName)

        self.le_CityName = QLineEdit(self.centralwidget)
        self.le_CityName.setObjectName(u"le_CityName")

        self.lt_Actions.addWidget(self.le_CityName)


        self.verticalLayout_2.addLayout(self.lt_Actions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.lt_Btns = QHBoxLayout()
        self.lt_Btns.setObjectName(u"lt_Btns")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lt_Btns.addItem(self.horizontalSpacer)

        self.btn_AddData = QPushButton(self.centralwidget)
        self.btn_AddData.setObjectName(u"btn_AddData")

        self.lt_Btns.addWidget(self.btn_AddData)

        self.btn_DeleteData = QPushButton(self.centralwidget)
        self.btn_DeleteData.setObjectName(u"btn_DeleteData")

        self.lt_Btns.addWidget(self.btn_DeleteData)


        self.verticalLayout_2.addLayout(self.lt_Btns)

        w_SQLEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_SQLEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 22))
        w_SQLEditor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_SQLEditor)
        self.statusbar.setObjectName(u"statusbar")
        w_SQLEditor.setStatusBar(self.statusbar)

        self.retranslateUi(w_SQLEditor)

        QMetaObject.connectSlotsByName(w_SQLEditor)
    # setupUi

    def retranslateUi(self, w_SQLEditor):
        w_SQLEditor.setWindowTitle(QCoreApplication.translate("w_SQLEditor", u"SQL-\u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_SQLEditor", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 SQL-\u043a\u043e\u043c\u0430\u043d\u0434", None))
        self.gbx_ChooseOption.setTitle(QCoreApplication.translate("w_SQLEditor", u"\u0412\u044b\u0431\u043e\u0440 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.rbtn_Insert.setText(QCoreApplication.translate("w_SQLEditor", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.rbtn_Delete.setText(QCoreApplication.translate("w_SQLEditor", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cm_DB.setItemText(0, QCoreApplication.translate("w_SQLEditor", u"city", None))
        self.cm_DB.setItemText(1, QCoreApplication.translate("w_SQLEditor", u"contacts", None))
        self.cm_DB.setItemText(2, QCoreApplication.translate("w_SQLEditor", u"enterprises", None))
        self.cm_DB.setItemText(3, QCoreApplication.translate("w_SQLEditor", u"industry", None))
        self.cm_DB.setItemText(4, QCoreApplication.translate("w_SQLEditor", u"managers", None))
        self.cm_DB.setItemText(5, QCoreApplication.translate("w_SQLEditor", u"services", None))

        self.lb_ID.setText(QCoreApplication.translate("w_SQLEditor", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 ID \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f", None))
        self.lb_CityName.setText(QCoreApplication.translate("w_SQLEditor", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.btn_AddData.setText(QCoreApplication.translate("w_SQLEditor", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_DeleteData.setText(QCoreApplication.translate("w_SQLEditor", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

