from input_functions import *
import sys
from PyQt5.QtWidgets import QMessageBox

experience_multiplier = 20
# Я не знаю, как охарактеризовать такие константы. В их названия трудно вложить смысловую нагрузку, поэтому я сделаю так
edinichka = 1
desyatochka = 10
pyaterochka = 5
nolik = 0
nolik_tochka_odin = 0.1
TUBES_MONSTERS_LIST = ['крыса', 'крыса', 'крыса', 'крыса', 'крыса', 'крыса', 'гнолл', 'гнолл', 'гнолл', 'краб']
CAVES_MONSTERS_LIST = ['скелет', 'скелет', 'скелет', 'скелет', 'скелет', 'скелет', 'скелет', 'фантом', 'фантом',
                       'фантом', 'фантом', 'летучая мышь', 'летучая мышь', 'летучая мышь', 'убийца', 'убийца']
CATACOMBS_MONSTERS_LIST = ['паук', 'паук', 'паук', 'паук', 'паук', 'паук', 'паук', 'зомби', 'зомби', 'зомби', 'зомби',
                           'око зла', 'око зла']


class Player:
    def __init__(self):
        self.maxhealth = 100
        self.health = 100
        self.money = 99999
        self.exp = 0
        self.level = 1
        self.boost = 0
        self.weapon = Weapon('нож', 2, 0)
        self.armor = Armor('тканевая одежда', 0, 0)
        self.amulet = Amulet('ничего', False, 0, 0)
        self.elixirs = 0
        self.potions = 0

    def add_exp(self, exp):
        self.exp += exp
        while self.exp >= self.level * experience_multiplier:
            if self.exp >= self.level * experience_multiplier:
                self.exp -= self.level * experience_multiplier
                self.level += edinichka
                self.maxhealth += desyatochka
                if self.level % pyaterochka == nolik:
                    self.boost += nolik_tochka_odin

    def heal(self, health):
        if health != 'max':
            self.health += health
            output(f'Вы восстановили {health} здоровья')
        if health == 'max' or self.health > self.maxhealth:
            self.health = self.maxhealth
            output(f'Ваши раны затянулись')
        profile_update()

    def check_if_dead(self):
        if self.health <= 0:
            self.die()

    def die(self):
        msg_death = QMessageBox()
        msg_death.setWindowTitle('Конец игры')
        msg_death.setText('Вы умерли! Игра окончена')
        msg_death.setIcon(QMessageBox.Warning)
        msg_death.setDefaultButton(QMessageBox.Close)
        msg_death.exec_()
        profile_update()
        sys.exit()


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
        if not self.action:
            return 'У вас нет амулета'
        elif self.action == 'доп.урон':
            return f'Ваш амулет - {self.name.lower()}'
        elif self.action == 'регенерация':
            return f'Ваш амулет - {self.name.lower()}, он восстанавливает по {str(self.power)} единиц здоровья за ход'
        elif self.action == 'макс.здоровье':
            return f'Ваш амулет - {self.name.lower()}, он увеличивает ваш максимальный запас здровья на ' \
                   f'{str(self.power)} единиц'


class Monster:
    def __init__(self, damage, health, reward, enemy):
        self.damage = damage
        self.health = health
        self.reward = reward
        self.enemy = enemy

    def attack(self, defence=0):
        damage_dealed = self.damage - self.enemy.armor.defence - defence
        if damage_dealed < 0:
            damage_dealed = 0
        self.enemy.health -= damage_dealed

    def die(self):
        self.enemy.money += self.reward[0]
        self.enemy.add_exp(self.reward[1])

