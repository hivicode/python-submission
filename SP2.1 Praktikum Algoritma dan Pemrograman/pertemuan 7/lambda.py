# Pertemuan 7 (penambahan input untuk panjang dan lebar)
# Nama: Bintang Fathir F.A
# NIM: 1124102166

def luastanah(panjang, lebar):
    luas = panjang*lebar
    return luas 

inputpanjang = int(input("masukkan panjang :"))
inputlebar = int(input("masukkan lebar :"))
print(f"luas tanah: {luastanah(inputpanjang, inputlebar)}")

luas = lambda panjang, lebar : panjang*lebar
print(f"luas tanah (lambda 1): {luas(inputpanjang, inputlebar)}")

print(f"luas tanah (lambda 2): {(lambda panjang, lebar : panjang*lebar)(inputpanjang, inputlebar)}")
