def inputan(unit):
    masukan = int(input(unit + ': ')) #fungsi untuk input
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
    dayaLampu = inputan("Daya Lampu")
    dayaKipas = inputan("Daya Kipas")
    dayaTelevisi = inputan("Daya Televisi")
    penggunaanLampu = inputan("Penggunaan Lampu")
    penggunaanKipas = inputan("Penggunaan Kipas")
    penggunaanTelevisi = inputan("Penggunaan Televisi")

    kwhLampu = energi(dayaLampu, penggunaanLampu)
    kwhKipas = energi(dayaKipas, penggunaanKipas)
    kwhTelevisi = energi(dayaTelevisi, penggunaanTelevisi)
    totalkwh = totalenergi(kwhLampu, kwhKipas, kwhTelevisi)
    print(f"Lampu: {kwhLampu}kwh\nKipas: {kwhKipas}kwh\nTelevisi: {kwhTelevisi}kwh\nTotal Energi Semua Barang: {totalkwh}kWh")

    biayaharian = biaya(totalkwh, hargakwh)
    biayabulanan = biaya(biayaharian, 30)
    print(f"Biaya: Rp{biayaharian}/hari, Rp{biayabulanan}/bulan")
main()