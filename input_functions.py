# -*- coding: utf-8 -*-

from time import sleep
from PyQt5.QtWidgets import QInputDialog
from sqlite_functions import *


def get_form(getform):
    global form, pl
    form = getform
    pl = form.pl


def grp_connect(spis, list_of_funcs, grp):
    for n, btn in enumerate(grp):
        btn.disconnect()
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def enable_buttons(grp, wrong_grp_1, wrong_grp_2):
    for btn in grp.buttons():
        btn.setVisible(True)
    for btn2 in list(wrong_grp_1.buttons()) + list(wrong_grp_2.buttons()):
        btn2.setVisible(False)


def input_two(spis, list_of_funcs):
    enable_buttons(form.grp_two, form.grp_three, form.grp_four)
    grp_connect(spis, list_of_funcs, form.grp_two.buttons())


def input_three(spis, list_of_funcs):
    enable_buttons(form.grp_three, form.grp_two, form.grp_four)
    grp_connect(spis, list_of_funcs, form.grp_three.buttons())


def input_four(spis, list_of_funcs):
    enable_buttons(form.grp_four, form.grp_two, form.grp_three)
    grp_connect(spis, list_of_funcs, form.grp_four.buttons())


def dialog_input(dialog, *argumenst):
    okay_pressed = False
    while not okay_pressed:
        choice, okay_pressed = dialog(*argumenst)
    return choice


def dialog_list_input(name, text, list):
    return dialog_input(QInputDialog.getItem, form, name, text, list, 0, False)


def dialog_int_input(name, text, start=0, minim=0, max=999, step=1):
    return dialog_input(QInputDialog.getInt, form, name, text, start, minim, max, step)


def dialog_str_input(name, text):
    return dialog_input(QInputDialog.getText, form, name, text)


def output(text):
    wastext = form.pln_output.toPlainText()
    text = '\n' + text + '\n'
    for i in range(len(text)):
        form.pln_output.setPlainText(text[:i] + wastext)
        form.repaint()
        sleep(0.01)
    wastext = '\n' + form.pln_output.toPlainText()
    form.pln_output.setPlainText(wastext)


def profile_update(dead=False):
    # pl.level - 1, т.к. для первого уровня не нужен опыт, а points - это сумма exp и money
    pl.points = pl.money + (pl.level - 1) * EXPERIENCE_MULTIPLIER + pl.exp
    change_player(form.login, pl, dead)


def labels_update():
    form.lbl_money.setText(f'Ваши монеты: {pl.money}')
    form.lbl_health.setText(f'Ваше здоровье: {pl.health}/{pl.maxhealth}')

