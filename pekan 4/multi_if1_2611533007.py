umur_3007 = int(input("Input umur anda:"))
sim_3007 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3007 >= 17 and sim_3007 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")

if umur_3007 >= 17 and sim_3007 != 'y':
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")

if umur_3007 < 17 and sim_3007 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")

if umur_3007 < 17 and sim_3007 != 'y':
    print("Anda Belum Cukup Umur Bawa Motor")