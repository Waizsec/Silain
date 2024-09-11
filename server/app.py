from flask import Flask, g, request, jsonify
import sqlite3
import database
import auth
import data_prepro_sql

app = Flask(__name__)


@app.route('/')
def index():
    db = database.connect_db()
    database.init_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    # data_prepro_sql.run_sql()
    return f"Tables in the database: {tables}"


# API Data
@app.route('/data-ikan-berdasarkan-jenis-ikan-tangkap-laut', methods=['GET'])
def data_ikan_tangkap_laut():
    # Connect to the database
    db = database.connect_db()
    cursor = db.cursor()

    query = '''
    SELECT 
        CASE 
            WHEN length(p."Province Name") > 0 THEN 
                upper(substr(p."Province Name", 1, 1)) || lower(substr(p."Province Name", 2))
            ELSE 
                p."Province Name"
        END AS province_name,
        d."Jenis Ikan Name" AS jenis_ikan,
        f."Nilai Produksi" AS total_value
    FROM 
        fact_jumlah_produksi_ikan_jenis_ikan_tangkap_laut f
    JOIN 
        dim_jenis_ikan d ON f."Jenis Ikan" = d."Jenis Ikan Code"
    JOIN 
        dim_province p ON f."Province" = p."Province Code"
    WHERE
        p."Province Name" IS NOT NULL AND
        f."Jenis Ikan" IS NOT NULL
    GROUP BY 
        p."Province Name", 
        f."Jenis Ikan"
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Convert rows to list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the database connection
    db.close()

    # Return the result as JSON
    return jsonify(result)


@app.route('/data-ikan-berdasarkan-medan', methods=['GET'])
def data_ikan_medan():
    # Connect to the database
    db = database.connect_db()
    cursor = db.cursor()

    # SQL query to fetch the data
    query = '''
    SELECT 
        f."Value" AS total_value,
        f."Year",
        CASE 
            WHEN length(p."Province Name") > 0 THEN 
                upper(substr(p."Province Name", 1, 1)) || lower(substr(p."Province Name", 2))
            ELSE 
                p."Province Name"
        END AS province_name,
        m."Location Name" AS location_name
    FROM 
        fact_jumlah_produksi_ikan_medan f
    JOIN 
        dim_province p ON f."Province" = p."Province Code"
    JOIN 
        dim_location m ON f."Location" = m."Location Code"
    WHERE
        p."Province Name" IS NOT NULL AND
        m."Location Name" IS NOT NULL
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Convert rows to list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the database connection
    db.close()

    # Return the result as JSON
    return jsonify(result)


@app.route('/data-ikan-berdasarkan-metode', methods=['GET'])
def data_ikan_metode():
    # Connect to the database
    db = database.connect_db()
    cursor = db.cursor()

    # SQL query to join tables and select the required columns
    query = '''
        SELECT
            f."Year" AS year,
            CASE 
                WHEN length(p."Province Name") > 0 THEN 
                    upper(substr(p."Province Name", 1, 1)) || lower(substr(p."Province Name", 2))
                ELSE 
                    p."Province Name"
            END AS province,
            m."Method Name" AS method,
            f."Value" AS value
        FROM
            fact_jumlah_produksi_ikan_metode f
        JOIN
            dim_province p ON f."Province" = p."Province Code"
        JOIN
            dim_method m ON f."Method" = m."Method Code"
        WHERE
            f."Value" IS NOT NULL
        '''

    # Execute the query
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Convert rows to list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the database connection
    db.close()

    # Return the result as JSON
    return jsonify(result)


@app.route('/data-ikan-berdasarkan-wilayah', methods=['GET'])
def data_ikan_wilayah():
    # Connect to the database
    db = database.connect_db()
    cursor = db.cursor()

    # SQL query to fetch the data, excluding rows with null or empty category_name and province_name
    query = '''
    SELECT 
        c."Category Name" AS category_name, 
        CASE 
            WHEN length(p."Province Name") > 0 THEN 
                upper(substr(p."Province Name", 1, 1)) || lower(substr(p."Province Name", 2))
            ELSE 
                p."Province Name"
        END AS province_name,
        SUM(f."Value") AS total_value, 
        f."Year"
    FROM 
        fact_jumlah_produksi_ikan_wilayah f
    JOIN 
        dim_category c ON f."Category" = c."Category Code"
    JOIN 
        dim_province p ON f."Province" = p."Province Code"
    WHERE
        c."Category Name" IS NOT NULL AND
        p."Province Name" IS NOT NULL AND
        f."Year" IN ('2018', '2019', '2020')
    GROUP BY
        c."Category Name", 
        p."Province Name",
        f."Year"
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Convert rows to list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the database connection
    db.close()

    # Return the result as JSON
    return jsonify(result)


# Authentifikasi
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        unique_key, user_username = auth.login(username, password)

        if unique_key:
            return jsonify({'unique_key': unique_key, 'username': user_username})
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return jsonify({'error': 'Username and password required'}), 400


@app.route('/verify_key', methods=['POST'])
def verify_key():
    unique_key = request.form.get('unique_key')
    valid = auth.verify_key(unique_key)
    return jsonify({'valid': valid})


# Database
@app.route('/drop', methods=['GET'])
def drop():
    database.drop_tables()
    return "Succed"


@app.route('/deleteuser', methods=['GET'])
def delete_users():
    # Connect to the database
    return auth.deleteuser()


@app.route('/createuser', methods=['GET'])
def create_user():
    return auth.create_user()


if __name__ == '__main__':
    app.run(debug=True)
