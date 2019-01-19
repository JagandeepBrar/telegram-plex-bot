import sqlite3
import datetime
from backend import constants

###############
# USERS TABLE #
###############

# Insert a new user into the database
def insertUser(telegram, status, detail, ombi, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO users(telegram_id, status, detail, ombi_id, name) VALUES (?, ?, ?, ?, ?)', (telegram, status, detail, ombi, name))
    db.commit()
    db.close()

###############
# SHOWS TABLE #
###############

# Insert a new TV series
def insertTV(tvdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO television(tvdb_id, name) VALUES (?, ?)', (tvdb, name))
    db.commit()
    db.close()

################
# MOVIES TABLE #
################

# Insert a new movie
def insertMovie(tmdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO movies(tmdb_id, name) VALUES (?, ?)', (tmdb, name))
    db.commit()
    db.close()

###################
# NOTIFIERS TABLE #
###################

def insertNotifier(id, telegram, media_id, media_type, frequency, desc):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO notifiers(watch_id, telegram_id, media_id, media_type, frequency, desc) VALUES (?, ?, ?, ?, ?, ?)', (id, telegram, media_id, media_type, frequency, desc))
    db.commit()
    db.close()