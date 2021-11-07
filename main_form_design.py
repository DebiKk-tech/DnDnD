# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 601)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.bar_monster_health = QtWidgets.QProgressBar(Form)
        self.bar_monster_health.setGeometry(QtCore.QRect(217, 160, 161, 20))
        self.bar_monster_health.setAutoFillBackground(True)
        self.bar_monster_health.setStyleSheet("QProgressBar::chunk {\n"
"     background-color: #FF0000;\n"
" }")
        self.bar_monster_health.setProperty("value", 24)
        self.bar_monster_health.setTextVisible(False)
        self.bar_monster_health.setObjectName("bar_monster_health")
        self.pln_output = QtWidgets.QPlainTextEdit(Form)
        self.pln_output.setGeometry(QtCore.QRect(13, 190, 571, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pln_output.setFont(font)
        self.pln_output.setObjectName("pln_output")
        self.btn_quad_1 = QtWidgets.QPushButton(Form)
        self.btn_quad_1.setEnabled(True)
        self.btn_quad_1.setGeometry(QtCore.QRect(10, 520, 131, 41))
        self.btn_quad_1.setObjectName("btn_quad_1")
        self.grp_four = QtWidgets.QButtonGroup(Form)
        self.grp_four.setObjectName("grp_four")
        self.grp_four.addButton(self.btn_quad_1)
        self.btn_quad_2 = QtWidgets.QPushButton(Form)
        self.btn_quad_2.setEnabled(True)
        self.btn_quad_2.setGeometry(QtCore.QRect(155, 520, 131, 41))
        self.btn_quad_2.setObjectName("btn_quad_2")
        self.grp_four.addButton(self.btn_quad_2)
        self.btn_quad_3 = QtWidgets.QPushButton(Form)
        self.btn_quad_3.setEnabled(True)
        self.btn_quad_3.setGeometry(QtCore.QRect(300, 520, 131, 41))
        self.btn_quad_3.setObjectName("btn_quad_3")
        self.grp_four.addButton(self.btn_quad_3)
        self.btn_quad_4 = QtWidgets.QPushButton(Form)
        self.btn_quad_4.setEnabled(True)
        self.btn_quad_4.setGeometry(QtCore.QRect(450, 520, 131, 41))
        self.btn_quad_4.setObjectName("btn_quad_4")
        self.grp_four.addButton(self.btn_quad_4)
        self.btn_triple_1 = QtWidgets.QPushButton(Form)
        self.btn_triple_1.setGeometry(QtCore.QRect(25, 520, 171, 51))
        self.btn_triple_1.setObjectName("btn_triple_1")
        self.grp_three = QtWidgets.QButtonGroup(Form)
        self.grp_three.setObjectName("grp_three")
        self.grp_three.addButton(self.btn_triple_1)
        self.btn_triple_3 = QtWidgets.QPushButton(Form)
        self.btn_triple_3.setGeometry(QtCore.QRect(205, 520, 171, 51))
        self.btn_triple_3.setObjectName("btn_triple_3")
        self.grp_three.addButton(self.btn_triple_3)
        self.btn_triple_2 = QtWidgets.QPushButton(Form)
        self.btn_triple_2.setGeometry(QtCore.QRect(390, 520, 171, 51))
        self.btn_triple_2.setObjectName("btn_triple_2")
        self.grp_three.addButton(self.btn_triple_2)
        self.btn_double_1 = QtWidgets.QPushButton(Form)
        self.btn_double_1.setGeometry(QtCore.QRect(10, 520, 276, 61))
        self.btn_double_1.setObjectName("btn_double_1")
        self.grp_two = QtWidgets.QButtonGroup(Form)
        self.grp_two.setObjectName("grp_two")
        self.grp_two.addButton(self.btn_double_1)
        self.btn_double_2 = QtWidgets.QPushButton(Form)
        self.btn_double_2.setGeometry(QtCore.QRect(310, 520, 276, 61))
        self.btn_double_2.setObjectName("btn_double_2")
        self.grp_two.addButton(self.btn_double_2)
        self.lbl_image = QtWidgets.QLabel(Form)
        self.lbl_image.setGeometry(QtCore.QRect(230, 30, 131, 121))
        self.lbl_image.setText("")
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image.setObjectName("lbl_image")
        self.lbl_health = QtWidgets.QLabel(Form)
        self.lbl_health.setGeometry(QtCore.QRect(20, 480, 221, 31))
        self.lbl_health.setObjectName("lbl_health")
        self.lbl_money = QtWidgets.QLabel(Form)
        self.lbl_money.setGeometry(QtCore.QRect(230, 480, 291, 31))
        self.lbl_money.setObjectName("lbl_money")
        self.lbl_monster_health = QtWidgets.QLabel(Form)
        self.lbl_monster_health.setGeometry(QtCore.QRect(380, 160, 141, 16))
        self.lbl_monster_health.setText("")
        self.lbl_monster_health.setObjectName("lbl_monster_health")
        self.lbl_monster_name = QtWidgets.QLabel(Form)
        self.lbl_monster_name.setGeometry(QtCore.QRect(100, 0, 391, 20))
        self.lbl_monster_name.setText("")
        self.lbl_monster_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_monster_name.setObjectName("lbl_monster_name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DnDnD"))
        self.btn_quad_1.setText(_translate("Form", "QUAD 1"))
        self.btn_quad_2.setText(_translate("Form", "QUAD 2"))
        self.btn_quad_3.setText(_translate("Form", "QUAD 3"))
        self.btn_quad_4.setText(_translate("Form", "QUAD 4"))
        self.btn_triple_1.setText(_translate("Form", "TRIPLE 1"))
        self.btn_triple_3.setText(_translate("Form", "TRIPLE 3"))
        self.btn_triple_2.setText(_translate("Form", "TIPLE 2"))
        self.btn_double_1.setText(_translate("Form", "DOUBLE 1"))
        self.btn_double_2.setText(_translate("Form", "DOUBLE 2"))
        self.lbl_health.setText(_translate("Form", "Ваше здоровье: 100/100"))
        self.lbl_money.setText(_translate("Form", "Ваши монеты: 20"))