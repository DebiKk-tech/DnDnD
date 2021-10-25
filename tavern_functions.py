from input_functions import *


def get_tavern_and_startloc(gettavern, getstartloc):
    global tavern, start_location
    tavern = gettavern
    start_location = getstartloc


def get_player(getpl):
    global pl
    pl = getpl


def games():
    print('Азартные игры')
    output('Не реализовано')


def elixirs():
    output('Вы решаете купить выпивки. Однако вы понимаете, что алкоголь лишь навредит вам. Поэтому ваш выбор падает на'
           ' лечебные зелья, полностью восстанавливающие ваш запас здоровья и эликсиры исцеления, которые вылечат вас'
           ' лишь на четверть от максимального запаса. Первые стоят 120 монет, вторые - 50. Также бармен предлагает вам'
           ' порцию зелья лечения за половину стоимости, если вы выпьете ее при нем')
    input_four(['Зелья', 'Эликсиры', 'Лечиться', 'Уйти'], [buy_potions, buy_elixirs, tavern_heal, start_location])


def give_money():
    print('Передача денег')
    output('Не реализовано')


def buy_potions():
    n = dialog_int_input('Количество зелий', 'Выберите, сколько зелий хотите купить')
    if n != 0:
        if pl.money >= 120 * n:
            pl.potions += n
            pl.money -= 120 * n
            output('Поздравляем с покупкой')
            tavern('Вывод не нужен')
        else:
            output('У вас недостаточно денег')
            tavern('Вывод не нужен')
    else:
        tavern('Вывод не нужен')


def buy_elixirs():
    n = dialog_int_input('Количество эликсиров', 'Выберите, сколько эликсиров хотите купить')
    if n != 0:
        if pl.money >= 50 * n:
            pl.elixirs += n
            pl.money -= 50 * n
            output('Поздравляем с покупкой')
            tavern('Вывод не нужен')
        else:
            output('У вас недостаточно денег')
            tavern('Вывод не нужен')
    else:
        tavern('Вывод не нужен')


def tavern_heal():
    if pl.money >= 60:  # 60 - половина стоимости зелья лечения
        pl.heal('max')
        tavern('Вывод не нужен')
    else:
        output('Недостаточно монет!')
        tavern('Вывод не нужен')
