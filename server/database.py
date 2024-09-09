import sqlite3

# Path to your SQLite database file
DATABASE = 'database.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Creating the tb_users table with id, username, password, and unique_key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            unique_key TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()


# Main entry to initialize the database, can be run directly if needed
if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
