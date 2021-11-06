# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 71, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 71, 21))
        self.label_2.setFont(font)
        self.lbl_msg = QLabel(Form)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setGeometry(QRect(30, 200, 371, 31))
        self.lbl_msg.setFont(font)
        self.btn_input = QPushButton(Form)
        self.btn_input.setObjectName(u"btn_input")
        self.btn_input.setGeometry(QRect(140, 250, 75, 23))
        self.edit_login = QLineEdit(Form)
        self.edit_login.setObjectName(u"edit_login")
        self.edit_login.setGeometry(QRect(90, 30, 113, 20))
        self.edit_password = QLineEdit(Form)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setGeometry(QRect(90, 80, 113, 20))
        self.radio_login = QRadioButton(Form)
        self.radio_login.setObjectName(u"radio_login")
        self.radio_login.setGeometry(QRect(20, 140, 82, 17))
        self.radio_login.setFont(font)
        self.radio_registration = QRadioButton(Form)
        self.radio_registration.setObjectName(u"radio_registration")
        self.radio_registration.setGeometry(QRect(190, 140, 151, 17))
        self.radio_registration.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434 \u0438 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lbl_msg.setText("")
        self.btn_input.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.radio_login.setText(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
        self.radio_registration.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

