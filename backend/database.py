import sqlite3

def initialize():
    initTables()

def initTables():
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('CREATE TABLE IF NOT EXISTS users(telegram_id INTEGER PRIMARY KEY, ombi_id TEXT, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS shows(tvdb_id INTEGER PRIMARY KEY, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS movies(tmdb_id INTEGER PRIMARY KEY, name TEXT)')
    db_cursor.execute('CREATE TABLE IF NOT EXISTS notifications(notification_id INTEGER PRIMARY KEY, telegram_id INTEGER, media_id INTEGER, media_type INTEGER, desc TEXT, FOREIGN KEY(telegram_id) REFERENCES users ON DELETE CASCADE)')
    db.commit()
    db.close()
    
def insertUser(telegram, ombi, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO users(telegram_id, ombi_id, name) VALUES (?, ?, ?)', (telegram, ombi, name))
    db.commit()
    db.close()

def updateUser(telegram, ombi, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ?, name = ? WHERE telegram_id = ?', (ombi, name, telegram))
    db.commit()
    db.close()

def insertTV(tvdb, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO shows(tvdb_id, name) VALUES (?, ?)', (tvdb, name))
    db.commit()
    db.close()

def insertMovie(tmdb, name):
    db = sqlite3.connect('database.db')
    db_cursor = db.cursor()
    db_cursor.execute('INSERT OR IGNORE INTO movies(tmdb_id, name) VALUES (?, ?)', (tmdb, name))
    db.commit()
    db.close()