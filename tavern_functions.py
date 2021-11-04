from input_functions import *
from throw_dices_form import ThrowDicesForm
from sqlite_functions import *
NO_OUTPUT = 'Вывод не нужен'


def get_form_tav_funcs(getform):
    global form
    form = getform


def get_tavern_and_startloc(gettavern, getstartloc):
    global tavern, start_location
    tavern = gettavern
    start_location = getstartloc


def get_player(getpl):
    global pl
    pl = getpl


def games():
    form.form2 = ThrowDicesForm(form, pl)
    form.form2.show()


def elixirs():
    output('Вы решаете купить выпивки. Однако вы понимаете, что алкоголь лишь навредит вам. Поэтому ваш выбор падает на'
           ' лечебные зелья, полностью восстанавливающие ваш запас здоровья и эликсиры исцеления, которые вылечат вас'
           ' лишь на четверть от максимального запаса. Первые стоят 120 монет, вторые - 50. Также бармен предлагает вам'
           ' порцию зелья лечения за половину стоимости, если вы выпьете ее при нем')
    input_four(['Зелья', 'Эликсиры', 'Лечиться', 'Уйти'], [buy_potions, buy_elixirs, tavern_heal, start_location])


def give_money():
    second_login = dialog_str_input('Кому передать?', 'Введите логин пользователя, с которым хотите поделиться'
                                                      'монетами')
    all_list = get_all_players()
    logins_list = []
    for elem in all_list:
        logins_list.append(elem[0])
    if second_login not in logins_list:
        output('Нет такого пользователя!')
    else:
        n = dialog_int_input('Сколько передать?', 'Введите количество монет')
        if n >= pl.money:
            pl.money -= n
            add_player_money(second_login, n)
            labels_update()



def buy_potions():
    n = dialog_int_input('Количество зелий', 'Выберите, сколько зелий хотите купить')
    if n != 0:
        if pl.money >= 120 * n:
            pl.potions += n
            pl.money -= 120 * n
            output('Поздравляем с покупкой')
        else:
            output('У вас недостаточно денег')
    tavern(NO_OUTPUT)
    labels_update()


def buy_elixirs():
    n = dialog_int_input('Количество эликсиров', 'Выберите, сколько эликсиров хотите купить')
    if n != 0:
        if pl.money >= 50 * n:
            pl.elixirs += n
            pl.money -= 50 * n
            output('Поздравляем с покупкой')
        else:
            output('У вас недостаточно денег')
    tavern(NO_OUTPUT)
    labels_update()


def tavern_heal():
    if pl.money >= 60:  # 60 - половина стоимости зелья лечения
        pl.heal('max')
    else:
        output('Недостаточно монет!')
    tavern(NO_OUTPUT)
