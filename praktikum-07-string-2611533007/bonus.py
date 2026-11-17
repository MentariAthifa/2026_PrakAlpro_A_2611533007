# Name: Mentari Athifa Khalish Andyni
#NIM: 2611533007
# Bonus

Kalimat = input("Masukkan kalimat: ")
Teks = Kalimat.lower().replace(" ", "")

if Teks == Teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")