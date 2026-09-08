is_lulus_3007 = True
is_cumlaude_3007 = True

nilai_3007 = 80
batas_lulus_3007 = 75

status_kelulusan_3007 = nilai_3007 >= batas_lulus_3007 

print("=== Check Kelulusan ===")
print("Nilai", nilai_3007)
print("Apakah Lulus?:", status_kelulusan_3007)
if is_lulus_3007 and is_cumlaude_3007:
    print("Selamat, Anda lulus dengan predikat Cum laude!")
