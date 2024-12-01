belanja = int(input("Masukkan jumlah belanja: "))
diskon1 = belanja*0.1
diskon2 = belanja*0.05
total1 = belanja-diskon1
total2 = belanja-diskon2

if belanja > 250.000:
    print(f"diskon: Rp{diskon1}\ntotal: Rp{total1}")
else:
    print(f"diskon: Rp{diskon2}\ntotal: Rp{total2}")