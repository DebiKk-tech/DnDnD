from input_functions import *


class Player():
    def __init__(self):
        self.maxhealth = 100
        self.health = 100
        self.money = 99999
        self.exp = 0
        self.level = 1
        self.boost = 0
        self.weapon = ('нож', 2)
        self.armor = ('тканевая одежда', 0)
        self.amulet = 'ничего'
        self.elixirs = 0
        self.potions = 0

    def add_exp(self, exp):
        self.exp += exp
        # self.level * 20 - кол-во опыта, необходимое для перехода на новый уровень
        while self.exp >= self.level * 20:
            if self.exp >= self.level * 20:
                self.exp -= self.level * 20
                self.level += 1
                self.maxhealth += 10
                if self.level % 5 == 0:
                    self.boost += 0.1

    def heal(self, health):
        if health != 'max':
            self.health += health
            output(f'Вы восстановили {health} здоровья')
        if health == 'max' or self.health > self.maxhealth:
            self.health = self.maxhealth
            output(f'Ваши раны затянулись')
        profile_update()

    def get_weapon_str(self):
        return 'У вас в руках оружие: ' + self.weapon[0] + ' которое наносит ' + str(self.weapon[1]) + ' урона'

    def get_armor_str(self):
        return 'Вы носите броню: ' + self.armor[0] + ' которая поглощает ' + str(self.armor[1]) + ' урона'

    def get_amulet_str(self):
        if self.amulet == 'Ничего':
            return 'У вас нет амулета'
        else:
            if self.amulet[0] == 'Религиозный амулет культиста':
                return 'Ваш амулет - религиозный амулет культиста'
            elif self.amulet[2] == 'регенерация':
                return 'Ваш амулет - ' + self.amulet[0] + ', он восстанавливает по ' + str(self.amulet[1]) + 'единиц \
здоровья за ход'
            elif self.amulet[2] == 'макс.здоровье':
                return 'Ваш амулет - ' + self.amulet[0] + ', он увеличивает ваш максимальный запас здровья на ' \
                       + str(self.amulet[1]) + 'единиц'
            else:
                return 'У вас нет амулета'

