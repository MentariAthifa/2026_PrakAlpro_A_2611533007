print("=== SISTEM LOKET ALPRO ADVENTURE PARK === ")

nama_3007 = input("Masukkan Nama Pengunjung :")
umur_3007 = int(input("Masukkan Umur Anda : "))
sim_c_3007 =  input("Apakah Anda Sudah Punya SIM C? (y/t) :").strip().lower()

print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3007 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3007 = int(input("Masukkan jumlah tiket           : "))

is_member_3007 = input("Apakah Anda member? (y/t)       : ")
kode_promo_valid_3007 = input("Apakah kode promo valid? (y/t)  : ")

if jumlah_tiket_3007 < 0:
    print("Jumlah Tiket Tidak Valid")

harga_paket_3007 = 0

match paket_3007:
    case 1:
        nama_paket_3007 = "Wahana Safari Rimba"
        harga_paket_3007 = 50000
    case 2:
        nama_paket_3007 = "Wahana Arung Jeram"
        harga_paket_3007 = 75000
    case 3:
        nama_paket_3007 = "Wahana Motor ATV Ekstrim"
        harga_paket_3007 = 120000
    case 4:
        nama_paket_3007 = "Wahana Roller Coaster Kilat"
        harga_paket_3007 = 100000
    case 5:
        nama_paket_3007 = "Wahana All-Access VIP"
        harga_paket_3007 = 220000
    case _:
        print("Wahana Tidak Valid")

print()
print("=== KELAYAKAN PENGENDARA WAHANA ===")

if paket_3007 == 3 :
 if umur_3007 >= 17 and sim_c_3007 == 'y':
    print("Status Akses : Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
 elif umur_3007 >= 17 and sim_c_3007 != 'y':
    print("Status Akses : Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
 elif umur_3007 < 17 and sim_c_3007 == 'y':
    print("Status Akses : Identitas tidak valid: Belum cukup umur memiliki SIM.")
 else:
    print("Status Akses : Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_3007 >= 10 :
        print("Anda sudah cukup umur untuk menaiki wahana {nama_paket_3007}")
    else:
        print("Anda belum cukup umur untuk menaiki wahana {nama_paket_3007}")     


subtotal_3007 = harga_paket_3007 * jumlah_tiket_3007
total_diskon_persen_3007 = 0

if subtotal_3007 > 200000:
    total_diskon_persen_3007 += 10 #Diskon belanja besar

if is_member_3007 in ['y', 'ya']:
    total_diskon_persen_3007 += 5 #Diskon member

if kode_promo_valid_3007 in ['y', 'ya']:
    total_diskon_persen_3007 += 15 #Diskon voucher

if jumlah_tiket_3007 >= 5:
    total_diskon_persen_3007 += 5 #Diskon tambahan rombongan

nominal_diskon_3007 = subtotal_3007 * (total_diskon_persen_3007 / 100)
total_bayar_3007 = subtotal_3007 - nominal_diskon_3007

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3007:,.0f}")
print(f"Total Diskon : {total_diskon_persen_3007}% (Rp {nominal_diskon_3007:,.0f})")
print(f"Total Bayar : Rp {total_bayar_3007:,.0f}")

if total_bayar_3007 > 300000:
    print("Catatan Layanan : Selamat! Anda berhak mendapatkan souvenir gratis.")
else:
    print("Catatan Layanan : Terima kasih telah berkunjung.")

print("Program selesai")