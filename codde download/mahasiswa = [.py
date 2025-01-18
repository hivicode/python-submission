mahasiswa = [
                {"nim": "A01", "nama": "Andi", "prodi": "Teknik Informatika"},
                {"nim": "A02", "nama": "Budi", "prodi": "Teknik Mesin"},
                {"nim": "A03", "nama": "Cici", "prodi": "Teknik Industri"}
            ]

print("{:^10} | {:<35} | {:^23}".format("NIM", "Nama", "Prodi"))
print(u'\u2500' * 100)
for mhs in mahasiswa:
    print("{:^10} | {:<35} | {:^23}".format(mhs["nim"], mhs["nama"], mhs["prodi"]))

    