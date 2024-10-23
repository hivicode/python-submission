from os import system
def main():
    print()
    num = int(input("Masukkan angka pertama: "))
    same = int(input("Masukkan angka kedua: "))
    system("cls")
    print("Angka Pertama: ", num)
    print("Angka Kedua: ", same)
    print()
    num += same
    print("ditambah", same, "=", num)
    num -= same
    print("dikurangi", same, "=", num)
    num *= same
    print("dikali", same, "=", num)
    num /= same
    print("dibagi", same, "=", int(num))
    num //= same
    print("hasil bagi", same, "=", int(num))
    num %= same
    print("sisa hasil bagi", same, "=", int(num))
    num **= same
    print("dipangkat", same, "=", int(num))
while True:
    main() 
# Bintang Fathir_1124102166