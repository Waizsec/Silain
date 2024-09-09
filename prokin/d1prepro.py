import os
import glob

# Set the directory path
directory_path = '../data'

# Define the file names you're looking for
file_names = [
    'Nilai Produksi Perikanan Budidaya Menurut Provinsi dan Jenis Budidaya, 2017-2019.xlsx',
    'Nilai Produksi Perikanan Tangkap di Perairan Umum Menurut Lokasi, 2017-2019.csv',
    'Produksi dan Nilai Produksi Perikanan Tangkap di Laut Menurut Provinsi dan Komoditas Utama, 2022.xlsx',
    'Produksi Perikanan Tangkap Menurut Provinsi dan Jenis Penangkapan, 2000-2020.csv'
]

# Load and print the available files in the directory
available_files = glob.glob(os.path.join(directory_path, '*'))

# Filter and print matching files
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    if file_path in available_files:
        print(f"File '{file_name}' exists in the directory.")
    else:
        print(f"File '{file_name}' does not exist in the directory.")
