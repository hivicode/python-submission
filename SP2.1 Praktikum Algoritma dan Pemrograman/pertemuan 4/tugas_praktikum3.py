# Pertemuan 4 (studi kasus sendiri)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

# Studi kasus: pendeteksi spesies
# Syarat:

# IF ELSE ✔
# ELIF ✔
# NESTED IF ✔

import random
print("\nProgram Pendeteksi Spesies")
print("-"*20)
nama = input("Nama Anda: ")
presentase = random.randint(0, 101)

if presentase >= 50 :
    spesies = "sedikit reptil"
    if presentase >= 99 :
        spesies = "sangat reptil"
    else:
        spesies = "cukup reptil"
elif presentase >= 25 :
    spesies = "sedikit lagi jadi reptil" 
else:
    spesies = "manusia"

print(f"Spesies: {presentase}% Anda {spesies}\n")
