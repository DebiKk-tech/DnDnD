from input_functions import *
from tavern_functions import *
WEAPON_DICT = {
    'Топор': (5, 1200),
    'Короткий меч': (7, 3000),
    'Цеп': (10, 5000),
    'Булава': (15, 7500),
    'Средний меч': (20, 10000),
    'Длинный меч': (32, 13000),
    'Алебарда': (40, 20000),
    'Клеймор': (50, 30000),
    'Меч Судеб': (70, 60000),
    'Клинок Армагеддона': (120, '???')
}
ARMOR_DICT = {
    'Кожаная броня': (1, 1500),
    'Кожаная броня с металлическими вставками': (2, 3000),
    'Железная броня': (3, 5000),
    'Стальная броня': (5, 7500),
    'Магически усиленная стальная броня': (7, 10000),
    'Мифриловая броня': (10, 20000),
    'Доспех Армагеддона': (20, '???')
}
AMULETS_DICT = {
    'Камень регенерации': ((2, 'регенерация'), 2000, 'Этот камень повысит вашу регенерацию'),
    'Большой камень регенерации': ((5, 'регенерация'), 10000, 'Этот камень сильно повысит вашу регенерацию'),
    'Камень максимального здоровья': ((20, 'макс.здоровье'), 3000, 'Этот камень увеличит ваш максимальный запас \
здоровья'),
    'Религиозный амулет культиста': ((20, 'доп.урон'), 10000, 'Это странный артефакт, найденный у сумасшедшего \
культиста. Никто не знает, что он делает'),
}


def get_form_loc(getform, getpl):
    global form, pl
    form = getform
    pl = getpl


def liders_table():
    output('Не реализовано')
    print('Таблица лидеров')


def shop(*args):
    if args[0] != 'Вывод не нужен':
        output('Вы пришли в магазин. Тут продается оружие, броня и амулеты. Искатели приходят сюда, чтобы купить себе '
               'аммуницию для похода в Подземелье')
        output(pl.get_weapon_str() + '\n' + pl.get_armor_str() + '\n' + pl.get_amulet_str())
    input_four(['Оружие', 'Броня', 'Амулеты', 'Уйти'], [shop_weapon, shop_armor, shop_amulets, start_location])


def tavern(*args):
    if args[0] != 'Вывод не нужен':
        output('Вы пришли в таверну. Тут люди пьют различные напитки, играют в игры и иногда передают друг другу '
               'монеты')
    input_four(['Азартные игры', 'Взять выпивки', 'Передать монеты', 'Уйти'], [games, elixirs, give_money,
                                                                               start_location])


def underground():
    output('Не реализовано')
    print('Подземка')


def start_location():
    output('Перед Вами встал выбор: пойти в магазин, в таверну или отправиться в атаку')
    input_four(['Магазин', 'Таверна', 'Подземелье', 'Таблица лидеров'], [shop, tavern, underground, liders_table])


def shop_weapon():
    list_of_strings = list(WEAPON_DICT.keys())
    list_of_strings = list(map(lambda x: str(x + ' - ' + str(WEAPON_DICT[x][0]) + ' урона, ' + str(WEAPON_DICT[x][1])
                                             + ' монет'), list_of_strings))
    weapon = dialog_list_input('Оружейный ассортимент', 'Выберите, что хотите купить',
                                             ['Ничего'] + list_of_strings)
    if weapon != 'Ничего':
        weapon = weapon.split(' - ')[0]
        if pl.money < WEAPON_DICT[weapon][1]:
            output('Недостаточно монет!')
        else:
            output(f'Вы купили {weapon.lower()}')
            pl.money -= WEAPON_DICT[weapon][1]
            pl.weapon = weapon.lower(), WEAPON_DICT[weapon][0]
            profile_update()
        start_location()
    else:
        shop('Вывод не нужен')


def shop_armor():
    list_of_strings = list(ARMOR_DICT.keys())
    list_of_strings = list(map(lambda x: str(x + ' - ' + str(ARMOR_DICT[x][0]) + ' защиты, ' + str(ARMOR_DICT[x][1])
                                             + ' монет'), list_of_strings))
    armor = dialog_list_input('Оружейный ассортимент', 'Выберите, что хотите купить',
                              ['Ничего'] + list_of_strings)
    if armor != 'Ничего':
        armor = armor.split(' - ')[0]
        if pl.money < ARMOR_DICT[armor][1]:
            output('Недостаточно монет!')
        else:
            output(f'Вы купили {armor.lower()}')
            pl.money -= ARMOR_DICT[armor][1]
            pl.armor = armor.lower(), ARMOR_DICT[armor][0]
            profile_update()
        start_location()
    else:
        shop('Вывод не нужен')


def shop_amulets():
    list_of_strings = list(AMULETS_DICT.keys())
    list_of_strings = list(map(lambda x: str(x) + ' - ' + AMULETS_DICT[x][2] + ', стоит ' + str(AMULETS_DICT[x][1]),
                               list_of_strings))
    amulet = dialog_list_input('Оружейный ассортимент', 'Выберите, что хотите купить',
                               ['Ничего'] + list_of_strings)
    if amulet != 'Ничего':
        amulet = amulet.split(' - ')[0]
        if pl.money < AMULETS_DICT[amulet][1]:
            output('Недостаточно монет!')
        else:
            output(f'Вы купили {amulet.lower()}')
            pl.money -= AMULETS_DICT[amulet][1]
            pl.amulet = (amulet.lower(), AMULETS_DICT[amulet][0][0], AMULETS_DICT[amulet][0][1])
            profile_update()
        start_location()
    else:
        shop('Вывод не нужен')


get_tavern_and_startloc(tavern, start_location)