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


def get_boss(boss_id):
    return cur.execute(GET_BOSS_BY_ID_QUERY, (boss_id,)).fetchall()


def update_boss(boss, id):
    dead = 0
    if boss.health <= 0:
        dead = 1
    cur.execute(UPDATE_BOSS_QUERY, (boss.health, dead, id))
    con.commit()


def get_boss_id_by_name(name):
    result = cur.execute(GET_BOSS_ID_BY_NAME_QUERY, (name,)).fetchall()
    return result[0][0]


def get_bosses_alive():
    result = cur.execute(GET_BOSSES_ALIVE_QUERY).fetchall()
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


def set_all_bosses_alive():
    cur.execute(SET_ROBOT_ALIVE_QUERY)
    cur.execute(SET_GNOLL_ALIVE_QUERY)
    cur.execute(SET_EYE_ALIVE_QUERY)
    cur.execute(SET_BOSSES_ALIVE_QUERY)
    con.commit()
