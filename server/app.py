from flask import Flask, g, request, jsonify
import sqlite3
import database
import auth

app = Flask(__name__)


@app.route('/')
def index():
    db = database.connect_db()
    database.init_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return f"Tables in the database: {tables}"


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        unique_key = auth.authenticate_user(username, password)

        if unique_key:
            return jsonify({'unique_key': unique_key})
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return jsonify({'error': 'Username and password required'}), 400


@app.route('/verify_key', methods=['POST'])
def verify_key():
    unique_key = request.form.get('unique_key')

    conn = database.connect_db()
    cursor = conn.cursor()

    # Check if the unique_key exists in the database
    cursor.execute('''
        SELECT 1 FROM tb_users WHERE unique_key = ?
    ''', (unique_key,))
    exists = cursor.fetchone() is not None

    conn.close()

    return jsonify({'valid': exists})


@app.route('/createuser', methods=['GET'])
def create_user():
    # Hardcoded username and password
    username = 'wisnu'
    password = '123'

    conn = database.connect_db()
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


if __name__ == '__main__':
    app.run(debug=True)
