# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(514, 420)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 341, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.spn_number = QSpinBox(Form)
        self.spn_number.setObjectName(u"spn_number")
        self.spn_number.setGeometry(QRect(390, 40, 42, 22))
        self.spn_number.setMinimum(2)
        self.spn_number.setMaximum(12)
        self.lbl_image1 = QLabel(Form)
        self.lbl_image1.setObjectName(u"lbl_image1")
        self.lbl_image1.setGeometry(QRect(80, 110, 141, 131))
        self.btn_throw = QPushButton(Form)
        self.btn_throw.setObjectName(u"btn_throw")
        self.btn_throw.setGeometry(QRect(190, 330, 111, 61))
        self.btn_throw.setFont(font)
        self.lbl_image2 = QLabel(Form)
        self.lbl_image2.setObjectName(u"lbl_image2")
        self.lbl_image2.setGeometry(QRect(280, 110, 141, 131))
        self.lbl_msg = QLabel(Form)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setGeometry(QRect(150, 280, 201, 41))
        self.lbl_msg.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u0441\u0438\u0442\u044c \u043a\u043e\u0441\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c:", None))
        self.lbl_image1.setText("")
        self.btn_throw.setText(QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u0441\u0438\u0442\u044c \u043a\u043e\u0441\u0442\u044c", None))
        self.lbl_image2.setText("")
        self.lbl_msg.setText("")
    # retranslateUi

