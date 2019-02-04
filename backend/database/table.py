import sqlite3
from backend import constants, logger

def initialize():
    db = sqlite3.connect(constants.DB_FILE) 
    db_cursor = db.cursor()
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY,
            status INTEGER,
            detail INTEGER,
            upgrade INTEGER,
            ombi_id TEXT,
            name TEXT
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS television(
            tvdb_id INTEGER PRIMARY KEY,
            name TEXT
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
            tmdb_id INTEGER PRIMARY KEY,
            name TEXT
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS notifiers(
            watch_id TEXT PRIMARY KEY,
            telegram_id INTEGER,
            media_id INTEGER,
            media_type INTEGER,
            frequency INTEGER,
            desc TEXT,
            FOREIGN KEY(telegram_id) REFERENCES users ON DELETE CASCADE
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS metadata_television(
            metadata_id TEXT PRIMARY KEY,
            tvdb_id INTEGER,
            show_title TEXT,
            show_type TEXT,
            episode_title TEXT,
            season TEXT,
            episode TEXT,
            quality TEXT,
            quality_version TEXT,
            is_upgrade INTEGER,
            download_time FLOAT,
            FOREIGN KEY(tvdb_id) REFERENCES television ON DELETE CASCADE
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS metadata_movies(
            metadata_id TEXT PRIMARY KEY,
            tmdb_id INTEGER,
            movie_title TEXT,
            quality TEXT,
            quality_version TEXT,
            is_upgrade INTEGER,
            download_time FLOAT,
            FOREIGN KEY(tmdb_id) REFERENCES movies ON DELETE CASCADE
        )"""
    )
    db.commit()
    db.close()
    logger.info(__name__, "Database tables created/loaded")