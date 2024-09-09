import sqlite3
import random
import string
from database import connect_db


def generate_unique_key():
    # Generate a random 16-character string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Query to authenticate user
    cursor.execute('''
        SELECT id FROM tb_users WHERE username = ? AND password = ?
    ''', (username, password))

    user = cursor.fetchone()

    if user:
        user_id = user[0]
        # Generate a new unique key
        unique_key = generate_unique_key()

        # Update the unique_key for the authenticated user
        cursor.execute('''
            UPDATE tb_users
            SET unique_key = ?
            WHERE id = ?
        ''', (unique_key, user_id))

        conn.commit()
        conn.close()

        return unique_key
    else:
        conn.close()
        return None
