import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query SELECT dengan ORDER BY
cursor.execute("SELECT * FROM FAUNA ORDER BY nama_fauna ASC") #ASC|DESC
rows = cursor.fetchall()

print("Data Fauna:")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*100)
for rows in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))
    
conn.close()