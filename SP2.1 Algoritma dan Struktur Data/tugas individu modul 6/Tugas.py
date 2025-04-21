class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
    
    def enqueue(self, data):
        data = str(input("Object yang ingin ditambahkan: "))
        self.queue.append(data)
        print(f"Data '{data}' berhasil ditambahkan ke dalam queue.")

    def dequeue(self):
        self.queue.pop(0)
        print(f"Data '{data}' berhasil dihapus dari queue.")

    def size(self):
        return len(self.queue)

    def max_length(self):
        return self.max_size
    
    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def display(self):
        print("Isi queue saat ini:", self.queue)

def main():
    max_size = int(input("Maxsize: "))
    q = Queue(max_size)

    while True:
        print("\nMenu:")
        print("1. Input data")
        print("2. Hapus data")
        print("3. Lihat panjang")
        print("4. Lihat kapasitas maksimal")
        print("5. Cek kosong")
        print("6. Cek penuh")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            data = input("Masukkan data yang akan ditambahkan: ")
            q.enqueue(data)
        elif pilihan == "2":
            q.dequeue()
        elif pilihan == "3":
            print("Panjang queue saat ini:", q.size())
        elif pilihan == "4":
            print("Kapasitas maksimal queue:", q.max_length())
        elif pilihan == "5":
            print("Queue kosong:", q.is_empty())
        elif pilihan == "6":
            print("Queue penuh:", q.is_full())
        elif pilihan == "8":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
