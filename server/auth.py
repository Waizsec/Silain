import sqlite3
import random
import string
from database import connect_db


def generate_unique_key():
    # Generate a random 16-character string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def verify_key(key):
    conn = connect_db()  # Make sure this function correctly returns a valid connection object
    cursor = conn.cursor()

    # Check if the unique_key exists in the database
    cursor.execute('''
        SELECT 1 FROM tb_users WHERE unique_key = ?
    ''', (key,))  # Add a comma to make it a tuple

    exists = cursor.fetchone() is not None

    conn.close()

    return exists


def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Query to authenticate user and get the id and username
    cursor.execute('''
        SELECT id, username FROM tb_users WHERE username = ? AND password = ?
    ''', (username, password))

    user = cursor.fetchone()

    if user:
        user_id, user_username = user
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

        return unique_key, user_username
    else:
        conn.close()
        return None, None


def create_user():
    # Hardcoded username and password
    username = 'Anan'
    password = '123'

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Check if the user already exists
        cursor.execute(
            'SELECT id FROM tb_users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Delete the existing user
            cursor.execute(
                'DELETE FROM tb_users WHERE username = ?', (username,))

        # Insert the new user into the tb_users table
        cursor.execute('''
            INSERT INTO tb_users (username, password, unique_key)
            VALUES (?, ?, ?)
        ''', (username, password, ''))

        conn.commit()
        conn.close()

        return f"User '{username}' created successfully."

    except sqlite3.IntegrityError:
        conn.close()
        return f"User '{username}' already exists.", 400
