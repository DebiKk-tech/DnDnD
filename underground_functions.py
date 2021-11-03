from input_functions import *
from creatures import *
from random import choice, randint
from fight import *


def get_player_tubes(getpl):
    global pl
    pl = getpl


SOME_MONEY = 'немного денег'
MUCH_MONEY = 'много денег'
MONSTER = 'монстр'

MONSTERS_DICT = {
    'крыса': [(1, 3), 4, (8, 1)],
    'гнолл': [(4, 8), 10, (15, 2)],
    'краб': [(2, 5), 50, (30, 3)],
    'скелет': [(10, 15), 20, (30, 2)],
    'фантом': [(4, 8), 100, (30, 3)],
    'летучая мышь': [(15, 20), 40, (50, 4)],
    'паук': [(30, 50), 50, (100, 6)],
    'зомби': [(25, 40), 150, (200, 7)],
    'око зла': [(60, 70), 100, (300, 10)]
}

HAPPENINGS_LIST = [MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER,
                   SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, MUCH_MONEY]


def get_start_location(getstartloc):
    global start_location
    start_location = getstartloc


# Зачем в эту функцию я добавил такой, казалось бы, странный условный оператор, который выполняет одно и то же в обоих
# случаях? Во втором, когда он проверяет условие, он выполняет функцию happening_choice, а мне это не надо
def tubes_happening_choice(*args):
    if args[0] == 'Монстр повержен':
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [tubes_happening_choice, start_location])
        return False
    elif not happening_choice(TUBES_MONSTERS_LIST, tubes_happening_choice):
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [tubes_happening_choice, start_location])


def caves_happening_choice(*args):
    if args[0] == 'Монстр повержен':
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [caves_happening_choice, start_location])
        return False
    elif not happening_choice(CAVES_MONSTERS_LIST, caves_happening_choice):
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [caves_happening_choice, start_location])


def catacombs_happening_choice(*args):
    if args[0] == 'Монстр повержен':
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [catacombs_happening_choice, start_location])
        return False
    elif not happening_choice(CATACOMBS_MONSTERS_LIST, catacombs_happening_choice):
        output('Вы хотели бы пойти дальше?')
        input_two(['Да', 'Нет'], [catacombs_happening_choice, start_location])


def happening_choice(MONSTERS_LIST, location):
    happening = choice(HAPPENINGS_LIST)
    if happening == SOME_MONEY:
        found = randint(1, 6)
        output(f'Вы нашли немного монет, а именно, {found}')
        pl.money += found
        labels_update()
    elif happening == MUCH_MONEY:
        found = randint(10, 60)
        output(f'Вы нашли много монет, а именно, {found}')
        pl.money += found
        labels_update()
    elif happening == MONSTER:
        monster_name = choice(MONSTERS_LIST)
        monster = MONSTERS_DICT[monster_name]
        monster = Monster(monster[0], monster[1], monster[2])
        output(f'На вас напал монстр: {monster_name}')
        fight(monster, location)
        return True
    return False

