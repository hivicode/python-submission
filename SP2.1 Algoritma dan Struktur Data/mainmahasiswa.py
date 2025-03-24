from datamahasiswa import Mahasiswa
from nilaimatakuliah import Matakuliah
from os import system

if __name__ == "__main__":
    mhs = Mahasiswa(
        nama = "Michael",
        prodi = "Teknik Informatika",
        dataMK = Matakuliah(
            mk = "Struktur Data",
            nilai = "90"
        )
    )

    system("cls")
    mhs.perkenalan()
