import mainqueue

def MainMenu():
    q = mainqueue.Queue()
    pilih = "y"
    while (pilih == "y"):
        print("| Menu Aplikasi Stack |")
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Object Terakhir")
        print("5. Panjang Dari Stack")
        print("="*20)

        pilihan = str(input("Masukkan pilihan: "))
        if pilihan == "1":
            print("Hallo")
            obj = str(input("Object yang ingin ditambahkan: "))
            q.Push(obj)
            print("Object " + obj + " telah ditambahkan")
        elif pilihan == "2":
            print("Object " + q.Pop() + " dihapus")
        elif pilihan == "3":
            print(q.isEmpty())
        elif pilihan == "4":
            print("Object terakhir: " + q.Peek())
        else:
            print("Panjang dari Stack adalah "+ str(q.Size()))

if __name__ == "__main__":
    MainMenu()