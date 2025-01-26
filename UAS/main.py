class transaksi:
    def __init__(self):
        self.keranjang = {}
        self.totalawal = 0
        self.totalharga = 0

    def tambah_barang(self, barang, harga, jumlah):
        try:
            if harga <= 0 or jumlah <= 0:
                raise ValueError
            else:
                self.keranjang[barang] = [harga, jumlah]
        except ValueError:
            print("\nHarga atau Jumlah tidak boleh 0\n")

    def hapus_barang(self, barang):
        try:
            del self.keranjang[barang]
            return
        except KeyError:
            print("\nBarang tidak ada di keranjang\n")

    def ubah_namabarang(self, barang, barangbaru):
        try:
            if barangbaru == barang or barangbaru == "":
                raise ValueError
            else:
                self.keranjang.update({barangbaru: self.keranjang.pop(barang)})
                return
        except ValueError:
            print("\nNama Barang tidak boleh sama atau kosong!\n")
        except KeyError:
            print("\nBarang tidak ada di dalam keranjang\n")
    
    def ubah_jumlahbarang(self, barang, jumlahbaru):
        try:
            if jumlahbaru <= 0:
                raise ValueError
            else:
                self.keranjang[barang][1] = jumlahbaru
        except ValueError:
                print("\nJumlah tidak boleh 0!\n")
        except KeyError:
                print("\nBarang tidak ada di dalam keranjang\n")

    def ubah_harga(self, barang, hargabaru):
        try:
            if hargabaru <= 0:
                raise ValueError
            else:
                self.keranjang[barang][0] = hargabaru
        except ValueError:
            print("\nHarga tidak boleh 0!\n")
        except KeyError:
            print("\nBarang tidak ada di dalam keranjang\n")

    def hapus_semua(self):
        self.keranjang.clear()
        print("\nKeranjang telah dihapus!\n")

    def lihat_keranjang(self):
        kunci = [key for key in self.keranjang.keys()]
        nilai1 = [value[0] for value in self.keranjang.values()]
        nilai2 = [value[1] for value in self.keranjang.values()]
        print("{:<15} | {:<15} | {:<15} | {:<15}".format("Nama Barang", "Jumlah", "Harga", "Subtotal"))
        print("-" * 62)
        for kunci, nilai1, nilai2 in zip(kunci, nilai1, nilai2):
            subtotal = nilai1 * nilai2
            print("{:<15} | {:<15} | {:<15} | {:<15}".format(kunci, nilai2, nilai1, subtotal))
        print("-" * 62)

    def total_jumlah(self):
        self.totalawal = 0 

        for barang, value in self.keranjang.items():
            self.totalawal += value[0] * value[1]
        print(f"Total harga: Rp{self.totalawal}")
        print(" ")

    def diskon(self):
        if self.totalawal >= 100000:
            diskon = self.totalawal * 0.10
        elif self.totalawal >= 50000:
            diskon = self.totalawal * 0.05
        else:
            diskon = 0
        self.totalharga = self.totalawal - diskon
        print("{:<53} {:<15}".format("Anda Hemat", diskon))
        print("{:<53} {:<15}".format("Total", self.totalharga))

    def bayar(self, tunai):
        try:
            if tunai < 0:
                raise ValueError
            elif tunai < self.totalharga:
                print("\nYah, uang anda kurang\n")
            else:
                kembalian = tunai - self.totalharga
                print("-" * 62)
                print("{:<53} {:<15}".format("Kembali", kembalian))
                print("-" * 62)
        except ValueError:
            print("\nTidak ada input!\n")
    
    def header(self):
        import datetime
        tgl = datetime.datetime.now()
        tgl = tgl.strftime("%d-%m-%Y %H:%M:%S")
        print("{:^60} \n{:^60} \n{:^60}".format("KRILLGOSONG SWALAYAN"
                                            , "CV. KODINGAN GWEH KEREN"
                                            , "JL. A.YANI NO 80 BANYUWANGI"))
        print("-" * 62)
        print("{:<9}: {:<9}".format("No", "MR00023/0103/240803")) #nomor ini hanya placeholder
        print("{:<9}: {:<9}".format("Kasir", "MozaLB"))
        print("{:<9}: {:<9}".format("Tanggal", f"{tgl}"))
        print("{:<9}: {:<9}".format("Kassa", "103"))
        print("-" * 62)