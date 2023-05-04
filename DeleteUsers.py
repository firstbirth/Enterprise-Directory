# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeleteUsersytCDVb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_w_DeleteUsers(object):
    def setupUi(self, w_DeleteUsers):
        if not w_DeleteUsers.objectName():
            w_DeleteUsers.setObjectName(u"w_DeleteUsers")
        w_DeleteUsers.resize(320, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_DeleteUsers.sizePolicy().hasHeightForWidth())
        w_DeleteUsers.setSizePolicy(sizePolicy)
        w_DeleteUsers.setMinimumSize(QSize(320, 160))
        w_DeleteUsers.setMaximumSize(QSize(320, 200))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        w_DeleteUsers.setWindowIcon(icon)
        w_DeleteUsers.setStyleSheet(u"#centralwidget{\n"
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
        self.centralwidget = QWidget(w_DeleteUsers)
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

        self.cmbx_Users = QComboBox(self.groupBox)
        self.cmbx_Users.setObjectName(u"cmbx_Users")

        self.horizontalLayout_2.addWidget(self.cmbx_Users)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_DelUser = QPushButton(self.groupBox)
        self.btn_DelUser.setObjectName(u"btn_DelUser")

        self.verticalLayout.addWidget(self.btn_DelUser)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.groupBox)

        w_DeleteUsers.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_DeleteUsers)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        w_DeleteUsers.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_DeleteUsers)
        self.statusbar.setObjectName(u"statusbar")
        w_DeleteUsers.setStatusBar(self.statusbar)

        self.retranslateUi(w_DeleteUsers)

        QMetaObject.connectSlotsByName(w_DeleteUsers)
    # setupUi

    def retranslateUi(self, w_DeleteUsers):
        w_DeleteUsers.setWindowTitle(QCoreApplication.translate("w_DeleteUsers", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_DeleteUsers", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u0445", None))
        self.lb_Desc.setText(QCoreApplication.translate("w_DeleteUsers", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_DelUser.setText(QCoreApplication.translate("w_DeleteUsers", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

