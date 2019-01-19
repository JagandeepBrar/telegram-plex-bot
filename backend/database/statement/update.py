import sqlite3
import datetime
from backend import constants

###############
# USERS TABLE #
###############

# Update a user's data already in the database
def updateUser(telegram, status, detail, ombi, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ?, name = ?, status = ?, detail = ? WHERE telegram_id = ?', (ombi, name, status, detail, telegram))
    db.commit()
    db.close()

# Update a user's status
def updateUserStatus(telegram, status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET status = ? WHERE telegram_id = ?', (status, telegram))
    db.commit()
    db.close()

# Update a user's detail preference
def updateUserDetail(telegram, detail):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET detail = ? WHERE telegram_id = ?', (detail, telegram))
    db.commit()
    db.close()

# Update a user's ombi ID
def updateUserOmbi(telegram, ombi):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ? WHERE telegram_id = ?', (ombi, telegram))
    db.commit()
    db.close()

###############
# SHOWS TABLE #
###############

# Update a TV show's name that is already in the database
def updateTV(tvdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE television SET name = ? WHERE tvdb_id = ?', (name, tvdb))
    db.commit()
    db.close()

################
# MOVIES TABLE #
################

# Update a movie's name that is already in the database
def updateMovie(tmdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE movies SET name = ? WHERE tmdb_id = ?', (name, tmdb))
    db.commit()
    db.close()

##################
# NOTIFIER TABLE #
##################

def updateNotifierFrequency(watch_id, freq):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE notifiers SET frequency = ? WHERE watch_id = ?', (freq, watch_id))
    db.commit()
    db.close()