from input_functions import *
from creatures import *
from random import choice, randint


def get_player_tubes(getpl):
    global pl
    pl = getpl


SOME_MONEY = 'немного денег'
MUCH_MONEY = 'много денег'
MONSTER = 'монстр'

MONSTERS_DICT = {
    'крыса': Monster((1, 3), 4, (8, 1)),
    'гнолл': Monster((4, 8), 10, (15, 2)),
    'краб': Monster((2, 5), 50, (30, 3))
}

HAPPENINGS_LIST = [MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER,
                   SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, MUCH_MONEY]


def get_start_location(getstartloc):
    global start_location
    start_location = getstartloc


def happening_choice():
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
        monster_name = choice(TUBES_MONSTERS_LIST)
        monster = MONSTERS_DICT[monster_name]
        output(f'На вас напал монстр: {monster_name}')
        fight(monster)
    output('Вы хотели бы пойти дальше?')
    input_two(['Да', 'Нет'], [happening_choice, start_location])

