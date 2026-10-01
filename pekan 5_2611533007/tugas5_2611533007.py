n_3007 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
print("#", end="")
for i in range(4 * n_3007 + 2):
    print("=", end="")
print("#")

# Jam pasir atas
for baris_3007 in range(n_3007, 0, -1):
    print("|", end="")

    for spasi_3007 in range(2 * (n_3007 - baris_3007)):
        print(" ", end="")
    for angka_mundur_3007 in range(baris_3007, 0, -1):
        print(angka_mundur_3007, end=" ")

    print("*", end=" ")

    for angka_maju_3007 in range(1, baris_3007 + 1):
        print(angka_maju_3007, end=" ")

    for spasi_3007 in range(2 * (n_3007 - baris_3007)):
        print(" ", end="")

    print("|")


# Bagian tengah
print("|", end="")

for spasi_3007 in range(2 * n_3007):
    print(" ", end="")

print("*", end="")

for spasi_3007 in range(2 * n_3007 + 1):
    print(" ", end="")

print("|")


# Jam pasir bawah
for baris_3007 in range(1, n_3007 + 1):
    print("|", end="")

    
    for spasi_3007 in range(2 * (n_3007 - baris_3007)):
        print(" ", end="")

    
    for angka_mundur_3007 in range(baris_3007, 0, -1):
        print(angka_mundur_3007, end=" ")

    
    print("*", end=" ")

    
    for angka_maju_3007 in range(1, baris_3007 + 1):
        print(angka_maju_3007, end=" ")


    for spasi_3007 in range(2 * (n_3007 - baris_3007)):
        print(" ", end="")

    print("|")

# Border bawah
print("#", end="")
for i in range(4 * n_3007 + 2):
    print("=", end="")
print("#")