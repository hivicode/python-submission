# Python Submission

List
=================

* [1. Input & Output](#1-input-output)
* [2. Data Types](#data-types)
* [3. Data Types Conversion](#conversion)
* [4. Arithmetic Operators](#arithmetic)
* [5. Assignment Operators](#assignment)
* [6. Find Total & Change](#totalchange)
* [Watch & Learn](#watch-learn)
  


---
## 1. Input Output

enter an input to be printed as output
<details>
<summary>Example</summary>
  
Code
  
```
from os import system
nama = input("Nama anda: ")
pt = input("Nama Perguruan Tinggi: ")
tahun_masuk = int(input("Tahun Masuk: "))
nim = int(input("NIM: "))
prodi = input("Program Studi: ")
system ("cls")
print ("Halo, nama saya", nama+".", "\nSaya adalah mahasiswa", pt, "Angkatan", tahun_masuk, "\nDengan NIM", nim, "\nSaya mengambil Program Studi", prodi+".")
```

Input
  
```
Nama anda: Bintang 
Nama Perguruan Tinggi: Stikom
Tahun Masuk: 2000
NIM: 1234567890
Program Studi: Informatika
```

Output after system ("cls") func
  
```
Halo, nama saya Bintang.
Saya adalah mahasiswa Stikom Angkatan 2000
Dengan NIM 1234567890
Saya mengambil Program Studi Informatika.
```
