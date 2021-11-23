# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

from throw_dices_form_design import Ui_Form
from random import randint
from input_functions import *
from constants import *


class ThrowDicesForm(QWidget, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        # По умолчанию оба кубика лежат единицами вверх
        self.pixmap1, self.pixmap2 = QPixmap('images/1_dot.png'), QPixmap('images/1_dot.png')
        self.lbl_image1.setPixmap(self.pixmap1)
        self.lbl_image2.setPixmap(self.pixmap2)
        self.btn_throw.clicked.connect(self.throw)
        self.parent = args[0]
        self.player = args[1]
        self.parent.setDisabled(True)

    def throw(self):
        if self.player.money < 20:
            self.lbl_msg.setText(NOT_ENOUGH_MONEY)
        else:
            # От 1 до 6 - количество граней игрального кубика
            n1 = randint(1, 6)
            n2 = randint(1, 6)
            # Минус 1, т.к. в списке индексация с нуля
            name1, name2 = DICE_IMAGES[n1 - 1], DICE_IMAGES[n2 - 1]
            self.pixmap1, self.pixmap2 = QPixmap(f'images/{name1}'), QPixmap(f'images/{name2}')
            self.lbl_image1.setPixmap(self.pixmap1)
            self.lbl_image2.setPixmap(self.pixmap2)
            if n1 + n2 == int(self.spn_number.text()):
                self.lbl_msg.setText(DICES_WIN_TEXT)
                self.player.money += DICES_WIN
            else:
                self.player.money -= DICES_LOSE
                self.lbl_msg.setText(DICES_LOSE_TEXT)

    def closeEvent(self, *event):
        self.parent.setDisabled(False)
        labels_update()