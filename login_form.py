# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from login_form_design import Ui_Form

from errors import *
from sqlite_functions import *
from constants import *


class LoginForm(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.radio_login.setChecked(True)
        self.parent = parent
        self.btn_input.clicked.connect(self.set_player_to_parent)

    def set_player_to_parent(self):
        login = self.edit_login.text()
        password = self.edit_password.text()
        try:
            if self.radio_registration.isChecked():
                check_login(login, registration=True)
                check_password(password, registration=True)
                add_player(login, password)
                self.parent.login = login
            else:
                check_login(login, registration=False)
                player_profile = get_player_by_login(login)
                correct_password = str(player_profile[0][1])
                check_password(password, correct_password, registration=False)
                self.parent.set_player(player_profile, login)
            self.parent.setVisible(True)
            self.close()
        except LoginEmptyError:
            self.lbl_msg.setText(LOGIN_INPUT)
        except LoginIsntUniqueError:
            self.lbl_msg.setText(LOGIN_ISNT_UNIQUE)
        except LoginIncorrectError:
            self.lbl_msg.setText(WRONG_LOGIN)
        except PasswordEmptyError:
            self.lbl_msg.setText(PASSWORD_INPUT)
        except PasswordIncorrectError:
            self.lbl_msg.setText(WRONG_PASSWORD)
        except PlayerIsDeadError:
            self.lbl_msg.setText(PLAYER_IS_DEAD)


def check_login(login, registration=False):
    all_list = get_all_players()
    logins_list = []
    for elem in all_list:
        logins_list.append(str(elem[0]))
    if login.strip() == '':
        raise LoginEmptyError
    elif login in logins_list and registration:
        raise LoginIsntUniqueError
    elif login not in logins_list and not registration:
        raise LoginIncorrectError
    if not registration:
        current_profile = get_player_by_login(login)[0]
        if current_profile[-1] == 1:
            raise PlayerIsDeadError


def check_password(password, correct='', registration=False):
    if password == '':
        raise PasswordEmptyError
    if not registration:
        if password != correct:
            raise PasswordIncorrectError
