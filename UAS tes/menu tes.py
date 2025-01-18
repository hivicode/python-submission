from os import system
from main import Transaksi
ts = Transaksi()

while True:
    print("-" * 60+"\nTOKO LMB\n"+"-" * 60)
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Ubah Nama Barang")
    print("4. Ubah Jumlah Barang")
    print("5. Ubah Harga Barang")
    print("6. Ulangi Transaksi")
    print("7. Lihat Keranjang")
    print("8. Lihat Total Belanja")
    print("9. Keluar")
    print("10. Bayar")
    print(" ")

    try:
        choice = int(input("Pilih nomor: "))
        if choice == 1:
            nama_item = str(input("Nama Barang: "))
            harga = int(input("Harga: "))
            jumlah = int(input("Jumlah: "))
            system("cls")
            ts.add_barang(nama_item, harga, jumlah)
            ts.check_order()

        elif choice == 2:
            hapus_barang = str(input("Nama barang yang ingin dihapus: "))
            system("cls")
            ts.delete_item(hapus_barang)
            ts.check_order()

        elif choice == 3:
            edit_nama_item = str(input("Ubah nama item yang kamu pilih: "))
            nama_baru = str(input("Nama baru: "))
            system("cls")
            ts.update_nama_item(edit_nama_item, nama_baru)
            ts.check_order()

        elif choice == 4:
            edit_jumlah_barang = str(input("Barang yang ingin diganti: "))
            jumlah_barang_baru = int(input("Masukkan jumlah: "))
            system("cls")
            ts.update_jumlah_item(edit_jumlah_barang, jumlah_barang_baru)
            ts.check_order()

        elif choice == 5:
            edit_harga_barang = str(input("Barang yang ingin diganti: "))
            harga_barang_baru = int(input("Masukkan harga: "))
            system("cls")
            ts.update_harga_item(edit_harga_barang, harga_barang_baru)
            ts.check_order()

        elif choice == 6:
            reset_transaksi = str(input("Ingin mengulang transaksi? (YES/NO): "))
            if reset_transaksi.upper() == "NO":
                print("Reset dibatalkan")
            elif reset_transaksi.upper() == "YES":
                ts.reset_item()
            else:
                print("Pilihan mu tidak benar!") 

        elif choice == 7:
            if len(ts.keranjang) == 0:
                print("Keranjang kosong")
            else:
                ts.check_order()
                
        elif choice == 8:
            system("cls")
            ts.total_pembelian()
            ts.discount_input() 

        elif choice == 9:
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

        elif choice == 10:
            keluar = str(input("Yakin mau keluar YES/NO : "))
            if keluar.upper() == "YES":
                break
            else:
                keluar.upper() == "NO"
                continue 
        else:
            print(" ")
            print("Bukan pilihan inputan ")
            print(" ")          
    except ValueError:
        print(" ")
        print("Inputan Anda Salah")
        print(" ")