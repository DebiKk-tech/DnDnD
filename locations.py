# -*- coding: utf-8 -*-

from input_functions import *
from tavern_functions import *
from creatures import *
from underground_functions import *
from rating_form import *
from constants import*
weapon_dict = {
    AXE: Weapon(AXE, 5, 1200),
    SHORT_SWORD: Weapon(SHORT_SWORD, 7, 3000),
    CEP: Weapon(CEP, 10, 5000),
    MACE: Weapon(MACE, 15, 7500),
    MID_SWORD: Weapon(MID_SWORD, 20, 10000),
    LONG_SWORD: Weapon(LONG_SWORD, 32, 13000),
    ALEBARD: Weapon(ALEBARD, 40, 20000),
    CLAYMORE: Weapon(CLAYMORE, 50, 30000),
    SWORD_OF_DOOM: Weapon(SWORD_OF_DOOM, 70, 60000)
}
armor_dict = {
    LEATHER_ARMOR: Armor(LEATHER_ARMOR, 1, 1500),
    HARDENED_LEATHER_ARNOR: Armor(HARDENED_LEATHER_ARNOR, 2, 3000),
    IRON_ARMOR: Armor(IRON_ARMOR, 3, 5000),
    STEEL_ARMOR: Armor(STEEL_ARMOR, 5, 7500),
    MAGIC_STEEL_ARMOR: Armor(MAGIC_STEEL_ARMOR, 7, 10000),
    MYTHRIL_ARMOR: Armor(MYTHRIL_ARMOR, 10, 20000)
}
# Строки в этом словаре отвечают за описание амулета в QInputDialog
amulets_dict = {
    REGEN_STONE: (Amulet(REGEN_STONE, REGENERATION, 2000, 2),
                  'Этот камень повысит вашу регенерацию'),
    BIG_REGEN_STONE: (Amulet(BIG_REGEN_STONE, REGENERATION, 10000, 5),
                      'Этот камень сильно повысит вашу регенерацию'),
    DEFENCE_STONE: (Amulet(DEFENCE_STONE, DEFENCE, 3000, 2),
                    'Этот камень увеличит эффективность вашей защитной стойки'),
    AMULET_OF_CULTIST: (Amulet(AMULET_OF_CULTIST, PLUS_DAMAGE, 10000, 20),
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
    input_four([GAMES, DRINKS, GIVE_MONEY, LEAVE], [games, drinks, give_money,
                                                                               start_location])


def underground():
    output(ENTERING_UNDERGROUND)
    select_location()


def start_location():
    output(START_LOCATION_TEXT)
    input_four([SHOP, TAVERN, UNDERGROUND, LEADERS_TABLE], [shop, tavern, underground, liders_table])


def shop_weapon():
    bought_tovar_list = buy(weapon_dict, [WEAPON_ASSORTIMENT, CHOICE_WHAT_TO_BUY], weapons=True)
    if bought_tovar_list[0]:
        pl.weapon = bought_tovar_list[1]


def shop_armor():
    bought_tovar_list = buy(armor_dict, [ARMOR_ASSORTIMENT, CHOICE_WHAT_TO_BUY], armor=True)
    if bought_tovar_list[0]:
        pl.armor = bought_tovar_list[1]


def shop_amulets():
    bought_tovar_list = buy(amulets_dict, [AMULETS_ASSORTIMENT, CHOICE_WHAT_TO_BUY], amulets=True)
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
    input_two([YES, NO], [tubes_happening_choice, start_location])


def caves():
    output(ENTERING_CAVES)
    input_two([YES, NO], [caves_happening_choice, start_location])


def catacombs():
    output(ENTERING_CATACOMBS)
    input_two([YES, NO], [catacombs_happening_choice, start_location])


def hell_tower():
    output(HELLTOWER_UNACTIVE)


get_tavern_and_startloc(tavern, start_location)
get_start_location(start_location)