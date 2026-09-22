total_belanja_3007 = float(input("Masukkan total belanja (Rp):"))

input_member_3007 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_3007 = input_member_3007 in ["y", "t"]

input_promo_3007 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3007 = input_promo_3007 in ["y", "t"]

total_diskon_persen_3007 = 0

if total_belanja_3007 > 1000000:
    total_diskon_persen_3007 += 10 #Diskon belanja besar

if is_member_3007:
    total_diskon_persen_3007 += 5 #Diskon member

if kode_promo_valid_3007:
    total_diskon_persen_3007 += 15 #Diskon voucher

nominal_diskon_3007 = total_belanja_3007 * (total_diskon_persen_3007 / 100)
total_bayar_3007 = total_belanja_3007 - nominal_diskon_3007

print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3007}% (Rp {nominal_diskon_3007:,.0f})")
print(f"Total Bayar : Rp {total_bayar_3007:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_3007}%")