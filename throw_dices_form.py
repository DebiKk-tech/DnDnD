from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from random import randint
from input_functions import *

DICE_IMAGES = ['1_dot.png', '2_dots.png', '3_dots.png', '4_dots.png', '5_dots.png', '6_dots.png']


class ThrowDicesForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('throw_dices_form.ui', self)
        self.pixmap1, self.pixmap2 = QPixmap('images/1_dot.png'), QPixmap('images/1_dot.png')
        self.lbl_image1.setPixmap(self.pixmap1)
        self.lbl_image2.setPixmap(self.pixmap2)
        self.btn_throw.clicked.connect(self.throw)
        self.parent = args[0]
        self.player = args[1]
        self.parent.setDisabled(True)

    def throw(self):
        if self.player.money < 20:
            self.lbl_msg.setText('У вас недостаточно монет')
        else:
            n1 = randint(1, 6)
            n2 = randint(1, 6)
            name1, name2 = DICE_IMAGES[n1 - 1], DICE_IMAGES[n2 - 1]
            self.pixmap1, self.pixmap2 = QPixmap(f'images/{name1}'), QPixmap(f'images/{name2}')
            self.lbl_image1.setPixmap(self.pixmap1)
            self.lbl_image2.setPixmap(self.pixmap2)
            if n1 + n2 == int(self.spn_number.text()):
                self.lbl_msg.setText('Вы выиграли 100 монет')
                self.player.money += 100
            else:
                self.player.money -= 20
                self.lbl_msg.setText('Вы програли 20 монет')

    def closeEvent(self, *event):
        self.parent.setDisabled(False)
        labels_update()