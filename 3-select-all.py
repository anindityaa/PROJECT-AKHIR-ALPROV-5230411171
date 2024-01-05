import sqlite3

conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM FAUNA")
rows = cursor.fetchall()

print("Data Fauna:")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*100)
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
conn.close()