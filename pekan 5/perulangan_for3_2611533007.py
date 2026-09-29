ulang_3007 = int(input("Masukkan jumlah perulangan: "))

jumlah_3007 = 0
for i in range(1, ulang_3007 + 1):
    print(i, end="")
    jumlah_3007 = jumlah_3007 + i

    if i < ulang_3007:
        print(" + ", end="")
    else:
        print(" = ", end="")
print()
print("Jumlah =", jumlah_3007)