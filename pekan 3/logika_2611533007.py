#Memasukkan nilai boolean
#Input tidak peka terhadap huruf besar dan kecil
a1_3007 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3007 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_3007)
print("A2 =", a2_3007)

#Konjungsi: bernilai True jika keduanya true
hasil = a1_3007 and a2_3007
print("\nKonjungsi (and)")
print("A1 and A2 =", hasil)

#Disjungsi: bernilai True jika salah satu true
hasil = a1_3007 or a2_3007
print("\nDisjungsi (or)")
print("A1 or A2 =", hasil)

#Negasi a1: membalik nilai a1_3007
hasil = not a1_3007
print("\nNegasi a1 (not)")
print("not A1 =", hasil)

#Negasi a2: membalik nilai a2_3007
hasil = not a2_3007
print("\nNegasi a2 (not)")
print("not A2 =", hasil)

#XOR: bernilai true jika kedua nilai berbeda
hasil = a1_3007 != a2_3007
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)
