from os import system

def inputan(unit): #fungsi untuk input
    masukan = int(input(unit + ': '))
    return masukan

def energi(daya, penggunaan): #fungsi untuk menghitung kwh
    kwh = daya * penggunaan / 1000
    return kwh

def totalenergi(energi1, energi2, energi3): #fungsi untuk menghitung total kwh
    totalkwh = energi1 + energi2 + energi3
    return totalkwh

def biaya(energi, harga): #fungsi untuk mehitung biaya
    harian = energi * harga
    return harian

def main():
    hargakwh = 1500
    garis = u"\u2500" * 20
    print(f"Masukkan daya barang dalam watt (hanya angka)\n{garis}")
    dayaLampu = inputan("Daya Lampu")
    dayaKipas = inputan("Daya Kipas")
    dayaTelevisi = inputan("Daya Televisi")
    print(f"\nMasukkan lama penggunaan barang dalam jam di satu hari (hanya angka)\n{garis}")
    penggunaanLampu = inputan("Penggunaan Lampu")
    penggunaanKipas = inputan("Penggunaan Kipas")
    penggunaanTelevisi = inputan("Penggunaan Televisi")

    system("cls")
    system("cls") #membersihkan inputan
    
    print(f"Daya\n{garis}\nLampu: {dayaLampu} watt\nKipas: {dayaKipas} watt\nTelevisi: {dayaTelevisi} watt\n") #menampilkan rincian inputan
    print(f"Lama Penggunaan\n{garis}\nLampu: {penggunaanLampu} jam\nKipas: {penggunaanKipas} jam\nTelevisi: {penggunaanTelevisi} jam\n")

    kwhLampu = energi(dayaLampu, penggunaanLampu)
    kwhKipas = energi(dayaKipas, penggunaanKipas)
    kwhTelevisi = energi(dayaTelevisi, penggunaanTelevisi)
    totalkwh = totalenergi(kwhLampu, kwhKipas, kwhTelevisi)
    print(f"Energi\n{garis}\nLampu: {kwhLampu} kWh\nKipas: {kwhKipas} kWh\nTelevisi: {kwhTelevisi} kWh\nTotal Energi Semua Barang: {totalkwh} kWh\n")

    biayaLampu = biaya(kwhLampu, hargakwh)
    biayaKipas = biaya(kwhKipas, hargakwh)
    biayaTelevisi = biaya(kwhTelevisi, hargakwh)
    biayaharian = biaya(totalkwh, hargakwh)
    biayabulanan = biaya(biayaharian, 30)
    print(f"Biaya\n{garis}\nLampu: Rp{biayaLampu}/hari\nKipas: Rp{biayaKipas}/hari\nTelevisi: Rp{biayaTelevisi}/hari{"\n"*2}Total Biaya:\nRp{biayaharian}/hari\nRp{biayabulanan}/bulan")
main()