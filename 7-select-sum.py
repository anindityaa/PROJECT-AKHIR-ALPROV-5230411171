import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(jml_skrng) FROM FAUNA")
total_populasi = cursor.fetchone()[0]

print(f"Total populasi hewan langka saat ini: {total_populasi}")

# Menutup koneksi
conn.close()