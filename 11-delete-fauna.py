import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query DELETE
asal = "Kalimantan" 
cursor.execute(f"DELETE FROM fauna WHERE asal = ?", (asal,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data fauna dengan asal {asal} berhasil dihapus.")
else:
    print(f"Tidak ada data fauna dengan asal {asal}.")

# Menutup koneksi
conn.close()