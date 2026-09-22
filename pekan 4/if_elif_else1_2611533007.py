umur_3007 = int(input("Input umur anda:"))
sim_3007 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3007 >= 17 and sim_3007 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")
elif umur_3007 >= 17 and sim_3007 != 'y':
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")
elif umur_3007 < 17 and sim_3007 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")
else:
    print("Anda Belum Cukup Umur dan Tidak Boleh Bawa Motor")
print("Program Selesai")