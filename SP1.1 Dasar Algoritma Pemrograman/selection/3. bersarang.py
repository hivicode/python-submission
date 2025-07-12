belanja = int(input("Masukkan jumlah belanja: "))
item = int(input("Masukkan jumlah item: "))
diskon1 = belanja*0.1
diskon2 = belanja*0.05
total1 = belanja-diskon1*item
total2 = belanja-diskon2*item

if belanja >= 250000:
    if item >= 3:
        print(f"diskon: Rp{diskon1}\ntotal: Rp{total1}")
    else:
        print(f"diskon: Rp{diskon2}\ntotal: Rp{total2}")
else:
    print(belanja*item)