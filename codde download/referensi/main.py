class Transaksi:
    """
    Kelas ini mewakili transaksi belanja keranjang.

    Atribut:
    - keranjang: Sebuah dictionary yang berisi item dan harga dan jumlah mereka
    - total_harga: Total harga dari semua item di keranjang
    - final_price: Harga akhir setelah diskon atau promosi diterapkan

    Metode:
    - add_barang(nama, harga, jumlah): Menambahkan item baru ke keranjang
    - delete_item(nama): Menghapus item dari keranjang
    - update_nama_item(nama, nama_baru): Memperbarui nama item di keranjang
    """
    def __init__(self):
        self.keranjang = {} 
        self.total_harga = 0
        self.final_price = 0
      
    def add_barang(self, nama, harga, jumlah): 
        """
        Menambahkan item baru ke keranjang.
        Jika harga atau jumlah kurang dari atau sama dengan 0, menimbulkan ValueError.
        """
        try:
            if harga <= 0 or jumlah <= 0:
                raise ValueError
            else:
                self.keranjang[nama] = [harga, jumlah]
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
            del self.keranjang[nama]
            return
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
                self.keranjang.update({nama_baru: self.keranjang.pop(nama)})
                return
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
                self.keranjang[nama][1] = jumlah_baru
                return
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
                self.keranjang[nama][0] = harga_baru #salah disini kemaren, salah index sama harga_baru gak usah list
                return
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
        return

    def check_order(self):        
      key = [key for key in self.keranjang.keys()]
      value1 = [value[0] for value in self.keranjang.values()]
      value2 = [value[1] for value in self.keranjang.values()]
      col_width = [15, 15, 15, 15]
      print(" ")
      print(
          "Nama Item".ljust(col_width[0])
          + "Jumlah".ljust(col_width[1])
          + "Harga".ljust(col_width[2])
          + "Total Harga".ljust(col_width[3])
      )
      print("-" * (col_width[0] + col_width[1] + col_width[2] + col_width[3]))
      for key, value1, value2 in zip(key, value1, value2):
          tot_price = value1 * value2
          print(
              key.ljust(col_width[0])
              + str(value2).ljust(col_width[1])
              + str(value1).ljust(col_width[2])
              + str(tot_price).ljust(col_width[3])
          )
      
    def total_pembelian(self):
        """Untuk passing total pembelian"""
        self.total_harga = 0 
        self.total_tipe = 0
        self.total_kuantitas = 0

        for nama, value in self.keranjang.items():
            self.total_harga += value[0] * value[1]
            self.total_tipe = len(self.keranjang)
            self.total_kuantitas += value[1] 
        print(f"Total harga: Rp{self.total_harga}")
        print(f"Jumlah tipe barang: {self.total_tipe}")
        print(f"Jumlah kuantitas barang: {self.total_kuantitas}")
        print(" ")
          
    def discount_input(self):
        """Logic agar discount dapat terinput pada total pembelian"""
        if self.total_harga >= 500000:
            discount = self.total_harga * 0.10
            
        elif self.total_harga >= 300000:
            discount =  self.total_harga * 0.08
        elif self.total_harga >= 200000:
            discount = self.total_harga * 0.05
        else:
            discount = 0
        self.final_price = self.total_harga - discount

        print(f"Setelah discount: {self.final_price}")
        print(" ")
        if self.final_price == self.total_harga:
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
            elif uang < self.final_price:
              print(" ")
              print("Pembayaran Gagal, uang tidak cukup")
              print(" ")
            else:
              kembalian = uang - self.final_price
              print(" ")
              print(f"kembalian : {kembalian}")
              print("Terimakasih telah berbelanja!")
              print(" ")
              self.keranjang.clear()
        except ValueError:
            print(" ")
            print("Kamu belum input nominal! ")
            print(" ")
      
