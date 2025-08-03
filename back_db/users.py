"""Working with Users database"""

import sqlite3
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_login import UserMixin
from config import DB_PATH


class UserLoginWrapper(UserMixin):
    """User-from-db object"""
    def __init__(self, _id, username, password_hash):
        """User objecdt appears with db' params"""
        self.id = str(_id)
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password):
        """Checks if the input's password is correct"""
        return check_password_hash(
            self.password_hash, password)

    @staticmethod
    def get(user_id):
        """Returns the User-from-db by user-id"""
        return get_user_by_id(user_id)


def init_db():
    """Creates Users table if not exists"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)
        conn.commit()


def get_user_by_username(
        username: str
        ) -> UserLoginWrapper | None:
    """Returns the user from the DB by login"""
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            """SELECT id,
                username,
                password_hash
            FROM users
            WHERE username = ?""",
            (username,)
        ).fetchone()
        return UserLoginWrapper(
            *row) if row else None


def get_user_by_id(user_id):
    """Returns the user from the DB by id"""
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            """
            SELECT id,
                username,
                password_hash
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        ).fetchone()
        return UserLoginWrapper(
            *row) if row else None


def create_user(
        username: str,
        password: str
        ) -> bool:
    """Creates new user in the Users DB"""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                """
                INSERT INTO
                    users
                    (username, password_hash)
                VALUES (?, ?)
                """,
                (username,
                 generate_password_hash(password))
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False
