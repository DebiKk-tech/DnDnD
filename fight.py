# -*- coding: utf-8 -*-

from input_functions import *
from creatures import *
from constants import *

defence_value = 0


def get_player_and_form_fight(getpl, getform):
    global pl, form
    pl = getpl
    form = getform


def monster_label_update(monster):
    if monster.health != 0:
        form.lbl_monster_health.setText(f'{monster.health}/{monster.maxhealth}')
    else:
        form.lbl_monster_health.setText('')


def fight(get_monster, get_location):
    global monster, defence_value, location
    location = get_location
    defence_value = 0
    monster = get_monster
    monster_label_update(monster)
    form.lbl_monster_name.setText(monster.name.capitalize())
    form.set_bar_monster_health_values(0, monster.health)
    form.set_image(monster.image)
    input_three([ATTACK, HEAL, DEFENCE], [attack, heal, defence])


def attack():
    global defence_value
    monster.get_damaged(pl.attack())
    form.bar_monster_health.setValue(monster.health)
    if not monster.check_if_dead():
        next_turn()
    else:
        form.bar_monster_health.setVisible(False)
        form.lbl_monster_name.setText('')
        form.set_image(False)
        location(MONSTER_DEFEATED)


def heal():
    input_three([ELIXIR, POTION, CANCEL], [elixir, potion, cancel])


def elixir():
    global defence_value
    # Если есть эликсиры (elixirs > 0)..
    if pl.elixirs > 0:
        # Тут maxhealth * 0.25, т.к. эликсиры исцеляют на четверть от максимального запаса
        pl.heal(pl.maxhealth * 0.25)
        pl.elixirs -= 1
        next_turn()
    else:
        output(DONT_HAVE_ELIXIRS)


def potion():
    global defence_value
    # Если есть зелья (potions > 0)..
    if pl.potions > 0:
        pl.heal(MAX)
        pl.elixirs -= 1
        next_turn()
    else:
        output(DONT_HAVE_POTIONS)


def cancel():
    input_three([ATTACK, HEAL, DEFENCE], [attack, heal, defence])


def defence():
    global defence_value
    # pl.amulet_action возвращает значение, на которое увеличивает защиту, а 2 - значение защиты без какого либо влияния
    defence_value = 2 + pl.amulet_action()
    next_turn(True)


def next_turn(current_turn_defence=False):
    global defence_value
    # Каждый ход защита уменьшается на 1, если игрок не нажал кнопку "Защита"
    if current_turn_defence:
        if defence_value > 0:
            defence_value -= 1
        pl.amulet_action()
    monster.attack(defence_value)
    pl.check_if_dead()
