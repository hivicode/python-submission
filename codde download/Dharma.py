#FUNCTION - MENAMPILKAN MENU
def menu():
    print("Menu: ")
    print("1. Tambah Barang")
    print("2. Lihat Daftar")
    print("3. Total Seluruh")
    opsi = input("Pilih nomor pada daftar: ")
    return opsi

#FUNCTION - MENGHITUNG HARGA (JUMLAH X HARGA)
def qty_ex_pcy(qty, pcy):
    return qty * pcy

#FUNCTION  & DICTIONARY- MENYIMPAN DATA YG SUDAH DIMASUKAN PADA INPUT AWALAN (HARGA, JUMLAH, NAMA BARANG)
def plus_tag():
    item_tag = input("Masukan nama barang, press enter jika tidak ada barang: ")
    if item_tag.lower() == '':
        return None
    pcy_tag = float(input(f"Masukan harga barang {item_tag}: "))
    qty_tag = int(input(f"Jumlah barang {item_tag}: "))
    item_info = {
        'Nama Barang': item_tag,
        'Harga Barang': pcy_tag,
        'Jumlah Barang': qty_tag,
        'Total': qty_ex_pcy(qty_tag, pcy_tag) 
    }
    d_list.append(item_info)

#FUNCTION - PENGECEKAN BARANG ADA ATAU TIDAK & MENAMPILKAN BARANG SERTA HARGA
def show_list():
    if not d_list:
        print("Ga ada data yang dimasukin")
    else:
        print("List Barang & Harga")
        print(f"{'Nama Barang':<20}{'Harga Barang':<10}{'Jumlah Barang':<10}{'Total':<10}")
        print("-" * 50)
        for list_item in d_list:
            print(f"{list_item['Nama Barang']:<20}{list_item['Harga Barang']:<10}{list_item['Jumlah Barang']:<10}{list_item['Total']:<10}")

#FUNCTION - PENENTUAN HASIL AKHIR BENTUK NOTA KASIR
def total_result():
    if not d_list:
        print("Tidak ada data barang yang dimasukin")
    else:
        total = sum(list_item['Total'] for list_item in d_list)
        print(f"{'Nama Barang':<20}{'Harga Barang':<10}{'Jumlah Barang':<10}{'Total':<10}")
        print("-" * 50)
        for list_item in d_list:
            print(f"{list_item['Nama Barang']:<20}{list_item['Harga Barang']:<10}{list_item['Jumlah Barang']:<10}{list_item['Total']:<10}")
        print("-" * 50)
        print(f"{'Total Keseluruhan':<20}{'':<10}{'':<10}{total:<10}")

# LIST - MENYIMPAN DATA YANG TELAH DI-INPUT
d_list = []

#LOOPING - WHILE TRUE AGAR BISA MENGULANG
while True:
    opsi = menu()
    if opsi == '1':
        plus_tag()
    elif opsi == '2':
        show_list()
    elif opsi == '3':
        total_result()
    else:
        break
