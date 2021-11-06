# -*- coding: utf-8 -*-

from input_functions import *
import sys
from PyQt5.QtWidgets import QMessageBox
from random import randint
from fight import monster_label_update
from constants import *


class Player:
    def __init__(self):
        self.maxhealth = 100
        self.health = 100
        self.money = 20
        self.exp = 0
        self.level = 1
        self.boost = 1
        self.weapon = Weapon('нож', 2, 0)
        self.armor = Armor('тканевая одежда', 0, 0)
        self.amulet = Amulet('ничего', 'False', 0, 0)
        self.elixirs = 0
        self.potions = 0
        self.points = 0

    def add_exp(self, exp):
        self.exp += exp
        level_changed = False
        while self.exp >= self.level * EXPERIENCE_MULTIPLIER:
            if self.exp >= self.level * EXPERIENCE_MULTIPLIER:
                self.exp -= self.level * EXPERIENCE_MULTIPLIER
                level_changed = True
                self.level += 1
                self.maxhealth += MAXHEALTH_PLUS
                if self.level % EVERY_THIS_LEVEL_BOOST_PLUS == 0:
                    self.boost += BOOST_PLUS
        if level_changed:
            output(f'Поздравляем! Ваш уровень теперь: {self.level}')

    def heal(self, health):
        if health != MAX:
            self.health += health
            output(f'Вы восстановили {health} здоровья')
        if health == MAX or self.health > self.maxhealth:
            self.health = self.maxhealth
            output(FULLY_HEALED)

    def check_if_dead(self):
        if self.health <= 0:
            self.die()

    def die(self):
        msg_death = QMessageBox()
        msg_death.setWindowTitle(GAME_OVER)
        msg_death.setText(YOU_DEAD)
        msg_death.setIcon(QMessageBox.Warning)
        msg_death.setDefaultButton(QMessageBox.Close)
        msg_death.exec_()
        profile_update(dead=True)
        sys.exit()

    def attack(self):
        damage = int(self.weapon.damage * self.boost)
        output(f'Вы атаковали монстра. Вы нанесли ему {damage} урона')
        return damage

    def amulet_action(self, boss_battle=False):
        # Здесь False текстом, т.к. из БД это значение приходит именно в виде текста, и оно не всегда False или True,
        # так что приходится использовать строку
        if self.amulet.action != 'False':
            if self.amulet.action == REGENERATION:
                self.heal(self.amulet.power)
                return 0
            elif self.amulet.action == DEFENCE or boss_battle:
                return self.amulet.power
        return 0


def get_player_creatures(getpl):
    global pl
    pl = getpl


class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

    def __str__(self):
        return 'У вас в руках оружие: ' + self.name.lower() + ' которое наносит ' + str(self.damage) + ' урона'


class Armor:
    def __init__(self, name, defence, price):
        self.name = name
        self.defence = defence
        self.price = price

    def __str__(self):
        return 'Вы носите броню: ' + self.name.lower() + ' которая поглощает ' + str(self.defence) + ' урона'


class Amulet:
    def __init__(self, name, action, price, power):
        self.name = name
        self.action = action
        self.price = price
        self.power = power

    def __str__(self):
        if self.action == 'False':
            return DONT_HAVE_AMULET
        elif self.action == PLUS_DAMAGE:
            return f'Ваш амулет - {self.name.lower()}'
        elif self.action == REGENERATION:
            return f'Ваш амулет - {self.name.lower()}, он восстанавливает по {str(self.power)} единиц здоровья за ход'
        elif self.action == DEFENCE:
            return f'Ваш амулет - {self.name.lower()}, он увеличивает эффективность вашей защитной стойки на ' \
                   f'{str(self.power)} единиц'


class Monster:
    def __init__(self, name, damage, health, reward, img_way):
        self.name = name
        self.damage = damage
        self.maxhealth = health
        self.reward = reward
        self.health = health
        self.image = img_way

    def attack(self, defence=0):
        damage_dealed = randint(self.damage[0], self.damage[1]) - pl.armor.defence - defence
        if damage_dealed < 0:
            damage_dealed = 0
        pl.health -= damage_dealed
        output(f'Монстр атаковал вас! Он нанёс вам {damage_dealed} урона')
        labels_update()
        # Если монстр - летучая мышь, она лечится на 1/10 от нанесенного урона
        if self.name == BAT:
            self.health += int(damage_dealed * 0.1)
            monster_label_update(self)

    def get_damaged(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        monster_label_update(self)

    def check_if_dead(self):
        if self.health <= 0:
            output(f'Вы одолели монстра, получив {self.reward[0]} монет и {self.reward[1]} опыта')
            pl.money += self.reward[0]
            pl.add_exp(self.reward[1])
            labels_update()
            return True
        return False

