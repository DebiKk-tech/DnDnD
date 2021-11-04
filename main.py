import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit
from PyQt5.QtGui import QPixmap

from input_functions import *
from locations import *
from creatures import *
from tavern_functions import get_form_tav_funcs
from underground_functions import get_player_tubes
from login_form import LoginForm


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_form.ui', self)
        self.pln_output.setReadOnly(True)
        for btn in self.grp_two.buttons():
            btn.setVisible(False)
        for btn in self.grp_three.buttons():
            btn.setVisible(False)
        for btn in self.grp_four.buttons():
            btn.setVisible(False)
        self.bar_monster_health.setVisible(False)
        self.pl = Player()
        self.loginForm = LoginForm(self)
        self.loginForm.show()
        self.pixmap = 1
        get_form(self)
        get_form_locations(self, self.pl)
        get_player(self.pl)
        get_player_creatures(self.pl)
        get_player_tubes(self.pl)
        get_player_and_form_fight(self.pl, self)
        get_form_tav_funcs(self)
        self.pln_output.setPlainText('\n\nDnDnD успешно запустилась. Приятной игры!')
        start_location()

    def set_image(self, pixmap):
        if not pixmap:
            self.lbl_image.setVisible(False)
        else:
            self.lbl_image.setVisible(True)
            self.pixmap = QPixmap(pixmap)
            self.lbl_image.setPixmap(self.pixmap)

    def set_player(self, player_profile, login):
        self.login = login
        player_profile = player_profile[0]
        weapon = Weapon(player_profile[3].split(', ')[0], int(player_profile[3].split(', ')[1]),
                        int(player_profile[3].split(', ')[2]))
        armor = Armor(player_profile[4].split(', ')[0], int(player_profile[4].split(', ')[1]),
                        int(player_profile[4].split(', ')[2]))
        amulet = Amulet(player_profile[5].split(', ')[0], player_profile[5].split(', ')[1],
                        int(player_profile[5].split(', ')[2]), int(player_profile[5].split(', ')[3]))
        self.pl.points = player_profile[2]
        self.pl.weapon = weapon
        self.pl.armor = armor
        self.pl.amulet = amulet
        self.pl.money = player_profile[6]
        self.pl.health = player_profile[7]
        self.pl.level = player_profile[8]
        self.pl.exp = player_profile[9]
        self.pl.elixirs = player_profile[10]
        self.pl.poitons = player_profile[11]
        self.pl.maxhealth = 100 + (self.pl.level - 1) * 10
        self.pl.boost = 1 + (self.pl.level // 5 * 0.1)
        labels_update()

    def set_bar_monster_health_values(self, minimum, maximum):
        self.bar_monster_health.setVisible(True)
        self.bar_monster_health.setRange(minimum, maximum)
        self.bar_monster_health.setValue(maximum)

    def closeEvent(self, *event):
        profile_update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Ui_Form()
    form.show()
    form.setVisible(False)
    sys.excepthook = except_hook
    sys.exit(app.exec())
