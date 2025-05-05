import functionstack
from os import system

def menu1():
    s = functionstack.Stack()
    while True:
        print("=" * 23)
        print("| Menu Aplikasi Stack |")
        print("=" * 23)
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Object Terakhir")
        print("5. Panjang Dari Stack")
        print("6. Kembali ke Menu Utama")
        print("=" * 20)

        pilihan = input("Masukkan pilihan (1-6): ")
        if pilihan == "1":
            obj = input("Object yang ingin ditambahkan: ")
            s.Push(obj)
            print(f"Object '{obj}' telah ditambahkan.")
        elif pilihan == "2":
            if not s.isEmpty():
                print(f"Object '{s.Pop()}' dihapus.")
            else:
                print("Stack kosong! Tidak ada object yang dihapus.")
        elif pilihan == "3":
            print("Stack kosong?" , s.isEmpty())
        elif pilihan == "4":
            if not s.isEmpty():
                print("Object terakhir:", s.Peek())
            else:
                print("Stack kosong! Tidak ada object.")
        elif pilihan == "5":
            print("Panjang dari Stack adalah", s.Size())
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-6.")
        print()