import sqlite3

# Update a user's data already in the database
def updateUser(telegram, ombi, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ?, name = ? WHERE telegram_id = ?', (ombi, name, telegram))
    db.commit()
    db.close()

# Update a TV show's name that is already in the database
def updateTV(tvdb, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE shows SET name = ? WHERE tvdb_id = ?', (name, tvdb))
    db.commit()
    db.close()

# Update a movie's name that is already in the database
def updateMovie(tmdb, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE movies SET name = ? WHERE tmdb_id = ?', (name, tmdb))
    db.commit()
    db.close()
