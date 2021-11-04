from input_functions import *
from tavern_functions import *
from creatures import *
from underground_functions import *
from rating_form import *
WEAPON_DICT = {
    'Топор': Weapon('Топор', 5, 1200),
    'Короткий меч': Weapon('Короткий меч', 7, 3000),
    'Цеп': Weapon('Цеп', 10, 5000),
    'Булава': Weapon('Булава', 15, 7500),
    'Средний меч': Weapon('Средний меч', 20, 10000),
    'Длинный меч': Weapon('Длинный меч', 32, 13000),
    'Алебарда': Weapon('Алебарда', 40, 20000),
    'Клеймор': Weapon('Клеймор', 50, 30000),
    'Меч Судеб': Weapon('Меч Судеб', 70, 60000),
    'Клинок Армагеддона': Weapon('Клинок Армагеддона', 120, '???')
}
ARMOR_DICT = {
    'Кожаная броня': Armor('Кожаная броня', 1, 1500),
    'Кожаная броня с металлическими вставками': Armor('Кожаная броня с металлическими вставками', 2, 3000),
    'Железная броня': Armor('Железная броня', 3, 5000),
    'Стальная броня': Armor('Стальная броня', 5, 7500),
    'Магически усиленная стальная броня': Armor('Магически усиленная стальная броня', 7, 10000),
    'Мифриловая броня': Armor('Мифриловая броня', 10, 20000),
    'Доспех Армагеддона': Armor('Доспех Армагеддона', 20, '???')
}
AMULETS_DICT = {
    'Камень регенерации': (Amulet('Камень регенерации', 'регенерация', 2000, 2),
                           'Этот камень повысит вашу регенерацию'),
    'Большой камень регенерации': (Amulet('Большой камень регенерации', 'регенерация', 10000, 5),
                                   'Этот камень сильно повысит вашу регенерацию'),
    'Камень защиты': (Amulet('Камень защиты', 'защита', 3000, 2),
                      'Этот камень увеличит эффективность вашей защитной стойки'),
    'Религиозный амулет культиста': (Amulet('Религиозный амулет культиста', 'доп.урон', 10000, 20),
                                     'Это странный артефакт, найденный у сумасшедшего культиста. Никто не знает, что '
                                     'он делает'),
}
NO_OUTPUT = 'Вывод не нужен'


def get_form_locations(getform, getpl):
    global form, pl
    form = getform
    pl = getpl


def liders_table():
    form.liders_form = RatingForm(form)
    form.liders_form.show()


def shop(*args):
    if args[0] != 'Вывод не нужен':
        output('Вы пришли в магазин. Тут продается оружие, броня и амулеты. Искатели приходят сюда, чтобы купить себе '
               'аммуницию для похода в Подземелье')
        output(str(pl.weapon) + '\n' + str(pl.armor) + '\n' + str(pl.amulet))
    input_four(['Оружие', 'Броня', 'Амулеты', 'Уйти'], [shop_weapon, shop_armor, shop_amulets, start_location])


def tavern(*args):
    if args[0] != 'Вывод не нужен':
        output('Вы пришли в таверну. Тут люди пьют различные напитки, играют в игры и иногда передают друг другу '
               'монеты')
    input_four(['Азартные игры', 'Взять выпивки', 'Передать монеты', 'Уйти'], [games, elixirs, give_money,
                                                                               start_location])


def underground():
    output('Вы спускаетесь в Подземелье..')
    select_location()


def start_location():
    output('Перед Вами встал выбор: пойти в магазин, в таверну или отправиться в атаку')
    input_four(['Магазин', 'Таверна', 'Подземелье', 'Таблица лидеров'], [shop, tavern, underground, liders_table])


def shop_weapon():
    list_of_strings = list(WEAPON_DICT.keys())
    list_of_strings = list(map(lambda x: str(x + ' - ' + str(WEAPON_DICT[x].damage) + ' урона, '
                                             + str(WEAPON_DICT[x].price) + ' монет'), list_of_strings))
    weapon = dialog_list_input('Оружейный ассортимент', 'Выберите, что хотите купить',
                                             ['Ничего'] + list_of_strings)
    if weapon != 'Ничего':
        weapon = weapon.split(' - ')[0]
        if pl.money < WEAPON_DICT[weapon].price:
            output('Недостаточно монет!')
        else:
            output(f'Вы приобрели: {weapon.lower()}')
            pl.money -= WEAPON_DICT[weapon].price
            pl.weapon = WEAPON_DICT[weapon]
    labels_update()
    shop(NO_OUTPUT)


def shop_armor():
    list_of_strings = list(ARMOR_DICT.keys())
    list_of_strings = list(map(lambda x: str(x + ' - ' + str(ARMOR_DICT[x].defence) + ' защиты, '
                                             + str(ARMOR_DICT[x].price) + ' монет'), list_of_strings))
    armor = dialog_list_input('Оружейный ассортимент', 'Выберите, что хотите купить',
                              ['Ничего'] + list_of_strings)
    if armor != 'Ничего':
        armor = armor.split(' - ')[0]
        if pl.money < ARMOR_DICT[armor].price:
            output('Недостаточно монет!')
        else:
            output(f'Вы приобрели: {armor.lower()}')
            pl.money -= ARMOR_DICT[armor].price
            pl.armor = ARMOR_DICT[armor]
    labels_update()
    shop(NO_OUTPUT)


def shop_amulets():
    list_of_strings = list(AMULETS_DICT.keys())
    list_of_strings = list(map(lambda x: str(x) + ' - ' + AMULETS_DICT[x][-1] + ', стоит ' +
                               str(AMULETS_DICT[x][0].price), list_of_strings))
    amulet = dialog_list_input('Ассортимент амулетов', 'Выберите, что хотите купить',
                               ['Ничего'] + list_of_strings)
    if amulet != 'Ничего':
        amulet = amulet.split(' - ')[0]
        if pl.money < AMULETS_DICT[amulet][0].price:
            output('Недостаточно монет!')
        else:
            output(f'Вы приобрели: {amulet.lower()}')
            pl.money -= AMULETS_DICT[amulet][0].price
            pl.amulet = AMULETS_DICT[amulet][0]
    shop(NO_OUTPUT)
    labels_update()


def select_location():
    output('Выберите локацию')
    input_four(['Канализация', 'Пещеры', 'Катакомбы', 'Адская башня'], [tubes, caves, catacombs, hell_tower])


def tubes():
    output('Вы подходите ко входу в Канализацию. Это верхний уровень Подземелья, самый лёгкий. Войти?')
    input_two(['Да', 'Нет'], [tubes_happening_choice, start_location])


def caves():
    output('Вы подходите ко входу в Пещеры. Это средний уровень Подземелья. Монстры здесь на порядок сильнее '
           'монстров из Канализации. Войти?')
    input_two(['Да', 'Нет'], [caves_happening_choice, start_location])


def catacombs():
    output('Вы подходите ко входу в Катакомбы. Это самый глубокий уровень Подземелья. Монстры здесь настолько сильные, '
           'что даже опытные искатели побаиваются в них заходить. Войти?')
    input_two(['Да', 'Нет'], [catacombs_happening_choice, start_location])


def hell_tower():
    output('Вы подходите к Адской Башне. Она сейчас неактивна, и сразиться с боссом не получится. Увы')


get_tavern_and_startloc(tavern, start_location)
get_start_location(start_location)