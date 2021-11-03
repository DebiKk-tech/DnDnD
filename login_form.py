from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys
import sqlite3

from errors import *
con = sqlite3.connect('db_players.db')
cur = con.cursor()


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_form.ui', self)
        self.btn_input.clicked.connect(self.add)

    def add(self):
        login = self.edit_login.text()
        password = self.edit_password.text()
        try:
            self.check_login_and_password(login, password)
            self.lbl_msg.setText(login + ' ' + password)
        except LoginEmptyError:
            self.lbl_msg.setText('Введите логин!')
        except LoginIsntUniqueError:
            self.lbl_msg.setText('Логин занят!')
        except PasswordEmptyError:
            self.lbl_msg.setText('Введите пароль!')

    def check_login_and_password(self, login, password):
        all_list = cur.execute("""SELECT * from players""").fetchall()
        logins_list = []
        for elem in all_list:
            logins_list.append(elem[0])
        if login.strip() == '':
            raise LoginEmptyError
        elif login in logins_list:
            raise LoginIsntUniqueError
        elif password.strip() == '':
            raise PasswordEmptyError


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
