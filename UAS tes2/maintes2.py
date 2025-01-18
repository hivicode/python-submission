class transaksi:
    def __init__(self):
        self.keranjang = {}
        self.subtotal = 0
        self.totalharga = 0

    def tambahbarang(self, barang, harga, jumlah):
        try:
            if harga <= 0 or jumlah <= 0:
                raise ValueError
            else:
                self.keranjang[barang] = [harga, jumlah]
                print(f"\n{jumlah} {barang} seharga Rp{harga} telah dimasukkkan dalam keranjang!")
        except ValueError:
            print("Harga atau Jumlah tidak boleh 0")

    def hapusbarang(self, barang):
        try:
            del self.keranjang[barang]
            return
        except KeyError:
            print("Barang tidak ada di keranjang")

    def ubah_namabarang(self, barang, barangbaru):
        try:
            if barangbaru == barang or barangbaru == "":
                raise ValueError
            else:
                self.keranjang.update({barangbaru: self.keranjang.pop(barang)})
                return
        except ValueError:
            print("Nama Barang tidak boleh sama atau kosong!")
        except KeyError:
            print("Barang tidak ada di dalam keranjang")
    
    def ubah_jumlahbarang(self, barang, jumlahbaru):
        try:
            if jumlahbaru <= 0:
                raise ValueError
            else:
                self.keranjang[barang][1] = jumlahbaru
        except ValueError:
                print("Jumlah tidak boleh 0!")
        except KeyError:
                print("Barang tidak ada di dalam keranjang")

    def ubah_harga(self, barang, hargabaru):
        try:
            if hargabaru <= 0:
                raise ValueError
            else:
                self.keranjang[barang][0] = hargabaru
        except ValueError:
            print("Harga tidak boleh 0!")
        except KeyError:
            print("Barang tidak ada di dalam keranjang")

    def hapus_semua(self):
        self.keranjang.clear()
        print("Keranjang telah dihapus!")

    