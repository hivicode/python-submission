class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, data):
        if self.is_full():
            print("Queue penuh! Tidak bisa menambahkan data.")
        else:
            self.queue.append(data)
            print(f"Data '{data}' berhasil ditambahkan ke dalam queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong! Tidak ada data yang bisa dihapus.")
        else:
            removed = self.queue.pop(0)
            print(f"Data '{removed}' berhasil dihapus dari queue.")

    def size(self):
        return len(self.queue)

    def max_length(self):
        return self.max_size

    def display(self):
        print("Isi queue saat ini:", self.queue)

def main():
    max_size = int(input("Masukkan kapasitas maksimal queue: "))
    q = Queue(max_size)

    while True:
        print("\nMenu:")
        print("1. Input data (enqueue)")
        print("2. Hapus data (dequeue)")
        print("3. Lihat panjang queue")
        print("4. Lihat kapasitas maksimal queue")
        print("5. Cek apakah queue kosong")
        print("6. Cek apakah queue penuh")
        print("7. Tampilkan isi queue")
        print("8. Keluar")

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
        elif pilihan == "7":
            q.display()
        elif pilihan == "8":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
