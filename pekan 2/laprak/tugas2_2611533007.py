# ==========================================
# SISTEM REGISTRASI PRAKTIKAN ALPRO 2026
# ==========================================

# Konstanta
BATAS_MINIMUM_NILAI = 75.0

# Input data praktikan
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3007 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3007 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3007 = int(input("Masukkan Umur : "))
skor_tes_3007 = float(input("Masukkan Skor Tes Awal : "))

# Data String
alamat_3007 = """Jl. Andalas No. 70F,
Kecamatan Padang Timur,
Kota Padang"""

# Data Complex
id_token_3007 = complex(100 + 3j)

# Boolean untuk menentukan kelulusan
lulus_3007 = skor_tes_3007 >= BATAS_MINIMUM_NILAI

# ==========================================
# MENAMPILKAN DATA PRAKTIKAN
# ==========================================

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_3007, "| Tipe:", type(nama_3007))
print("Jenis Kelamin :", jenis_kelamin_3007, "| Tipe:", type(jenis_kelamin_3007))
print("Alamat Domisili:")
print(alamat_3007, "| Tipe:", type(alamat_3007))
print("Umur :", umur_3007, "tahun | Tipe:", type(umur_3007))
print("Skor Tes Awal :", skor_tes_3007, "| Tipe:", type(skor_tes_3007))
print("ID Token Sinyal:", id_token_3007, "| Tipe:", type(id_token_3007))

# ==========================================
# STATUS KELULUSAN
# ==========================================

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", BATAS_MINIMUM_NILAI)
print("Apakah Dinyatakan Lulus?:", lulus_3007, "| Tipe:", type(lulus_3007))