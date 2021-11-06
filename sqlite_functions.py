# -*- coding: utf-8 -*-

import sqlite3

from constants import *
con = sqlite3.connect('db_players.db')
cur = con.cursor()


def get_all_players():
    return cur.execute(GET_ALL_QUERY).fetchall()


def add_player(login, password):
    cur.execute(ADD_PLAYER_QUERY, (login, password))
    con.commit()


def change_player(login, pl, dead=False):
    weapon = pl.weapon.name + ', ' + str(pl.weapon.damage) + ', ' + str(pl.weapon.price)
    armor = pl.armor.name + ', ' + str(pl.armor.defence) + ', ' + str(pl.armor.price)
    amulet = pl.amulet.name + ', ' + str(pl.amulet.action) + ', ' + str(pl.amulet.price) + ', ' + str(pl.amulet.power)
    cur.execute(CHANGE_PLAYER_QUERY, (pl.money, pl.points, weapon, armor, amulet, pl.health, pl.level, pl.exp,
                                      pl.elixirs, pl.potions, dead, login))
    con.commit()


def get_player_by_login(login):
    return cur.execute(GET_PLAYER_BY_LOGIN_QUERY, (login,)).fetchall()


def add_player_money(login, n):
    player = get_player_by_login(login)[0]
    new_money = player[6] + n
    cur.execute(ADD_MONEY_QUERY, (new_money, login))
    con.commit()
