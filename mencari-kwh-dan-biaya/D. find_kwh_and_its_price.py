from os import system
system("cls")
garis = u'\u2500' * 20 #unicode underline
hargakwh = 1500

# menentukan dan menginput watt atau daya setiap barang
print(f"Masukkan daya barang dalam watt (hanya angka)\n{garis}")
dayaLampu = int(input("Daya Lampu: "))
dayaKipas = int(input("Daya Kipas: "))
dayaTelevisi = int(input("Daya Televisi: "))
print()
# menginputkan lama penggunaan setiap barang
print(f"Masukkan lama penggunaan barang dalam jam di satu hari (hanya angka)\n{garis}")
penggunaanLampu = int(input("Penggunaan Lampu: "))
penggunaanKipas = int(input("Penggunaan Kipas: "))
penggunaanTelevisi = int(input("Penggunaan Televisi: "))

system("cls")
system("cls") #membersihkan inputan

# menampilkan inputan daya dan lama penggunaan
print(f"Daya\n{garis}\nLampu: {dayaLampu} watt\nKipas: {dayaKipas} watt\nTelevisi: {dayaTelevisi} watt")
print()
print(f"Lama Penggunaan\n{garis}\nLampu: {penggunaanLampu} jam\nKipas: {penggunaanKipas} jam\nTelevisi: {penggunaanTelevisi} jam")
print()

# menghitung energi yang digunakan dalam unit kWh pada setiap barang berdasarkan lama penggunaan (daya*penggunaan/1000)
energiLampu = dayaLampu*penggunaanLampu/1000
energiKipas = dayaKipas*penggunaanKipas/1000
energiTelevisi = dayaTelevisi*penggunaanTelevisi/1000
totalenergi = energiLampu+energiKipas+energiTelevisi
print(f"Energi (kWh)\n{garis}\nLampu: {energiLampu} kWh\nKipas: {energiKipas} kWh\nTelevisi: {energiTelevisi} kWh")
print(f"Total energi semua barang: {totalenergi}kwh")
print()

# menghitung biaya setiap dan semua barang berdasarkan energi (energi*harga)
biayaLampu = energiLampu*hargakwh
biayaKipas = energiKipas*hargakwh
biayaTelevisi = energiTelevisi*hargakwh
biayaharian = biayaLampu+biayaKipas+biayaTelevisi
biayabulanan = biayaharian*30
print(f"Biaya\n{garis}\nLampu: Rp{biayaLampu}/hari\nKipas: Rp{biayaKipas}/hari\nTelevisi: Rp{biayaTelevisi}/hari{"\n"*2}Total Biaya:\nRp{biayaharian}/hari\nRp{biayabulanan}/bulan")