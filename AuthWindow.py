# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthWindowSAYhDC.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import icons_rc

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(405, 189)
        Authorization.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/organization.png", QSize(), QIcon.Normal, QIcon.Off)
        Authorization.setWindowIcon(icon)
        Authorization.setStyleSheet(u"#Authorization{\n"
"	background-color:#0d1b2a\n"
"}\n"
"\n"
".QLabel{\n"
"	color:#e0e1dd;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
".QGroupBox{\n"
"	color:#E0E1DD;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
".QPushButton{\n"
"	background-color:#293241;\n"
"	color:#E0E1DD;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"	background-color:#1b263b;\n"
"}")
        self.gridLayout = QGridLayout(Authorization)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_ok = QPushButton(Authorization)
        self.pb_ok.setObjectName(u"pb_ok")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/correct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_ok.setIcon(icon1)
        self.pb_ok.setIconSize(QSize(10, 10))

        self.gridLayout.addWidget(self.pb_ok, 2, 0, 1, 1)

        self.groupBox = QGroupBox(Authorization)
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
        self.lineEdit.setText("root")#это удалить
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.le_password = QLabel(self.groupBox)
        self.le_password.setObjectName(u"le_password")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.le_password)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setText("root")#это удалить
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pb_cancel = QPushButton(Authorization)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/multiply.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_cancel.setIcon(icon2)
        self.pb_cancel.setIconSize(QSize(10, 10))

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        self.lb_message = QLabel(Authorization)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(Authorization)

        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.pb_ok.setText(QCoreApplication.translate("Authorization", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.le_login.setText(QCoreApplication.translate("Authorization", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.le_password.setText(QCoreApplication.translate("Authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pb_cancel.setText(QCoreApplication.translate("Authorization", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.lb_message.setText(QCoreApplication.translate("Authorization", u"", None))
    # retranslateUi

