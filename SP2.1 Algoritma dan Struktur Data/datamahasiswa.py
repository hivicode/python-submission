class Mahasiswa:
    def __init__(self, nama, prodi, dataMK):
        self.nama = nama
        self.prodi = prodi
        self.dataMK = dataMK

    def perkenalan(self):
        print(f"Perkenalkan saya {self.nama} dari {self.prodi}")
        print(f"Saya mengikuti matakuliah {self.dataMK.mk} dengan nilai akhir {self.dataMK.nilai}")