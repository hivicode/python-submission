def main():
    keranjang = []

    while True:
        print("1. Tambahkan Barang")
        print("2. Hapus Barang")
        print("3. Edit Nama Barang")
        print("4. Edit Jumlah Barang")
        print("5. Edit Harga Barang")
        print("6. Reset Transaksi")
        print("7. Lihat Keranjang")
        print("8. Lihat Total Belanja")
        print("9. Bayar")
        print("10. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = float(input("Masukkan harga barang: "))
            keranjang.append({"nama": nama, "jumlah": jumlah, "harga": harga})
        elif pilihan == "2":
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            keranjang = [barang for barang in keranjang if barang["nama"] != nama]
        elif pilihan == "3":
            nama = input("Masukkan nama barang yang ingin diedit: ")
            for barang in keranjang:
                if barang["nama"] == nama:
                    barang["nama"] = input("Masukkan nama baru: ")
                    break
        elif pilihan == "4":
            nama = input("Masukkan nama barang yang ingin diedit: ")
            for barang in keranjang:
                if barang["nama"] == nama:
                    barang["jumlah"] = int(input("Masukkan jumlah baru: "))
                    break
        elif pilihan == "5":
            nama = input("Masukkan nama barang yang ingin diedit: ")
            for barang in keranjang:
                if barang["nama"] == nama:
                    barang["harga"] = float(input("Masukkan harga baru: "))
                    break
        elif pilihan == "6":
            keranjang = []
        elif pilihan == "7":
            for barang in keranjang:
                print(f"Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
        elif pilihan == "8":
            total = sum(barang["jumlah"] * barang["harga"] for barang in keranjang)
            print(f"Total Belanja: {total}")
        elif pilihan == "9":
            total = sum(barang["jumlah"] * barang["harga"] for barang in keranjang)
            print(f"Total yang harus dibayar: {total}")
            keranjang = []
        elif pilihan == "10":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()