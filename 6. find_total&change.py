harga = int(input("Harga Barang: ")) 
jumlah = int(input("Jumlah Barang: ")) 
total = harga*jumlah
print("Total Harga: ", total)
bayar = int(input("Jumlah Pembayaran: "))
kembalian = bayar-total
print("Kembalian: ", kembalian)