from os import system
system("cls")
from utsmain import transaksi
ts = transaksi()

while True:
    print("Menu:")
    print("1. Tambah Pelanggan ke Antrian")
    print("2. Proses Pelanggan dari Antrian")
    print("3. Tambah Barang")
    print("4. Hapus Barang")
    print("5. Kembalikan Barang yang Dihapus")
    print("6. Ubah Nama Barang")
    print("7. Ubah Jumlah Barang")
    print("8. Ubah Harga Barang")
    print("9. Lihat Keranjang")
    print("10. Hapus Keranjang")
    print("11. Pembayaran")
    print("12. Keluar")
    print(" ")

    try:
        choice = int(input("Pilih Nomor : "))
        if choice == 1:
            nama_pelanggan = str(input("Masukkan Nama Pelanggan: "))
            system("cls")
            ts.tambah_pelanggan(nama_pelanggan)

        elif choice == 2:
            system("cls")
            ts.proses_pelanggan()

        elif choice == 3:
            barang = str(input("Masukkan Nama Barang: "))
            harga = int(input("Masukkan Harga: "))
            jumlah = int(input("Masukkan Jumlah: "))
            system("cls")
            ts.tambah_barang(barang, harga, jumlah)
            ts.lihat_keranjang()
        
        elif choice == 4:
            hapus_barang = str(input("Nama Barang Yang Ingin Dihapus: "))
            system("cls")
            ts.hapus_barang(hapus_barang)
            ts.lihat_keranjang()

        elif choice == 5:
            system("cls")
            ts.kembalikan_barang()

        elif choice == 6:
            ubah_nama = str(input("Nama Barang Yang Ingin Diubah: "))
            nama_baru = str(input("Masukkan Nama Baru: "))
            system("cls")
            ts.ubah_namabarang(ubah_nama, nama_baru)
            ts.lihat_keranjang()
            
        elif choice == 7:
            ubah_jumlah = str(input("Nama Barang Yang Ingin Diubah: "))
            jumlah_baru = int(input("Masukkan Jumlah Baru: "))
            system("cls")
            ts.ubah_jumlahbarang(ubah_jumlah, jumlah_baru)
            ts.lihat_keranjang()

        elif choice == 8:
            ubah_harga = str(input("Nama Barang Yang Ingin Diubah: "))
            harga_baru = int(input("Masukkan Harga Baru: "))
            system("cls")
            ts.ubah_harga(ubah_harga, harga_baru)
            ts.lihat_keranjang()

        elif choice == 9:
            system("cls")
            if len(ts.keranjang) == 0:
                print("\nKeranjang Kosong!\n")
            else:
                ts.lihat_keranjang()

        elif choice == 10:
            hapus_keranjang = str(input("Ingin Menghapus Semua Barang Dalam Keranjang? (y/n): "))
            if hapus_keranjang.upper() == "N":
                print("Batal Menghapus")
            elif hapus_keranjang.upper() == "Y":
                system("cls")
                ts.hapus_semua()
            else:
                print("Mohon Pilih y atau n!")

        elif choice == 11:
            ts.total_jumlah()
            bayar_tunai = int(input("Masukkan Jumlah Tunai Anda: "))
            system("cls")
            ts.header()
            ts.lihat_keranjang()
            ts.diskon()
            print("{:<53} {:<15}".format("Tunai", bayar_tunai))
            ts.bayar(bayar_tunai)
            belanja_lagi = str(input("Ingin Belanja Lagi? (y/n): "))
            if belanja_lagi.upper() == "Y":
                system("cls")
                ts.hapus_semua()
                ts.proses_pelanggan()
                continue
            elif belanja_lagi.upper() == "N":
                break
            else:
                system("cls")
                print("\nAnda tidak memilih y, program dilanjutkan\n")
                

        elif choice == 12:
            keluar = str(input("Yakin? (y/n): "))
            if keluar.upper() == "Y":
                system("cls")
                break
            elif keluar.upper() == "N":
                continue
            else:
                system("cls")
                print("\nAnda tidak memilih y, program dilanjutkan\n")

        else:
            system("cls")
            print("\nPilihan Nomor Tidak Valid\n")

    except ValueError:
        system("cls")
        print("\nMohon Masukkan Yang Benar\n")