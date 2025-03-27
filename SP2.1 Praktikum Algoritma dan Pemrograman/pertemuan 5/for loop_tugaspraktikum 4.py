# Pertemuan 4 (studi kasus sendiri)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

# mengulangi item untuk ditampilkan
mobil = ["nissan", "toyota", "mazda"]
for i in mobil:
    print("mobil", i)

print("\n")

# mengulangi huruf yang terdapat dalam string
for i in "nissan":
    print(i)
    
print("\n")

# for break statement
# mengulangi item untuk ditampilkan namun berhenti saat kondisi yang ditentukan terpenuhi
mobil = ["nissan", "toyota", "mazda", "honda"]
for i in mobil:
  print(i)
  if i == "mazda": #berhenti di mazda
    break

print("\n")

# for continue statement
# mengulangi semua item namun melewati atau skip kondisi yg ditentukan
mobil = ["nissan", "toyota", "mazda", "honda"]
for i in mobil:
  if i == "mazda": # skip mazda untuk ditampilkan
    continue
  print(i)

print("\n")

# mengulangi 4 range, jadi mulai dari 0 sampai 3
for i in range(4):
   print(i)


print("\n")

# mengulangi antara angka 3 sampai 8, jadi mulai dari 3 sampai 7
for i in range(3, 8):
   print(i)
