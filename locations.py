from input_functions import *
from tavern_functions import *
from creatures import *
from underground_functions import *
from rating_form import *
from constants import*
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


def get_form_locations(getform, getpl):
    global form, pl
    form = getform
    pl = getpl


def liders_table():
    form.liders_form = RatingForm(form)
    form.liders_form.show()


def shop(*args):
    if args[0] != NO_OUTPUT:
        output(ENTERING_SHOP)
        output(str(pl.weapon) + '\n' + str(pl.armor) + '\n' + str(pl.amulet))
    input_four([WEAPON, ARMOR, AMULETS, LEAVE], [shop_weapon, shop_armor, shop_amulets, start_location])


def tavern(*args):
    if args[0] != NO_OUTPUT:
        output(ENTERING_TAVERN)
    input_four([GAMES, DRINKS, GIVE_MONEY, LEAVE], [games, elixirs, give_money,
                                                                               start_location])


def underground():
    output(ENTERING_UNDERGROUND)
    select_location()


def start_location():
    output(START_LOCATION_TEXT)
    input_four(['Магазин', 'Таверна', 'Подземелье', 'Таблица лидеров'], [shop, tavern, underground, liders_table])


def shop_weapon():
    bought_tovar_list = buy(WEAPON_DICT, ['Оружейный ассортимент', 'Выберите, что хотите купить'], weapons=True)
    if bought_tovar_list[0]:
        pl.weapon = bought_tovar_list[1]


def shop_armor():
    bought_tovar_list = buy(ARMOR_DICT, ['Ассортимент брони', 'Выберите, что хотите купить'], armor=True)
    if bought_tovar_list[0]:
        pl.armor = bought_tovar_list[1]


def shop_amulets():
    bought_tovar_list = buy(AMULETS_DICT, ['Ассортимент амулетов', 'Выберите, что хотите купить'], amulets=True)
    if bought_tovar_list[0]:
        pl.amulet = bought_tovar_list[1]


def buy(DICT, arguments, weapons=False, armor=False, amulets=False):
    list_of_strings = list(DICT.keys())
    if amulets:
        list_of_strings = list(map(lambda x: str(x) + ' - ' + DICT[x][-1] + ', стоит ' +
                                   str(DICT[x][0].price), list_of_strings))
    elif weapons:
        list_of_strings = list(map(lambda x: str(x + ' - ' + str(DICT[x].damage) + ' урона, '
                                                 + str(DICT[x].price) + ' монет'), list_of_strings))
    elif armor:
        list_of_strings = list(map(lambda x: str(x + ' - ' + str(DICT[x].defence) + ' защиты, '
                                                 + str(DICT[x].price) + ' монет'), list_of_strings))
    tovar = dialog_list_input(*arguments, [NOTHING] + list_of_strings)
    bought = False
    if tovar != NOTHING:
        tovar = tovar.split(' - ')[0]
        name = tovar.lower()
        if amulets:
            tovar = DICT[tovar][0]
        else:
            tovar = DICT[tovar]
        if pl.money < tovar.price:
            output(NOT_ENOUGH_MONEY)
        else:
            output(f'Вы приобрели: {name}')
            pl.money -= tovar.price
            bought = True
    shop(NO_OUTPUT)
    labels_update()
    return [bought, tovar]


def select_location():
    output(SELECT_LOCATION)
    input_four([TUBES, CAVES, CATACOMBS, HELLTOWER], [tubes, caves, catacombs, hell_tower])


def tubes():
    output(ENTERING_TUBES)
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