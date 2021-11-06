# -*- coding: utf-8 -*-

from input_functions import *
from throw_dices_form import ThrowDicesForm
from sqlite_functions import *
from constants import *


def get_form_tav_funcs(getform):
    global form
    form = getform


def get_tavern_and_startloc(gettavern, getstartloc):
    global tavern, start_location
    tavern = gettavern
    start_location = getstartloc


def get_player(getpl):
    global pl
    pl = getpl


def games():
    form.form2 = ThrowDicesForm(form, pl)
    form.form2.show()


def drinks():
    output(TAVERN_HEAL_TEXT)
    input_four([POTIONS, ELIXIRS, HEAL, LEAVE], [buy_potions, buy_elixirs, tavern_heal, start_location])


def give_money():
    second_login = dialog_str_input(TO_WHO_GIVE, INPUT_WHO_GIVE)
    all_list = get_all_players()
    logins_list = []
    for elem in all_list:
        logins_list.append(elem[0])
    if second_login not in logins_list:
        output(NO_USER)
    else:
        n = dialog_int_input(HOW_MANY_GIVE, INPUT_HOW_MANY_GIVE)
        if n >= pl.money:
            pl.money -= n
            add_player_money(second_login, n)
            labels_update()



def buy_potions():
    n = dialog_int_input('Количество зелий', 'Выберите, сколько зелий хотите купить')
    if n != 0:
        if pl.money >= POTION_COST * n:
            pl.potions += n
            pl.money -= POTION_COST * n
            output(CONGRATS)
        else:
            output(NOT_ENOUGH_MONEY)
    tavern(NO_OUTPUT)
    labels_update()


def buy_elixirs():
    n = dialog_int_input('Количество эликсиров', 'Выберите, сколько эликсиров хотите купить')
    if n != 0:
        if pl.money >= ELIXIR_COST * n:
            pl.elixirs += n
            pl.money -= ELIXIR_COST * n
            output(CONGRATS)
        else:
            output(NOT_ENOUGH_MONEY)
    tavern(NO_OUTPUT)
    labels_update()


def tavern_heal():
    if pl.money >= HEAL_COST:
        pl.heal(MAX)
    else:
        output(NOT_ENOUGH_MONEY)
    labels_update()
    tavern(NO_OUTPUT)
