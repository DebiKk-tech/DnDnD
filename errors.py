# -*- coding: utf-8 -*-

class LoginIsntUniqueError(Exception):
    pass


class PasswordEmptyError(Exception):
    pass


class LoginEmptyError(Exception):
    pass


class PasswordIncorrectError(Exception):
    pass


class LoginIncorrectError(Exception):
    pass


class PlayerIsDeadError(Exception):
    pass