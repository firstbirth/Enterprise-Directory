# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUserDsrSht.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        if not CreateUser.objectName():
            CreateUser.setObjectName(u"CreateUser")
        CreateUser.resize(578, 529)
        CreateUser.setStyleSheet(u"#centralwidget{\n"
"background-color:#0D1B2A;\n"
"}\n"
"\n"
".QPushButton {\n"
"	background-color:#293241;\n"
"	color:#E0E1DD;\n"
"}\n"
"\n"
".QRadioButton{\n"
"color:#E0E1DD;\n"
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
"}\n"
".QLabel{\n"
"	color:#e0e1dd;\n"
"	font-weight:bold;\n"
"}")
        self.centralwidget = QWidget(CreateUser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 240, 118))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.User = QRadioButton(self.groupBox)
        self.User.setObjectName(u"User")

        self.horizontalLayout.addWidget(self.User)

        self.Admin = QRadioButton(self.groupBox)
        self.Admin.setObjectName(u"Admin")

        self.horizontalLayout.addWidget(self.Admin)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_Login = QLineEdit(self.groupBox)
        self.le_Login.setObjectName(u"le_Login")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_Login)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Password)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.btn_CreateUser = QPushButton(self.centralwidget)
        self.btn_CreateUser.setObjectName(u"btn_CreateUser")
        self.btn_CreateUser.setGeometry(QRect(170, 130, 80, 24))
        CreateUser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CreateUser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 22))
        CreateUser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CreateUser)
        self.statusbar.setObjectName(u"statusbar")
        CreateUser.setStatusBar(self.statusbar)

        self.retranslateUi(CreateUser)

        QMetaObject.connectSlotsByName(CreateUser)
    # setupUi

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(QCoreApplication.translate("CreateUser", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("CreateUser", u"\u0422\u0438\u043f \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.User.setText(QCoreApplication.translate("CreateUser", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.Admin.setText(QCoreApplication.translate("CreateUser", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("CreateUser", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("CreateUser", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.btn_CreateUser.setText(QCoreApplication.translate("CreateUser", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

