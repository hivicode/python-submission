import ShellSort

def GenerateElement():
    print("Masukkan elemen array (pisahkan dengan koma): ")
    user_input = input("Contoh: 86,54,33,75,45\n>> ")
    try:
        dataelement = [int(x.strip()) for x in user_input.split(",")]
        return dataelement
    except ValueError:
        print("Input tidak valid. Gunakan hanya angka dan koma.")
        return GenerateElement()

def MainMenu():
    element = GenerateElement()
    sorter = ShellSort.ShellSort()
    
    
    print("\nData sebelum diurutkan:")
    ShellSort.ShellSort.print_array(element)
    
    sorter.sorter(element)

    print("\nData setelah diurutkan:")
    ShellSort.ShellSort.print_array(element)

    pilih = "y"
    while pilih.lower() == "y":
        print("\nMenu Tambahan")
        print("1. Tampilkan Data Lagi")
        print("2. Keluar")
        print("="*25)
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            print("Data saat ini:")
            ShellSort.ShellSort.print_array(element)
        elif pilihan == "2":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
        pilih = input("Ingin kembali ke menu? (y/n): ")

if __name__ == "__main__":
    MainMenu()
