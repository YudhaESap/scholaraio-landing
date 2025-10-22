"""
auth.py

This module provides simple user account management functions for the ScholarAIO platform.
The functions here are stubs for creating and authenticating users, and storing user profiles.
In a real production system, you would integrate with a proper database and authentication
framework. These functions are intended as a placeholder for Step 3 (User Accounts & Data Storage).
"""

import sqlite3
from typing import Optional

DB_PATH = "users.db"

def init_db():
    """Initialize a simple SQLite database for storing user accounts."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()

def register_user(username: str, email: str, password_hash: str) -> bool:
    """
    Register a new user with username, email and hashed password.

    Args:
        username (str): The desired username.
        email (str): The user's email address.
        password_hash (str): A hashed version of the user's password.

    Returns:
        bool: True if registration succeeded, False if user/email already exists.
    """
    init_db()
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                  (username, email, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Username or email already exists
        return False
    finally:
        conn.close()

def authenticate_user(username: str, password_hash: str) -> bool:
    """
    Authenticate a user based on username and hashed password.

    Args:
        username (str): The username.
        password_hash (str): A hashed version of the user's password.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row and row[0] == password_hash:
        return True
    return False
