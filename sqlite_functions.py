import sqlite3
con = sqlite3.connect('db_players.db')
cur = con.cursor()


def get_everything():
    return cur.execute("""SELECT * from players""").fetchall()


def add_player(login, password):
    cur.execute("""INSERT INTO player VALUES (?, ?)""", (login, password))
    con.commit()

