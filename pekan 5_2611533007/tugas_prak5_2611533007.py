tinggi_3007 = int(input("Masukkan tinggi pola: "))

for i in range(1, tinggi_3007 + 1):
    for j in range(tinggi_3007 - i):
        print(" ", end="")

    for g in range(i):
       print("* ", end="")
    print()