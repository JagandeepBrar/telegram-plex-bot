import sqlite3
import logging
from backend import constants

def initialize():
    db = sqlite3.connect(constants.DB_FILE) 
    db_cursor = db.cursor()
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY,
            status INTEGER,
            frequency INTEGER,
            detail INTEGER,
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
            desc TEXT,
            FOREIGN KEY(telegram_id) REFERENCES users ON DELETE CASCADE
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS metadata_television(
            metadata_id TEXT PRIMARY KEY,
            tvdb_id INTEGER,
            type TEXT,
            title TEXT,
            episode_desc TEXT,
            season TEXT,
            episode TEXT,
            download_time TEXT,
            quality TEXT,
            FOREIGN KEY(tvdb_id) REFERENCES television ON DELETE CASCADE
        )"""
    )
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS metadata_movies(
            metadata_id TEXT PRIMARY KEY,
            tmdb_id INTEGER,
            title TEXT,
            download_time TEXT,
            quality TEXT,
            FOREIGN KEY(tmdb_id) REFERENCES movies ON DELETE CASCADE
        )"""
    )
    db.commit()
    db.close()
    logging.getLogger(__name__).info("Database tables created/loaded")