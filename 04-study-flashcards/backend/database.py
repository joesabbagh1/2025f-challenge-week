"""MySQL database helper for Study Flashcards."""

import os
import mysql.connector

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "study_flashcards"),
}


def get_db(db_name: str | None = None):
    """Get a database connection."""
    config = dict(DB_CONFIG)
    if db_name:
        config["database"] = db_name
    return mysql.connector.connect(**config)


def init_db(db_name: str | None = None):
    """Initialize the database schema."""
    config_no_db = {k: v for k, v in DB_CONFIG.items() if k != "database"}
    target_db = db_name or DB_CONFIG["database"]
    conn = mysql.connector.connect(**config_no_db)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {target_db}")
    cursor.close()
    conn.close()

    config = dict(DB_CONFIG)
    config["database"] = target_db
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS decks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INT AUTO_INCREMENT PRIMARY KEY,
            deck_id INT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            difficulty INT DEFAULT 1,
            last_reviewed VARCHAR(30),
            FOREIGN KEY (deck_id) REFERENCES decks(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
