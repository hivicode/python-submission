# TIPE DATA (studi kasus sendiri)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

# studi kasus: membuat input biodata, setelah input selesai membersihkan terminal dan menampilkan inputannya dengan detail yang lebih rapi

from os import system
nama = input("Nama anda: ")
pt = input("Nama Perguruan Tinggi: ")
tahun_masuk = int(input("Tahun Masuk: "))
nim = int(input("NIM: "))
prodi = input("Program Studi: ")
system ("cls")
print ("Halo, nama saya", nama+".", "\nSaya adalah mahasiswa", pt, "Angkatan", tahun_masuk, "\nDengan NIM", nim, "\nSaya mengambil Program Studi", prodi+".")
