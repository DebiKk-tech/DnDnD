# -*- coding: utf-8 -*-

from random import randint, choice

from input_functions import *
from creatures import *
from constants import *

defence_value = 0


def get_player_and_form_fight(getpl, getform):
    global pl, form
    pl = getpl
    form = getform


def get_start_location_fight(getstartloc):
    global start_location
    start_location = getstartloc


def monster_label_update(monster):
    if monster.health != 0:
        form.lbl_monster_health.setText(f'{monster.health}/{monster.maxhealth}')
    else:
        form.lbl_monster_health.setText('')


def fight(get_monster, get_location=False):
    global monster, defence_value, location
    location = get_location
    defence_value = 0
    monster = get_monster
    monster_label_update(monster)
    form.lbl_monster_name.setText(monster.name.capitalize())
    form.set_bar_monster_health_values(0, monster.health)
    form.set_image(monster.image)
    if not monster.boss:
        input_three([ATTACK, HEAL, DEFENCE], [attack, heal, defence])
    else:
        input_four([ATTACK, HEAL, DEFENCE, RUN], [attack, heal, defence, run])


def attack():
    global defence_value
    monster.get_damaged(pl.attack())
    form.bar_monster_health.setValue(monster.health)
    if not monster.check_if_dead():
        next_turn()
    else:
        if monster.boss:
            output('Босс побеждён! Поздравляем!')
            # С шансом 1 к 25 игрок получает особую награду - Доспех или Клинок Армагеддона
            n = randint(0, 24)
            if n == 13:
                reward = choice([ARMAGEDDON_SWORD, ARMAGEDDON_ARMOR])
                output(f'Среди останков босса вы обнаружили легендарный предмет: {reward}')
                if reward == ARMAGEDDON_SWORD and pl.weapon.name != ARMAGEDDON_SWORD:
                    pl.weapon = Weapon(ARMAGEDDON_SWORD, 100, 0)
                    output('Это оружие, которое наносит 100 урона')
                elif reward == ARMAGEDDON_ARMOR and pl.armor.name != ARMAGEDDON_ARMOR:
                    pl.armor = Armor(ARMAGEDDON_ARMOR, 20, 0)
                    output('Это броня, которая поглощает 20 урона')
                else:
                    output('Однако он у вас уже есть, так что вы продали его')
                    pl.money += 20000
                    labels_update()
        end_of_fight()
        if not monster.boss:
            location(MONSTER_DEFEATED)
        else:
            start_location()


def heal():
    input_three([ELIXIR, POTION, CANCEL], [elixir, potion, cancel])


def elixir():
    global defence_value
    # Если есть эликсиры (elixirs > 0)..
    if pl.elixirs > 0:
        # Тут maxhealth * 0.25, т.к. эликсиры исцеляют на четверть от максимального запаса здоровья
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


def run():
    # У игрока есть шанс 1 к 5 чтобы сбежать
    n = randint(1, 5)
    if n == 2:
        output('Вы сбежали')
        end_of_fight()
        start_location()
    else:
        output('Вы хотели сбежать, но магия Адской Башни не позволила вам это сделать')
        next_turn()


def next_turn(current_turn_defence=False):
    global defence_value
    # Каждый ход защита уменьшается на 1, если игрок не нажал кнопку "Защита"
    if current_turn_defence:
        if defence_value > 0:
            defence_value -= 1
        pl.amulet_action()
    monster.attack(defence_value)
    pl.check_if_dead()


def end_of_fight():
    form.bar_monster_health.setVisible(False)
    form.lbl_monster_name.setText('')
    form.set_image(False)
    if monster.boss:
        id = get_boss_id_by_name(monster.name)
        update_boss(monster, id)
        if get_bosses_alive() == [1, 1, 1]:
            output('УРА! Все боссы побеждены! Местные жители благодарят вас, и вручают награду')
            pl.money += 200000
            labels_update()
