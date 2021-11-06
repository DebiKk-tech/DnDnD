# -*- coding: utf-8 -*-

from input_functions import *
from creatures import *
from random import choice, randint
from fight import *
from constants import  *


def get_player_tubes(getpl):
    global pl
    pl = getpl


def get_start_location(getstartloc):
    global start_location
    start_location = getstartloc


# Три эти однострочные функции были созданы для привязки к локации, а также к кнопке "Да" после события в Подземелье
def tubes_happening_choice(*args):
    prom_happening_choice(*args, MONSTERS_LIST=TUBES_MONSTERS_LIST, location=tubes_happening_choice)


def caves_happening_choice(*args):
    prom_happening_choice(*args, MONSTERS_LIST=CAVES_MONSTERS_LIST, location=caves_happening_choice)


def catacombs_happening_choice(*args):
    prom_happening_choice(*args, MONSTERS_LIST=CATACOMBS_MONSTERS_LIST, location=catacombs_happening_choice)


def prom_happening_choice(*args, MONSTERS_LIST, location):
    if args[0] == MONSTER_DEFEATED:
        output(GO_FURTHER)
        input_two([YES, NO], [location, start_location])
        return False
    else:
        monster_attacks = happening_choice(MONSTERS_LIST, location)
        if not monster_attacks:
            output(GO_FURTHER)
            input_two([YES, NO], [location, start_location])


def happening_choice(MONSTERS_LIST, location):
    happening = choice(HAPPENINGS_LIST)
    if happening != MONSTER:
        if happening == SOME_MONEY:
            found = randint(SOME_MONEY_MIN, SOME_MONEY_MAX)
            output(f'Вы нашли немного монет, а именно, {found}')
        elif happening == MUCH_MONEY:
            found = randint(MUCH_MONEY_MIN, MUCH_MONEY_MAX)
            output(f'Вы нашли много монет, а именно, {found}')
        pl.money += found
        labels_update()
    elif happening == MONSTER:
        monster_name = choice(MONSTERS_LIST)
        monster = MONSTERS_DICT[monster_name]
        monster = Monster(*monster)
        output(f'На вас напал монстр: {monster_name}')
        fight(monster, location)
        return True
    return False

