angka1_3007 = int(input("Input angka-1: "))
angka2_3007 = int(input("Input angka-2: "))

print("\nNilai awal angka-1 =", angka1_3007)
print("Nilai angka-2 =", angka2_3007)

#Assignment biasa
hasil_3007 = angka1_3007
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3007)

#Assignment penambahan
hasil_3007 = angka1_3007
hasil_3007 += angka2_3007
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3007)

#Assignment pengurangan
hasil_3007 = angka1_3007
hasil_3007 -= angka2_3007
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3007)

#Assignment perkalian
hasil_3007 = angka1_3007
hasil_3007 *= angka2_3007
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3007)

#Assignment pembagian
if angka2_3007 != 0:
    hasil_3007 = angka1_3007
    hasil_3007 /= angka2_3007
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3007)
    #Operator tambahan
    hasil_3007 = angka1_3007
    hasil_3007 //= angka2_3007
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3007)
    hasil_3007 = angka1_3007
    hasil_3007 %= angka2_3007
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3007)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0")

#Operator tambahan: assignment perpangkatan
hasil_3007 = angka1_3007
hasil_3007 **= angka2_3007
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3007)
