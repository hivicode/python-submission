class Transaksi:
    """
    Kelas ini mewakili transaksi belanja keranjang.

    Atribut:
    - keranjang: Sebuah list yang berisi item, harga, dan jumlah mereka
    - subtotal: Total harga dari semua item di keranjang
    - total_akhir: Harga akhir setelah diskon atau promosi diterapkan

    Metode:
    - add_barang(nama, harga, jumlah): Menambahkan item baru ke keranjang
    - delete_item(nama): Menghapus item dari keranjang
    - update_nama_item(nama, nama_baru): Memperbarui nama item di keranjang
    """
    def __init__(self):
        self.keranjang = [] 
        self.subtotal = 0
        self.total_akhir = 0
      
    def add_barang(self, nama, harga, jumlah): 
        """
        Menambahkan item baru ke keranjang.
        Jika harga atau jumlah kurang dari atau sama dengan 0, menimbulkan ValueError.
        """
        try:
            if harga <= 0 or jumlah <= 0:
                raise ValueError
            else:
                self.keranjang.append({"nama": nama, "harga": harga, "jumlah": jumlah})
                print(" ")
                print(f"Item {nama}:{harga} dengan jumlah {jumlah} telah dimasukkan!")
        except ValueError:
            print("harga atau jumlah tidak boleh kurang dari 0")
      
    def delete_item(self, nama):
        """
        Menghapus item dari keranjang.
        Jika item tidak ditemukan di keranjang, menimbulkan KeyError.
        """
        try:
            self.keranjang = [item for item in self.keranjang if item["nama"] != nama]
            return f"Item {nama} telah dihapus"
        except KeyError:
            print("Barang tidak ditemukan di keranjang")
  
    def update_nama_item(self, nama, nama_baru):
        """
        Method ini digunakan untuk memperbarui nama item pada keranjang belanja.
        
        Parameter:
        nama (str): Nama item sebelumnya.
        nama_baru (str): Nama item baru yang akan diperbarui.
        
        Return:
        str: Mengembalikan string yang menandakan nama item berhasil diperbarui.
        
        Raises:
        ValueError: Terjadi jika nama baru sama dengan nama sebelumnya atau nama baru kosong.
        KeyError: Terjadi jika item tidak ditemukan pada keranjang.
        """
        try:
            if nama_baru == nama or nama_baru == " ":
                raise ValueError
            else:
                for item in self.keranjang:
                    if item["nama"] == nama:
                        item["nama"] = nama_baru
                        return f"{nama_baru} telah diperbarui di keranjang!"
        except ValueError:
            print("Nama tidak boleh sama/kosong!")
        except KeyError:
            print("Barang tidak ditemukan di keranjang")

    def update_jumlah_item(self, nama, jumlah_baru):
        """
        Method ini digunakan untuk memperbarui jumlah item pada keranjang belanja.
        
        Parameter:
        nama (str): Nama item yang akan diperbarui jumlahnya.
        jumlah_baru (int): Jumlah item baru.
        
        Return:
        str: Mengembalikan string yang menandakan jumlah item berhasil diperbarui.
        
        Raises:
        ValueError: Terjadi jika jumlah baru kurang dari sama dengan 0.
        KeyError: Terjadi jika item tidak ditemukan pada keranjang.
        """
        try:
            if jumlah_baru <= 0:
                raise ValueError
            else:
                for item in self.keranjang:
                    if item["nama"] == nama:
                        item["jumlah"] = jumlah_baru
                        return f"{jumlah_baru} telah diperbarui di keranjang!"
        except ValueError:
            print(" ")
            print("Jumlah tidak boleh kosong!")
            print(" ")
        except KeyError:
            print(" ")
            print("Barang yang kamu cari tidak ada!")
            print(" ")

    def update_harga_item(self, nama, harga_baru):  # update harga dalam dictionary
        """
        Mengubah harga item dalam keranjang

        Parameters:
        nama (str): Nama item yang ingin diubah harganya
        harga_baru (int): Harga baru dari item tersebut

        Returns:
        str: Pesan berhasil atau tidaknya proses update harga item
        """
        try:
            if harga_baru <= 0:
                raise ValueError
            else:
                for item in self.keranjang:
                    if item["nama"] == nama:
                        item["harga"] = harga_baru
                        return f"{harga_baru} telah diperbarui di keranjang!"
        except ValueError:
            print(" ")
            print("Jumlah tidak boleh kosong!")
            print(" ")
        except KeyError:
            print(" ")
            print("Barang yang kamu cari tidak ada!")
            print(" ")
  
    def reset_item(self): #untuk reset seluruh item yang ada di keranjang
        """
        Mereset seluruh item dalam keranjang

        Returns:
        str: Pesan bahwa keranjang sudah direset
        """

        self.keranjang.clear()
        return "Keranjang kamu sudah di hapus"

    def check_order(self):        
        col_width = [15, 15, 15, 15]
        print(" ")
        print(
            "Nama Item".ljust(col_width[0])
            + "Jumlah".ljust(col_width[1])
            + "Harga".ljust(col_width[2])
            + "Total Harga".ljust(col_width[3])
        )
        print("-" * (col_width[0] + col_width[1] + col_width[2] + col_width[3]))
        for item in self.keranjang:
            tot_price = item["harga"] * item["jumlah"]
            print(
                item["nama"].ljust(col_width[0])
                + str(item["jumlah"]).ljust(col_width[1])
                + str(item["harga"]).ljust(col_width[2])
                + str(tot_price).ljust(col_width[3])
            )
      
    def total_pembelian(self):
        """Untuk passing total pembelian"""
        self.subtotal = 0 
        self.total_tipe = 0
        self.total_kuantitas = 0

        for item in self.keranjang:
            self.subtotal += item["harga"] * item["jumlah"]
            self.total_tipe = len(self.keranjang)
            self.total_kuantitas += item["jumlah"] 
        print(f"Total harga: Rp{self.subtotal}")
        print(f"Jumlah tipe barang: {self.total_tipe}")
        print(f"Jumlah kuantitas barang: {self.total_kuantitas}")
        print(" ")
          
    def discount_input(self):
        """Logic agar discount dapat terinput pada total pembelian"""
        if self.subtotal >= 500000:
            discount = self.subtotal * 0.10
            
        elif self.subtotal >= 300000:
            discount =  self.subtotal * 0.08
        elif self.subtotal >= 200000:
            discount = self.subtotal * 0.05
        else:
            discount = 0
        self.total_akhir = self.subtotal - discount

        print(f"Setelah discount: {self.total_akhir}")
        print(" ")
        if self.total_akhir == self.subtotal:
            print(" ")
            print("Naikkan belanja mu agar dapat discount!")
            print(" ")
        else:
            print(" ")
            print("Yeay dapet discount!")
            print(" ")

    def pembayaran(self, uang):
        """Logic Pembayaran bisa dilakukan sesuai input nominal harga"""
        try:
            if uang < 0:
              raise ValueError
            elif uang < self.total_akhir:
              print(" ")
              print("Pembayaran Gagal, uang tidak cukup")
              print(" ")
            else:
              kembalian = uang - self.total_akhir
              print(" ")
              print(f"kembalian : {kembalian}")
              print("Terimakasih telah berbelanja!")
              print(" ")
              self.keranjang.clear()
        except ValueError:
            print(" ")
            print("Kamu belum input nominal! ")
            print(" ")