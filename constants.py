# -*- coding: utf-8 -*-

# Константы, содержащие текст для оформления (вывода)
SUCCESSFUL_START = '\n\nDnDnD успешно запустилась. Приятной игры!'
ENTERING_TUBES = 'Вы подходите ко входу в Канализацию. Это верхний уровень Подземелья, самый лёгкий. Войти?'
ENTERING_CAVES = 'Вы подходите ко входу в Пещеры. Это средний уровень Подземелья. Монстры здесь на порядок сильнее ' \
                 'монстров из Канализации. Войти?'
ENTERING_CATACOMBS = 'Вы подходите ко входу в Катакомбы. Это самый глубокий уровень Подземелья. Монстры' \
                     'здесь настолько сильные, что даже опытные искатели побаиваются сюда заходить. Войти?'
ENTERING_SHOP = 'Вы пришли в магазин. Тут продается оружие, броня и амулеты. Искатели приходят сюда, чтобы купить' \
                'себе аммуницию для похода в Подземелье'
ENTERING_TAVERN = 'Вы пришли в таверну. Тут люди пьют различные напитки, играют в игры и иногда передают друг другу ' \
                  'монеты'
ENTERING_UNDERGROUND = 'Вы спускаетесь в Подземелье...'
START_LOCATION_TEXT = 'Перед Вами встал выбор: пойти в магазин, в таверну или отправиться в атаку'
SELECT_LOCATION = 'Выберите локацию'
HELLTOWER_UNACTIVE = 'Вы подходите к Адской Башне. Она сейчас неактивна, и сразиться с боссом не получится. Увы!'
CHOICE_WHAT_TO_BUY = 'Выберите, что хотите купить'
WEAPON_ASSORTIMENT = 'Оружейный ассортимент'
ARMOR_ASSORTIMENT = 'Ассортимент брони'
AMULETS_ASSORTIMENT = 'Ассортимент амулетов'
NOT_ENOUGH_MONEY = 'Недостаточно монет!'
GO_FURTHER = 'Вы хотели бы пойти дальше?'
DONT_HAVE_ELIXIRS = 'У вас нет эликсиров!'
DONT_HAVE_POTIONS = 'У вас нет зелий!'
FULLY_HEALED = 'Ваши раны затянулись'
GAME_OVER = 'Игра окончена!'
YOU_DEAD = 'Вы умерли! Игра окончена!'
TAVERN_HEAL_TEXT = 'Есть выбор: зелье за 120 монет, которое полностью вылечит вас в бою, эликсир за 60 монет, который' \
                   ' восстановит ваше здоровье на четверть от максимального или мгновенное исцеление здесь и сейчас з' \
                   'а 60 монет'
TO_WHO_GIVE = 'Кому передать?'
INPUT_WHO_GIVE = 'Введите логин пользователя, с которым хотите поделиться монетами'
HOW_MANY_GIVE = 'Сколько передать?'
INPUT_HOW_MANY_GIVE = 'Введите количество монет'
NO_USER = 'Нет такого пользователя!'
CONGRATS = 'Поздравляем с покупкой'
DONT_HAVE_AMULET = 'У вас нет амулета'

# Константы, содержащие текст кнопок
WEAPON = 'Оружие'
ARMOR = 'Броня'
AMULETS = 'Амулеты'
LEAVE = 'Уйти'
GAMES = 'Азартные игры'
DRINKS = 'Взять выпивки'
GIVE_MONEY = 'Передать монеты'
TUBES = 'Канализация'
CAVES = 'Пещеры'
CATACOMBS = 'Катакомбы'
HELLTOWER = 'Адская башня'
YES = 'Да'
NO = 'Нет'
SHOP = 'Магазин'
TAVERN = 'Таверна'
UNDERGROUND = 'Подземелье'
LEADERS_TABLE = 'Таблица лидеров'
ELIXIR = 'Эликсир'
POTION = 'Зелье'
ELIXIRS = 'Эликсиры'
POTIONS = 'Зелья'
CANCEL = 'Отмена'
ATTACK = 'Атака'
HEAL = 'Лечение'

# Константы, содержащие названия товаров
AXE = 'Топор'
SHORT_SWORD = 'Короткий меч'
CEP = 'Цеп'
MACE = 'Булава'
MID_SWORD = 'Средний меч'
LONG_SWORD = 'Длинный меч'
ALEBARD = 'Алебарда'
CLAYMORE = 'Клеймор'
SWORD_OF_DOOM = 'Меч Судеб'
ARMAGEDDON_SWORD = 'Клинок Армагеддона'
LEATHER_ARMOR = 'Кожаная броня'
HARDENED_LEATHER_ARNOR = 'Кожаная броня с металлическими вставками'
IRON_ARMOR = 'Железная броня'
STEEL_ARMOR = 'Стальная броня'
MAGIC_STEEL_ARMOR = 'Магически усиленная стальная броня'
MYTHRIL_ARMOR = 'Мифриловая броня'
ARMAGEDDON_ARMOR = 'Доспех Армагеддона'
REGEN_STONE = 'Камень регенерации'
BIG_REGEN_STONE = 'Большой камень регенерации'
DEFENCE_STONE = 'Камень защиты'
AMULET_OF_CULTIST = 'Религиозный амулет культиста'

# Константы, содержащие названия действий амулетов (искл. DEFENCE ещё и название кнопки)
REGENERATION = 'регенерация'
DEFENCE = 'Защита'
PLUS_DAMAGE = 'доп.урон'

