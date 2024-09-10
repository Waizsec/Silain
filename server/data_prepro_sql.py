import sqlite3
from bs4 import BeautifulSoup
import pandas as pd


def run_sql():
    # Load the data from the Excel file
    df = pd.read_excel('data/Nilai Produksi Perikanan Budidaya Menurut Provinsi dan Jenis Budidaya, 2017-2019.xlsx',
                       sheet_name=0,
                       skiprows=4)  # Skip the first 4 rows to use the 5th row as header

    # Rename columns for clarity
    df.columns = ['Province', 'Jaring Apung Laut 2019', 'Jaring Apung Laut 2018', 'Jaring Apung Laut 2017',
                  'Jaring Apung Tawar 2019', 'Jaring Apung Tawar 2018', 'Jaring Apung Tawar 2017',
                  'Jaring Tancap Tawar 2019', 'Jaring Tancap Tawar 2018', 'Jaring Tancap Tawar 2017',
                  'Karamba 2019', 'Karamba 2018', 'Karamba 2017',
                  'Kolam Air Deras 2019', 'Kolam Air Deras 2018', 'Kolam Air Deras 2017',
                  'Kolam Air Tenang 2019', 'Kolam Air Tenang 2018', 'Kolam Air Tenang 2017',
                  'Laut Lainnya 2019', 'Laut Lainnya 2018', 'Laut Lainnya 2017',
                  'Minapadi Sawah 2019', 'Minapadi Sawah 2018', 'Minapadi Sawah 2017',
                  'Rumput Laut 2019', 'Rumput Laut 2018', 'Rumput Laut 2017',
                  'Tambak Intensif 2019', 'Tambak Intensif 2018', 'Tambak Intensif 2017',
                  'Tambak Sederhana 2019', 'Tambak Sederhana 2018', 'Tambak Sederhana 2017',
                  'Tambak Semi Intensif 2019', 'Tambak Semi Intensif 2018', 'Tambak Semi Intensif 2017',
                  'Jumlah 2019', 'Jumlah 2018', 'Jumlah 2017']

    df = df.iloc[:-1, :-3]

    # Drop rows where 'Province' is NaN
    df = df.dropna(subset=['Province'])

    # Melt the DataFrame to long format
    data1 = df.melt(id_vars=['Province'],
                    var_name='Variable',
                    value_name='Value')

    # Extract the Method and Year from the 'Variable' column
    data1[['Method', 'Year']] = data1['Variable'].str.extract(r'(.+) (\d{4})')

    # Drop the original 'Variable' column
    data1 = data1.drop(columns=['Variable'])

    # Display the final DataFrame
    data1

    """# **Prepro 2**

    ## Nilai Produksi Perikanan Tangkap di Perairan Umum Menurut Lokasi, 2017-2019
    """

    # Load the data from the CSV file
    # Skip the first 4 rows to use the 5th row as header
    df = pd.read_csv(
        'data/Nilai Produksi Perikanan Tangkap di Perairan Umum Menurut Lokasi, 2017-2019.csv',)

    # Rename columns for clarity based on the expected structure
    df.columns = ['Province', 'Waduk 2019', 'Waduk 2018', 'Sungai 2019', 'Sungai 2018',
                  'Danau 2019', 'Danau 2018', 'Rawa 2019', 'Rawa 2018', 'Genangan Air 2019', 'Genangan Air 2018',
                  'Waduk 2017', 'Sungai 2017', 'Danau 2017', 'Rawa 2017', 'Genangan Air 2017']

    # Drop rows and columns where all values are NaN or irrelevant
    df = df.dropna(subset=['Province']).reset_index(drop=True)

    # Melt the DataFrame to long format
    data2 = df.melt(id_vars=['Province'],
                    var_name='Variable',
                    value_name='Value')

    # Extract the Method and Year from the 'Variable' column
    data2[['Location', 'Year']] = data2['Variable'].str.extract(
        r'(.+) (\d{4})')

    # Drop the original 'Variable' column
    data2 = data2.drop(columns=['Variable'])

    # Replace NaN values with 0
    data2['Value'] = data2['Value'].fillna(0)

    # Display the final DataFrame
    data2

    """# **Prepro 3**

    ## Produksi dan Nilai Produksi Perikanan Tangkap di Laut Menurut Provinsi dan Komoditas Utama, 2022
    """

    # Load the data from the Excel file
    file_path = 'data/Produksi dan Nilai Produksi Perikanan Tangkap di Laut Menurut Provinsi dan Komoditas Utama, 2022.xlsx'
    # Adjust skiprows if needed
    data3 = pd.read_excel(file_path, sheet_name=0, skiprows=0)

    # Rename columns for clarity
    data3.columns = [
        'Province',
        'Produksi Cakalang (ton)',
        'Nilai Cakalang (Rp)',
        'Produksi Tongkol (ton)',
        'Nilai Tongkol (Rp)',
        'Produksi Tuna (ton)',
        'Nilai Tuna (Rp)',
        'Produksi Udang (ton)',
        'Nilai Udang (Rp)',
        'Produksi Lainnya (ton)',
        'Nilai Lainnya (Rp)',
        'Produksi Total (ton)',
        'Nilai Total (Rp)'
    ]

    # Ensure the 'Province' column remains as string
    data3['Province'] = data3['Province'].astype(str)
    data3.fillna(0, inplace=True)

    # Display the DataFrame
    data3.head()

    """# **Pepro 4**

    ## Produksi Perikanan Tangkap Menurut Provinsi dan Jenis Penangkapan, 2000-2020
    """

    # Load the data from the CSV file
    df = pd.read_csv(
        'data/Produksi Perikanan Tangkap Menurut Provinsi dan Jenis Penangkapan, 2000-2020.csv', skiprows=2)

    # Extract the number of years and categories
    years = list(range(2000, 2021))
    categories = ['Perikanan Laut', 'Perairan Umum Daratan', 'Jumlah']

    # Generate column names
    columns = ['Province']
    for category in categories:
        for year in years:
            columns.append(f'{category} {year}')

    # Rename columns based on the generated names
    df.columns = columns

    # Drop rows where 'Province' is NaN
    df = df.dropna(subset=['Province']).reset_index(drop=True)

    # Melt the DataFrame to long format
    data4 = df.melt(id_vars=['Province'],
                    var_name='Variable',
                    value_name='Value')

    # Extract the Category and Year from the 'Variable' column
    data4[['Category', 'Year']] = data4['Variable'].str.extract(
        r'(.+) (\d{4})')

    # Drop the original 'Variable' column
    data4 = data4.drop(columns=['Variable'])

    # Replace NaN values with 0
    data4['Value'] = data4['Value'].fillna(0)

    # Display the final DataFrame
    data4

    """# Prepro 5

    ## Produksi Perikanan menurut Provinsi, Jenis Ikan dengan metode Tangkap Laut di Tahun 2020
    """

    # Read the HTML content
    # Adjust the file path
    file_path = 'data/Produksi Perikanan menurut Provinsi, Jenis Ikan dengan metode Tangkap Laut di Tahun 2020.htm'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Find all tables
    tables = soup.find_all('table')

    # Extract headers and rows from the first table
    if tables:
        table = tables[0]  # Choose the first table (adjust if needed)

        # Extract headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract rows and columns
        rows = []
        for row in table.find_all('tr'):
            cols = [col.text.strip() for col in row.find_all('td')]
            if cols:
                rows.append(cols)

        # Create the DataFrame
        df = pd.DataFrame(rows)

        # If the DataFrame contains headers in the first row, set them
        if len(df) > 0 and len(df.columns) == len(headers):
            df.columns = df.iloc[0]
            df = df[1:]

        # Reset index
        df = df.reset_index(drop=True)

        # Ensure all column names are strings and remove newline characters
        df.columns = df.columns.astype(str)
        df.columns = [col.replace('\n', '').strip() for col in df.columns]

        # Remove newline characters from all cell values
        df = df.applymap(lambda x: x.replace('\n', '').strip()
                         if isinstance(x, str) else x)

        # Define new column names
        new_columns = ['Jenis', 'Province', 'Jenis Ikan',
                       'Year', 'Volume Produksi', 'Nilai Produksi']
        df.columns = new_columns

        # Remove any trailing empty columns or rows
        df = df.dropna(axis=1, how='all')
        df = df.dropna(how='all')

        # Convert columns to appropriate data types
        df['Volume Produksi'] = pd.to_numeric(
            df['Volume Produksi'], errors='coerce')
        df['Nilai Produksi'] = pd.to_numeric(
            df['Nilai Produksi'], errors='coerce')
        # Drop the column 'Jenis' from the data5 DataFrame

        # Display the cleaned DataFrame
        print(df)
    else:
        print("No tables found in the HTML content.")

    data5 = df

    data5

    # Replace NaN values with 0 in data5 DataFrame
    data5 = data5.fillna(0)

    data5 = data5.drop(columns=['Jenis'], errors='ignore')
    data5 = data5.drop(columns=['Year'], errors='ignore')

    data5

    """# Final Database Structure

    ## Making data dimension

    ### Dim Province
    """

    # Drop rows that have "Jumlah" or "Indonesia" in the 'Province' column for each dataset
    data1 = data1[~data1['Province'].str.contains(
        'jumlah|indonesia|Jumlah|Indonesia', na=False)]
    data2 = data2[~data2['Province'].str.contains(
        'jumlah|indonesia|Jumlah|Indonesia', na=False)]
    data3 = data3[~data3['Province'].str.contains(
        'jumlah|indonesia|Jumlah|Indonesia', na=False)]
    data4 = data4[~data4['Province'].str.contains(
        'jumlah|indonesia|Jumlah|Indonesia', na=False)]
    data5 = data5[~data5['Province'].str.contains(
        'jumlah|indonesia|Jumlah|Indonesia', na=False)]

    # Lowercase all the 'Province' column text in each dataset
    data1['Province'] = data1['Province'].str.lower()
    data2['Province'] = data2['Province'].str.lower()
    data3['Province'] = data3['Province'].str.lower()
    data4['Province'] = data4['Province'].str.lower()
    data5['Province'] = data5['Province'].str.lower()

    # Extract unique provinces from each dataset
    unique_provinces_data1 = set(data1['Province'].unique())
    unique_provinces_data2 = set(data2['Province'].unique())
    unique_provinces_data3 = set(data3['Province'].unique())
    unique_provinces_data4 = set(data4['Province'].unique())
    unique_provinces_data5 = set(data5['Province'].unique())

    # Combine all unique provinces
    all_unique_provinces = unique_provinces_data1.union(
        unique_provinces_data2, unique_provinces_data3, unique_provinces_data4, unique_provinces_data5)

    # Convert the set to a sorted list
    all_unique_provinces = sorted(list(all_unique_provinces))

    # Display the unique provinces
    print(all_unique_provinces)

    # Create the province codes like P1, P2, etc.
    province_codes = [f'P{i+1}' for i in range(len(all_unique_provinces))]

    # Create a DataFrame for Province Codes
    dim_province = pd.DataFrame({
        'Province Code': province_codes,
        'Province Name': all_unique_provinces
    })

    # Display the Province DataFrame
    dim_province.head()

    # Create a mapping from Province Name to Province Code
    province_mapping = dict(
        zip(dim_province['Province Name'], dim_province['Province Code']))

    # Replace province names with codes in each dataset
    data1['Province'] = data1['Province'].map(province_mapping)
    data2['Province'] = data2['Province'].map(province_mapping)
    data3['Province'] = data3['Province'].map(province_mapping)
    data4['Province'] = data4['Province'].map(province_mapping)
    data5['Province'] = data5['Province'].map(province_mapping)

    data1.head()

    data2.head()

    data3.head()

    data4.head()

    """### Dim Category"""

    data5.head()

    unique_Category_data4 = set(data4['Category'].unique())
    category_codes = [f'C{i+1}' for i in range(len(unique_Category_data4))]

    # Create a DataFrame for category codes
    dim_category = pd.DataFrame({
        'Category Code': category_codes,
        # Sorting to maintain consistent order
        'Category Name': sorted(unique_Category_data4)
    })

    # Display the category DataFrame
    dim_category.head()

    # Create a mapping from Category Name to Category Code
    category_mapping = dict(
        zip(dim_category['Category Name'], dim_category['Category Code']))

    # Replace category names with codes in `data4`
    data4['Category'] = data4['Category'].map(category_mapping)

    # Display the updated DataFrame
    data4.head()

    """### Dim Location"""

    # Assuming you have already loaded your data into data2

    # Extract unique locations from data2
    unique_locations_data2 = set(data2['Location'].unique())

    # Create location codes like L1, L2, etc.
    location_codes = [f'L{i+1}' for i in range(len(unique_locations_data2))]

    # Create a DataFrame for location codes
    dim_location = pd.DataFrame({
        'Location Code': location_codes,
        # Sorting to maintain consistent order
        'Location Name': sorted(unique_locations_data2)
    })

    # Display the location DataFrame
    dim_location.head()

    # Create a mapping from Location Name to Location Code
    location_mapping = dict(
        zip(dim_location['Location Name'], dim_location['Location Code']))

    # Replace location names with codes in `data2`
    data2['Location'] = data2['Location'].map(location_mapping)

    # Display the updated DataFrame
    data2.head()

    """### Dim Method"""

    # Extract unique methods from data1
    unique_methods_data1 = set(data1['Method'].unique())

    # Create method codes like M1, M2, etc.
    method_codes = [f'M{i+1}' for i in range(len(unique_methods_data1))]

    # Create a DataFrame for method codes
    dim_method = pd.DataFrame({
        'Method Code': method_codes,
        # Sorting to maintain consistent order
        'Method Name': sorted(unique_methods_data1)
    })

    # Display the method DataFrame
    dim_method.head()

    # Create a mapping from Method Name to Method Code
    method_mapping = dict(
        zip(dim_method['Method Name'], dim_method['Method Code']))

    # Replace method names with codes in `data1`
    data1['Method'] = data1['Method'].map(method_mapping)

    # Display the updated DataFrame
    data1.head()

    """### Dim Jenis Ikan (JI)"""

    # Assuming data5 is already defined
    # Drop any leading or trailing spaces in column names for consistency
    data5.columns = data5.columns.str.strip()

    # Extract unique 'Jenis Ikan' from data5
    unique_jenis_ikan = set(data5['Jenis Ikan'].unique())

    # Create 'Jenis Ikan' codes like J1, J2, etc.
    jenis_ikan_codes = [f'JI{i+1}' for i in range(len(unique_jenis_ikan))]

    # Create a DataFrame for 'Jenis Ikan' codes
    dim_jenis_ikan = pd.DataFrame({
        'Jenis Ikan Code': jenis_ikan_codes,
        # Sorting to maintain consistent order
        'Jenis Ikan Name': sorted(unique_jenis_ikan)
    })

    # Display the 'dim_jenis_ikan' DataFrame
    dim_jenis_ikan

    # Create a mapping from 'Jenis Ikan Name' to 'Jenis Ikan Code'
    jenis_ikan_mapping = dict(
        zip(dim_jenis_ikan['Jenis Ikan Name'], dim_jenis_ikan['Jenis Ikan Code']))

    # Replace 'Jenis Ikan' names with codes in data5
    data5['Jenis Ikan'] = data5['Jenis Ikan'].map(jenis_ikan_mapping)

    # Display the updated data5 DataFrame
    data5.head()

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create tables for each DataFrame

    # Create table for data1
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_nilai_produksi_provinsi_dan_jenis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Usaha] TEXT,
        Provinsi TEXT,
        [Jenis Ikan] TEXT,
        Tahun INTEGER,
        [Volume Produksi] INTEGER,
        [Nilai Produksi] INTEGER
    )
    ''')

    # Create table for data2
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_nilai_produksi_perikanan_tangkap_perairan_umum (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Usaha] TEXT,
        Provinsi TEXT,
        [Jenis Ikan] TEXT,
        Tahun INTEGER,
        [Volume Produksi] INTEGER,
        [Nilai Produksi] INTEGER
    )
    ''')

    # Create table for data3
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_produksi_nilai_produksi_perikanan_tangkap_laut (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Usaha] TEXT,
        Provinsi TEXT,
        [Jenis Ikan] TEXT,
        Tahun INTEGER,
        [Volume Produksi] INTEGER,
        [Nilai Produksi] INTEGER
    )
    ''')

    # Create table for data4
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_produksi_perikanan_tangkap (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Usaha] TEXT,
        Provinsi TEXT,
        [Jenis Ikan] TEXT,
        Tahun INTEGER,
        [Volume Produksi] INTEGER,
        [Nilai Produksi] INTEGER
    )
    ''')

    # Create table for data5
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fact_produksi_perikanan_jenis_ikan_tangkap_laut (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Usaha] TEXT,
        Provinsi TEXT,
        [Jenis Ikan] TEXT,
        Tahun INTEGER,
        [Volume Produksi] INTEGER,
        [Nilai Produksi] INTEGER
    )
    ''')

    # Create dimension tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_province (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Province TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Category TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_jenis_ikan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        [Jenis Ikan Code] TEXT,
        [Jenis Ikan Name] TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_location (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Location TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dim_method (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Method TEXT
    )
    ''')

    # Insert data into tables
    data1.to_sql('fact_nilai_produksi_provinsi_dan_jenis',
                 conn, if_exists='replace', index=False)
    data2.to_sql('fact_nilai_produksi_perikanan_tangkap_perairan_umum',
                 conn, if_exists='replace', index=False)
    data3.to_sql('fact_produksi_nilai_produksi_perikanan_tangkap_laut',
                 conn, if_exists='replace', index=False)
    data4.to_sql('fact_produksi_perikanan_tangkap',
                 conn, if_exists='replace', index=False)
    data5.to_sql('fact_produksi_perikanan_jenis_ikan_tangkap_laut',
                 conn, if_exists='replace', index=False)

    dim_province.to_sql('dim_province', conn, if_exists='replace', index=False)
    dim_category.to_sql('dim_category', conn, if_exists='replace', index=False)
    dim_jenis_ikan.to_sql('dim_jenis_ikan', conn,
                          if_exists='replace', index=False)
    dim_location.to_sql('dim_location', conn, if_exists='replace', index=False)
    dim_method.to_sql('dim_method', conn, if_exists='replace', index=False)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Data has been successfully inserted into the SQLite database.")
