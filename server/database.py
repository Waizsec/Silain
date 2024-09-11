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


def drop_tables():
    # Replace with your actual database path
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # List of tables to drop
    tables = [
        'fact_nilai_produksi_provinsi_dan_jenis',
        'fact_nilai_produksi_perikanan_tangkap_perairan_umum',
        'fact_produksi_nilai_produksi_perikanan_tangkap_laut',
        'fact_produksi_perikanan_tangkap',
        'fact_produksi_perikanan_jenis_ikan_tangkap_laut',
        'dim_province',
        'dim_category',
        'dim_jenis_ikan',
        'dim_location',
        'dim_method'
    ]

    # Loop through tables and drop them
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

    conn.commit()
    conn.close()


# Main entry to initialize the database, can be run directly if needed
if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
