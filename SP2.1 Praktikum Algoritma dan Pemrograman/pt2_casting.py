# TIPE DATA (studi kasus sendiri)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

# studi kasus: mengubah tipe data dari harga barang

#input harga barang dengan tipe data string
harga = input("Harga Barang: ")

#variable tipe data
int_harga = int(harga) #adding *integer* to convert
float_harga = float(harga) #addding *float* to convert

#output tipe data yang telah diinput beserta yang sudah diubah
print (harga, type(harga))
print (int_harga, type(int_harga))
print (float_harga, type(float_harga))
