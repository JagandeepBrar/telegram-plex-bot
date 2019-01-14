import sqlite3
from backend import constants

###############
# SHOWS TABLE #
###############

def deleteTV(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('DELETE FROM shows WHERE tvdb_id = ?', (id,))
    db.commit()
    db.close()

################
# MOVIES TABLE #
################

def deleteMovie(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('DELETE FROM movies WHERE tmdb_id = ?', (id,))
    db.commit()
    db.close()
