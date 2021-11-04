import sqlite3
con = sqlite3.connect('db_players.db')
cur = con.cursor()


def get_all_players():
    return cur.execute("""SELECT * from players""").fetchall()


def add_player(login, password):
    cur.execute("""INSERT INTO players(login, password) VALUES (?, ?)""", (login, password))
    con.commit()


def change_player(login, pl, dead=False):
    weapon = pl.weapon.name + ', ' + str(pl.weapon.damage) + ', ' + str(pl.weapon.price)
    armor = pl.armor.name + ', ' + str(pl.armor.defence) + ', ' + str(pl.armor.price)
    amulet = pl.amulet.name + ', ' + str(pl.amulet.action) + ', ' + str(pl.amulet.price) + ', ' + str(pl.amulet.power)
    cur.execute("""UPDATE players SET \n
                    money = ?, points = ?, weapon = ?, armor = ?, amulet = ?, health = ?, level = ?,
                    exp = ?, elixirs = ?, potions = ?, dead = ?
                   WHERE login LIKE ?""", (pl.money, pl.points, weapon, armor, amulet, pl.health, pl.level, pl.exp,
                                        pl.elixirs, pl.potions, dead, login))
    con.commit()


def get_player_by_login(login):
    return cur.execute("""SELECT * FROM players WHERE login LIKE ?""", (login,)).fetchall()


def add_player_money(login, n):
    player = get_player_by_login(login)[0]
    new_money = player[6] + n
    cur.execute("""UPDATE players SET money = ? WHERE login LIKE ?""", (new_money, login))
    con.commit()
