from os import system
from main import Transaksi
ts = Transaksi()


"""
Program cashier ini memungkinkan customer untuk menambah, menghapus, mengedit, 
dan melihat barang dalam keranjang belanja, dan melakukan proses checkout dengan menghitung total pembelian, diskon, dan pembayaran.

Kelas Transaksi dari modul utama memegang informasi keranjang belanja dan semua operasi yang dilakukan. 
Program ini menggunakan instance kelas Transaksi, ts untuk melakukan semua operasi.

Program berjalan dalam sebuah loop while, di mana customer diminta untuk memilih dari 10 opsi:

Tambah barang
Hapus barang
Edit nama barang
Edit jumlah barang
Edit harga barang
Reset keranjang belanja
Lihat keranjang belanja
Lihat total pembelian
Keluar dari sistem
Proses checkout

Untuk setiap opsi, program melakukan tindakan yang sesuai dengan memanggil metode yang sesuai dalam kelas Transaksi. 
Input pengguna di cast ke integer atau string, dan manajemen error dilakukan menggunakan blok try-except.
"""


while True:
    print("-" * 60)
    print("PYTHON CASHIER PROGRAM v1.3")
    print("-" * 60)
    print("1. Tambahkan Barang")
    print("2. Hapus Barang")
    print("3. Edit Nama Barang")
    print("4. Edit Jumlah Barang")
    print("5. Edit Harga Barang")
    print("6. Reset Transaksi")
    print("7. Lihat Keranjang")
    print("8. Lihat Total Belanja")
    print("9. Keluar dari Sistem")
    print("10. Check out barang?")
    print(" ")

    try:
        choice = int(input("Masukkan nomor : "))
        """Memasukkan nama,harga,dan jumlah barang yang akan dimasukkan ke keranjang"""
        if choice == 1:
            nama_item = str(input("Input nama barang : "))
            harga = int(input("Input harga  : "))
            jumlah = int(input("Input jumlah : "))
            ts.add_barang(nama_item, harga, jumlah)
            ts.check_order()

        elif choice == 2:
            """Menghapus barang dari keranjang belanja."""
            hapus_barang = str(input("Nama barang yang akan dihapus: "))
            ts.delete_item(hapus_barang)
            ts.check_order()

        elif choice == 3:
            """Mengedit nama barang yang ada di keranjang belanja."""
            edit_nama_item = str(input("Edit nama item yang kamu pilih: "))
            nama_baru = str(input("Nama baru nya apa?: "))
            ts.update_nama_item(edit_nama_item, nama_baru)
            ts.check_order()

        elif choice == 4:
            """Mengedit jumlah barang yang ada di keranjang belanja."""
            edit_jumlah_barang = str(input("Barang yang mau di ganti apa?: "))
            jumlah_barang_baru = int(input("Input jumlah barang nya: "))
            ts.update_jumlah_item(edit_jumlah_barang, jumlah_barang_baru)
            ts.check_order()

        elif choice == 5:
            """Mengedit harga barang yang ada di keranjang belanja."""
            edit_harga_barang = str(input("Barang yang mau di ganti apa?: "))
            harga_barang_baru = int(input("Input harga baru nya: "))
            ts.update_harga_item(edit_harga_barang, harga_barang_baru)
            ts.check_order()

        elif choice == 6:
            """Mereset total transaksi di keranjang belanja"""
            reset_transaksi = str(input("KAMU YAKIN? YES/NO: "))
            if reset_transaksi.upper() == "NO":
                print("Reset dibatalkan")
            elif reset_transaksi.upper() == "YES":
                ts.reset_item()
            else:
                print("Pilihan mu tidak benar!") 

        elif choice == 7:
            """Melihat total seluruh dari transaksi di keranjang belanja"""
            if len(ts.keranjang) == 0:
                system("cls")
                print("\nKeranjang kosong\n")
            else:
                ts.check_order()
                
        elif choice == 8:
            """Melihat total dari pembelanjaan sekaligus melihat discount terinput"""
            ts.total_pembelian()
            ts.discount_input() 

        elif choice == 9:
            """Keluar dari sistem kasir secara total"""
            keluar = str(input("Yakin mau keluar YES/NO : "))
            if keluar.upper() == "YES":
                break
            else:
                keluar.upper() == "NO"
                continue 

        elif choice == 10:
            """Customer membayar transaksi dari total di keranjang belanja"""
            ts.check_order()
            ts.total_pembelian()
            ts.discount_input()
            print(" ")
            customer_bayar = int(input("Masukkan total sesuai harga: "))
            ts.pembayaran(customer_bayar)
            belanja_lagi = str(input("Mau belanja lagi? YES/NO : "))
            if belanja_lagi.upper() == "YES":
                continue
            else:
                belanja_lagi.upper() == "NO"
                break 

        else:
            print(" ")
            print("Bukan pilihan inputan ")
            print(" ")
            
    except ValueError:
        system("cls")
        print("\nInputan Anda Salah\n")