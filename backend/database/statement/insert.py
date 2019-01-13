import sqlite3
from backend import constants

# Insert a new user into the database
def insertUser(telegram, name, verification):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO users(telegram_id, ombi_id, status, name) VALUES (?, ?, ?, ?)', (telegram, None, verification, name))
    db.commit()
    db.close()

# Insert a new TV series
def insertTV(tvdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO shows(tvdb_id, name) VALUES (?, ?)', (tvdb, name))
    db.commit()
    db.close()

# Insert a new movie
def insertMovie(tmdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO movies(tmdb_id, name) VALUES (?, ?)', (tmdb, name))
    db.commit()
    db.close()
