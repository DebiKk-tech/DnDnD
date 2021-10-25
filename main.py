import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit
from PyQt5.QtGui import QTextCursor
from input_functions import *
from locations import *
from creatures import *


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
        get_form(self)
        self.pl = Player()
        get_form_loc(self, self.pl)
        get_player(self.pl)
        output('DnDnD успешно запустилась. Приятной игры!')
        start_location()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Ui_Form()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
