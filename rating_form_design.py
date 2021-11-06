# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(712, 418)
        self.tbl_top_rating = QTableWidget(Form)
        self.tbl_top_rating.setObjectName(u"tbl_top_rating")
        self.tbl_top_rating.setGeometry(QRect(5, 51, 701, 361))
        self.tbl_top_rating.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 331, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043b\u0438\u0434\u0435\u0440\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u043e\u043f \u0438\u0433\u0440\u043e\u043a\u043e\u0432 (\u043d\u0430 \u044d\u0442\u043e\u043c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0435)", None))
    # retranslateUi