# Константы, содержащие запросы в базу данных
GET_ALL_QUERY = 'SELECT * FROM players'
ADD_PLAYER_QUERY = 'INSERT INTO players(login, password) VALUES (?, ?)'
CHANGE_PLAYER_QUERY = """UPDATE players SET 
                    money = ?, points = ?, weapon = ?, armor = ?, amulet = ?, health = ?, level = ?,
                    exp = ?, elixirs = ?, potions = ?, dead = ?
                   WHERE login LIKE ?"""
GET_PLAYER_BY_LOGIN_QUERY = 'SELECT * FROM players WHERE login LIKE ?'
ADD_MONEY_QUERY = 'UPDATE players SET money = ? WHERE login LIKE ?'

# Константы с текстом ошибок
LOGIN_INPUT = 'Введите логин!'
LOGIN_ISNT_UNIQUE = 'Логин занят!'
WRONG_LOGIN = 'Неверный логин!'
PASSWORD_INPUT = 'Введите пароль!'
WRONG_PASSWORD = 'Пароль неверный!'
PLAYER_IS_DEAD = 'Игрок уже умер. Создайте новый профиль'

# Служебные константы
NOTHING = 'Ничего'
NO_OUTPUT = 'Вывод не нужен'
MONSTER_DEFEATED = 'Монстр повержен'
SOME_MONEY_MIN = 1  # Минимальное значение события "Немного денег"
SOME_MONEY_MAX = 6  # Максимальное значение события "Немного денег"
MUCH_MONEY_MIN = 10  # Минимальное значение события "Много денег"
MUCH_MONEY_MAX = 60  # Максимальное значение события "Много денег"
EXPERIENCE_MULTIPLIER = 20  # Значение, на которое возрастает количество опыта, необходимое для перехода на другой
#                                                                                                                уровень
MAXHEALTH_PLUS = 10  # Значение, на которое возрастает maxhealth каждый уровень
EVERY_THIS_LEVEL_BOOST_PLUS = 5  # Если уровень, на который переходит игрок, кратен этому числу, увеличивается boost
BOOST_PLUS = 0.01  # На это значение увеличивается boost каждые EVERY_THIS_LEVEL_BOOST_PLUS уровней
MAX = 'max'
POTION_COST = 120  # Стоимость зелий
ELIXIR_COST = 60  # Стоимость эликсиров
HEAL_COST = 60  # Стоимость лечения
# Список с изображениями граней игрального кубика
DICE_IMAGES = ['1_dot.png', '2_dots.png', '3_dots.png', '4_dots.png', '5_dots.png', '6_dots.png']
DICES_WIN = 100  # Сумма выигрыша при броске костей
DICES_WIN_TEXT = 'Вы выиграли 100 монет'  # Текст при выигрыше в кости
DICES_LOSE = 20  # Сумма проигрыша при броске костей
DICES_LOSE_TEXT = 'Вы програли 20 монет'  # Текст при проигрыше в кости

# Константы с названиями монстров
RAT = 'крыса'
GNOLL = 'гнолл'
CRAB = 'краб'
SKELETON = 'скелет'
FANTOM = 'фантом'
BAT = 'летучая мышь'
SPIDER = 'паук'
RAT_KING = 'крысиный король'
EVIL_EYE = 'око зла'

# Списки монстров для каждой локации
TUBES_MONSTERS_LIST = [RAT, RAT, RAT, RAT, RAT, RAT, GNOLL, GNOLL, GNOLL, CRAB]
CAVES_MONSTERS_LIST = [SKELETON, SKELETON, SKELETON, SKELETON, SKELETON, SKELETON, SKELETON, FANTOM, FANTOM,
                       FANTOM, FANTOM, BAT, BAT, BAT]
CATACOMBS_MONSTERS_LIST = [SPIDER, SPIDER, SPIDER, SPIDER, SPIDER, SPIDER, SPIDER, RAT_KING, RAT_KING, RAT_KING,
                           RAT_KING, EVIL_EYE, EVIL_EYE]

# Константы с текстом событий в Подземелье
SOME_MONEY = 'немного денег'
MUCH_MONEY = 'много денег'
MONSTER = 'монстр'

# Словарь со списком характеристик монстров (чтобы создавать новый экземпляр класса Monster)
MONSTERS_DICT = {
    RAT: [RAT, (1, 3), 4, (24, 2), 'images/rat.png'],
    GNOLL: [GNOLL, (4, 8), 10, (45, 4), 'images/gnoll.png'],
    CRAB: [CRAB, (2, 5), 50, (90, 6), 'images/crab.png'],
    SKELETON: [SKELETON, (10, 15), 20, (90, 4), 'images/skeleton.png'],
    FANTOM: [FANTOM, (6, 10), 100, (90, 6), 'images/fantom.png'],
    BAT: [BAT, (12, 17), 40, (150, 8), 'images/bat.png'],
    SPIDER: [SPIDER, (30, 50), 50, (300, 12), 'images/spider.png'],
    RAT_KING: [RAT_KING, (25, 40), 150, (600, 14), 'images/rat_king.png'],
    EVIL_EYE: [EVIL_EYE, (60, 70), 100, (900, 20), 'images/evil_eye.png']
}

# Список событий в Подземелье
HAPPENINGS_LIST = [MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER,
                   SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, SOME_MONEY, MUCH_MONEY]
