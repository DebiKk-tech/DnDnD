from input_functions import *
from creatures import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

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
    form.bar_monster_health.setVisible(True)
    form.bar_monster_health.setMaximum(monster.health)
    form.bar_monster_health.setMinimum(0)
    form.bar_monster_health.setValue(monster.health)
    form.setImage('images/rat.png')
    input_three(['Атака', 'Лечение', 'Защита'], [attack, heal, defence])


def attack():
    global defence_value
    monster.get_damaged(pl.attack())
    form.bar_monster_health.setValue(monster.health)
    if not monster.check_if_dead():
        next_turn()
    else:
        form.bar_monster_health.setVisible(False)
        location('Монстр повержен')


def heal():
    input_three(['Эликсир', 'Зелье', 'Отмена'], [elixir, potion, cancel])


def elixir():
    global defence_value
    if pl.elixirs > 0:
        pl.heal(pl.maxhealth * 0.25)
        pl.elixirs -= 1
        next_turn()
    else:
        output('У вас нет эликсиров!')


def potion():
    global defence_value
    if pl.potions > 0:
        pl.heal(max)
        pl.health = pl.maxhealth
        pl.elixirs -= 1
        next_turn()
    else:
        output('У вас нет зелий!')


def cancel():
    input_three(['Атака', 'Лечение', 'Защита'], [attack, heal, defence])


def defence():
    global defence_value
    defence_value = 2 + pl.amulet_action()
    next_turn(True)


def next_turn(current_turn_defence=False):
    global defence_value
    if current_turn_defence:
        if defence_value > 0:
            defence_value -= 1
        pl.amulet_action()
    monster.attack(defence_value * 2)
    pl.check_if_dead()
