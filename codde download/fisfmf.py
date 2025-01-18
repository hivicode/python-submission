def input_mahasiswa():
    mhs = {}
    print("Input Mahasiswa")
    print(u'\u2500' * 15)
    mhs["nim"] = input("NIM: ")
    mhs["nama"] = input("Nama: ")
    mhs["prodi"] = input("Prodi: ")
    return mhs

def tambah_mahasiswa(mahasiswa):
    mahasiswa.append(input_mahasiswa())
    return mahasiswa

if __name__ == "__main__":
    mahasiswa = []
    lanjut = "y"
    while(lanjut == "y"):
        mahasiswa = tambah_mahasiswa(mahasiswa)
        print("{:^10} | {:<35} | {:^23}".format("NIM", "Nama", "Prodi"))
        print(u'\u2500' * 100)
        for mhs in mahasiswa:
            print("{:^10} | {:<35} | {:^23}".format(mhs["nim"], mhs["nama"], mhs["prodi"]))
        lanjut = input("Tambah Mahasiswa? (y/n)")