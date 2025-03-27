# Pertemuan 4 (studi kasus sendiri)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

# Studi kasus: membuat perulangan dari angka awal 0 sampai kurang dari atau sama dengan 10 dengan kelipatan 2

print("While loop")
awal = 0 #nilai awal 0
while awal <= 10: # jika nilai awal kurang dari atau sama dengan 10, maka
    print(awal) # tampilkan
    awal += 2 # dengan kondisi berkelipatan 2

print("\n")

# Studi kasus: membuat perulangan dari angka awal 0 sampai kurang dari atau sama dengan 16 dengan kelipatan 2,
# namun berhentikan tampilan saat di angka 10

print("While if loop")
awal = 0
while awal <= 16:
    print(awal)
    if awal == 10: # jika nilai awal mencapai perulangan angka 10, maka
        break # berhentikan
    awal += 2

print("\n")

# Studi kasus: membuat perulangan dari angka awal 0 sampai kurang dari 10 dengan kelipatan 2,
# dan tampilkan bahwa angka awal tidak lebih kurang dari 10

print("While else loop")
awal = 0
while awal < 10:
  print(awal)
  awal += 2
else:
  print("nilai tidak lebih kurang dari 10")
