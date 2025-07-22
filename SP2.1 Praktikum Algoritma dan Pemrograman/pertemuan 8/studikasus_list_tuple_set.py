# Pertemuan 8
# Nama: Bintang Fathir F.A
# NIM: 1124102166
"""
Studi Kasus: Pengelolaan Data Mahasiswa dalam Kelas

Deskripsi:
1. Gunakan List untuk menyimpan daftar nama mahasiswa yang hadir.
2. Gunakan Tuple untuk menyimpan data mata kuliah (kode, nama, sks) yang tidak berubah.
3. Gunakan Set untuk mencatat mahasiswa yang sudah mengumpulkan tugas (tidak boleh ada duplikasi).

Tugas:
- Tampilkan daftar mahasiswa yang hadir.
- Tampilkan data mata kuliah.
- Tampilkan mahasiswa yang sudah mengumpulkan tugas.
- Tampilkan mahasiswa yang hadir tapi belum mengumpulkan tugas.
"""

# Input data mata kuliah (Tuple)
kode = input("Masukkan kode mata kuliah: ")
nama_mk = input("Masukkan nama mata kuliah: ")
sks = int(input("Masukkan jumlah SKS: "))
mata_kuliah = (kode, nama_mk, sks)

# Input daftar hadir (List)
daftar_hadir = []
print("\nMasukkan nama mahasiswa yang hadir (ketik 'selesai' untuk berhenti):")
while True:
    nama = input(f"Mahasiswa ke-{len(daftar_hadir)+1}: ").strip()
    if nama.lower() == 'selesai':
        break
    if nama:
        daftar_hadir.append(nama)

# Input mahasiswa yang sudah mengumpulkan tugas (Set)
pengumpul_tugas = set()
print("\nMasukkan nama mahasiswa yang sudah mengumpulkan tugas (ketik 'selesai' untuk berhenti):")
while True:
    nama = input(f"Mahasiswa ke-{len(pengumpul_tugas)+1}: ").strip()
    if nama.lower() == 'selesai':
        break
    if nama:
        pengumpul_tugas.add(nama)

print("\nDaftar Mahasiswa yang Hadir:")
for i, nama in enumerate(daftar_hadir, 1):
    print(f"{i}. {nama}")

print("\nData Mata Kuliah:")
print(f"Kode: {mata_kuliah[0]}")
print(f"Nama: {mata_kuliah[1]}")
print(f"SKS: {mata_kuliah[2]}")

print("\nMahasiswa yang Sudah Mengumpulkan Tugas:")
if pengumpul_tugas:
    for nama in pengumpul_tugas:
        print(f"- {nama}")
else:
    print("Belum ada yang mengumpulkan tugas.")

# Mahasiswa yang hadir tapi belum mengumpulkan tugas
hadir_unik = set(daftar_hadir)  # Hilangkan duplikasi hadir
belum_kumpul = hadir_unik - pengumpul_tugas

print("\nMahasiswa yang Hadir tapi Belum Mengumpulkan Tugas:")
if belum_kumpul:
    for nama in belum_kumpul:
        print(f"- {nama}")
else:
    print("Semua mahasiswa yang hadir sudah mengumpulkan tugas.") 