from os import system
nama = input("Nama anda: ")
pt = input("Nama Perguruan Tinggi: ")
tahun_masuk = int(input("Tahun Masuk: "))
nim = int(input("NIM: "))
prodi = input("Program Studi: ")
system ("cls")
print ("Halo, nama saya", nama+".", "\nSaya adalah mahasiswa", pt, "Angkatan", tahun_masuk, "\nDengan NIM", nim, "\nSaya mengambil Program Studi", prodi+".")