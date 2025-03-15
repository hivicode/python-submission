from os import system
system("clear")
from main import transaksi
ts = transaksi()

while True:
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Ubah Nama Barang")
    print("4. Ubah Jumlah Barang")
    print("5. Ubah Harga Barang")
    print("6. Lihat Keranjang")
    print("7. Hapus Keranjang")
    print("8. Pembayaran")
    print("9. Keluar")
    print(" ")

    try:
        choice = int(input("Pilih Nomor : "))
        if choice == 1:
            barang = str(input("Masukkan Nama Barang: "))
            harga = int(input("Masukkan Harga: "))
            jumlah = int(input("Masukkan Jumlah: "))
            system("clear")
            ts.tambah_barang(barang, harga, jumlah)
            ts.lihat_keranjang()
        
        elif choice == 2:
            hapus_barang = str(input("Nama Barang Yang Ingin Dihapus: "))
            system("clear")
            ts.hapus_barang(hapus_barang)
            ts.lihat_keranjang()

        elif choice == 3:
            ubah_nama = str(input("Nama Barang Yang Ingin Diubah: "))
            nama_baru = str(input("Masukkan Nama Baru: "))
            system("clear")
            ts.ubah_namabarang(ubah_nama, nama_baru)
            ts.lihat_keranjang()
            
        
        elif choice == 4:
            ubah_jumlah = str(input("Nama Barang Yang Ingin Diubah: "))
            jumlah_baru = int(input("Masukkan Jumlah Baru: "))
            system("clear")
            ts.ubah_jumlahbarang(ubah_jumlah, jumlah_baru)
            ts.lihat_keranjang()

        elif choice == 5:
            ubah_harga = str(input("Nama Barang Yang Ingin Diubah: "))
            harga_baru = int(input("Masukkan Harga Baru: "))
            system("clear")
            ts.ubah_harga(ubah_harga, harga_baru)
            ts.lihat_keranjang()

        elif choice == 6:
            system("clear")
            if len(ts.keranjang) == 0:
                print("\nKeranjang Kosong!\n")
            else:
                ts.lihat_keranjang()

        elif choice == 7:
            hapus_keranjang = str(input("Ingin Menghapus Semua Barang Dalam Keranjang? (y/n): "))
            if hapus_keranjang.upper() == "N":
                print("Batal Menghapus")
            elif hapus_keranjang.upper() == "Y":
                system("clear")
                ts.hapus_semua()
            else:
                print("Mohon Pilih y atau n!")

        elif choice == 8:
            ts.total_jumlah()
            bayar_tunai = int(input("Masukkan Jumlah Tunai Anda: "))
            system("clear")
            ts.header()
            ts.lihat_keranjang()
            ts.diskon()
            print("{:<53} {:<15}".format("Tunai", bayar_tunai))
            ts.bayar(bayar_tunai)
            belanja_lagi = str(input("Ingin Belanja Lagi? (y/n): "))
            if belanja_lagi.upper() == "Y":
                system("clear")
                ts.hapus_semua()
                continue
            else:
                belanja_lagi.upper() == "N"
                break
        
        elif choice == 9:
            keluar = str(input("Yakin? (y/n): "))
            if keluar.upper() == "Y":
                system("clear")
                break
            else:
                keluar.upper() == "N"
                continue

        else:
            system("clear")
            print("\nPilihan Nomor Tidak Valid\n")

    except ValueError:
        system("clear")
        print("\nMohon Masukkan Yang Benar\n")
