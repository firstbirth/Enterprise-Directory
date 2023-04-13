# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aumGhCmZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 189)
        Form.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setFixedSize(400, 180)
        Form.setStyleSheet(u"#Form{\n"
"	background-color:#202020;\n"
"}\n"
"\n"
".QLabel{\n"
"	color:wheat;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
".QGroupBox{\n"
"	color:wheat;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
".QPushButton{\n"
"	background-color:green;\n"
"	color:white;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"	background-color:#006c00;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.le_login = QLabel(self.groupBox)
        self.le_login.setObjectName(u"le_login")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.le_login)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.le_password = QLabel(self.groupBox)
        self.le_password.setObjectName(u"le_password")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.le_password)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.lb_message = QLabel(Form)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.pb_ok = QPushButton(Form)
        self.pb_ok.setObjectName(u"pb_ok")
        icon_OK = QIcon(":/newPrefix/icons/correct.png")
        self.pb_ok.setIcon(icon_OK)
        self.pb_ok.setIconSize(QSize(10, 10))

        self.gridLayout.addWidget(self.pb_ok, 2, 0, 1, 1)

        self.pb_cancel = QPushButton(Form)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon_Cancel = QIcon(":/newPrefix/icons/multiply.png")
        self.pb_cancel.setIcon(icon_Cancel)
        self.pb_cancel.setIconSize(QSize(10, 10))

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Auth window", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Authorization", None))
        self.le_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.le_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lb_message.setText(QCoreApplication.translate("Form", u"message", None))
        self.pb_ok.setText(QCoreApplication.translate("Form", u"Login", None))
        self.pb_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

