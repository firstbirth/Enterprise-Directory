# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BackupHwbqLc.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_w_CreateBackup(object):
    def setupUi(self, w_CreateBackup):
        if not w_CreateBackup.objectName():
            w_CreateBackup.setObjectName(u"w_CreateBackup")
        w_CreateBackup.resize(320, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_CreateBackup.sizePolicy().hasHeightForWidth())
        w_CreateBackup.setSizePolicy(sizePolicy)
        w_CreateBackup.setMinimumSize(QSize(320, 160))
        w_CreateBackup.setMaximumSize(QSize(320, 200))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        w_CreateBackup.setWindowIcon(icon)
        w_CreateBackup.setStyleSheet(u"#centralwidget{\n"
"background-color:#0D1B2A;\n"
"}\n"
"\n"
".QLabel{\n"
"	color:#E0E1DD;\n"
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
        self.centralwidget = QWidget(w_CreateBackup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_Desc = QLabel(self.groupBox)
        self.lb_Desc.setObjectName(u"lb_Desc")

        self.horizontalLayout_2.addWidget(self.lb_Desc)

        self.le_BackupName = QLineEdit(self.groupBox)
        self.le_BackupName.setObjectName(u"le_BackupName")

        self.horizontalLayout_2.addWidget(self.le_BackupName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_Password = QLabel(self.groupBox)
        self.lb_Password.setObjectName(u"lb_Password")

        self.verticalLayout.addWidget(self.lb_Password)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")
        self.le_Password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.le_Password)

        self.btn_CreateBckp = QPushButton(self.groupBox)
        self.btn_CreateBckp.setObjectName(u"btn_CreateBckp")

        self.verticalLayout.addWidget(self.btn_CreateBckp)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupBox)

        w_CreateBackup.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_CreateBackup)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        w_CreateBackup.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_CreateBackup)
        self.statusbar.setObjectName(u"statusbar")
        w_CreateBackup.setStatusBar(self.statusbar)

        self.retranslateUi(w_CreateBackup)

        QMetaObject.connectSlotsByName(w_CreateBackup)
    # setupUi

    def retranslateUi(self, w_CreateBackup):
        w_CreateBackup.setWindowTitle(QCoreApplication.translate("w_CreateBackup", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_CreateBackup", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438", None))
        self.lb_Desc.setText(QCoreApplication.translate("w_CreateBackup", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438: ", None))
        self.lb_Password.setText(QCoreApplication.translate("w_CreateBackup", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_CreateBckp.setText(QCoreApplication.translate("w_CreateBackup", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u0443\u044e \u043a\u043e\u043f\u0438\u044e", None))
    # retranslateUi

