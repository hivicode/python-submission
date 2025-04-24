import functionqueue

def menu2():
    while True:
        try:
            max_size = int(input("Masukkan kapasitas maksimal Queue: "))
            if max_size > 0:
                break
            else:
                print("Kapasitas maksimal harus lebih dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    q = functionqueue.Queue(max_size=max_size)
    while True:
        print("=" * 23)
        print("| Menu Aplikasi Queue |")
        print("=" * 23)
        print("1. Input Data")
        print("2. Hapus Data")
        print("3. Cek Data Terawal")
        print("4. Cek Maxsize")
        print("5. Cek Panjang")
        print("6. Cek Kosong")
        print("7. Cek Penuh")
        print("8. Kembali ke Menu Utama")
        print("=" * 20)

        pilihan = input("Masukkan pilihan (1-8): ")
        if pilihan == "1":
            obj = input("Data yang ingin ditambahkan: ")
            if q.Enqueue(obj):
                print(f"Data '{obj}' telah ditambahkan.")
            else:
                print("Queue penuh! Tidak bisa menambah data.")
        elif pilihan == "2":
            data = q.Dequeue()
            if data is not None:
                print(f"Data '{data}' dihapus.")
            else:
                print("Queue kosong! Tidak ada data yang dihapus.")
        elif pilihan == "3":
            data = q.Peek()
            if data is not None:
                print("Data terdepan:", data)
            else:
                print("Queue kosong! Tidak ada data.")
        elif pilihan == "4":
            print("Maxsize: ", q.MaxSize())
        elif pilihan == "5":
            print("Panjang dari Queue adalah", q.Size())
        elif pilihan == "6":
            print("Queue kosong?", q.isEmpty())
        elif pilihan == "7":
            print("Queue penuh?", q.isFull())
        elif pilihan == "8":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-7.")
        print()