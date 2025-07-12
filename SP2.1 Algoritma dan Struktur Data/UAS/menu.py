import random
import os
from classSort import Sort
from classSearch import Search

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]



def input_array_manually():
    print("\nMasukkan elemen array (pisahkan dengan spasi):")
    arr = list(map(int, input().split()))
    return arr

def display_array(arr, title="Array"):
    print(f"\n{title}: {arr}")

def sorting_menu_with_array(arr):
    sort_obj = Sort()
    
    print("\n=== MENU SORTING ===")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Kembali ke menu utama")
    
    choice = input("\nPilih algoritma sorting (1-6): ")
    
    if choice == "6":
        os.system('cls' if os.name == 'nt' else 'clear') #cls windows, clear linux
        return arr
    
    display_array(arr, "Array sebelum sorting")
    
    if choice == "1":
        result = sort_obj.bubble_sort(arr)
        algorithm = "Bubble Sort"
    elif choice == "2":
        result = sort_obj.selection_sort(arr)
        algorithm = "Selection Sort"
    elif choice == "3":
        result = sort_obj.insertion_sort(arr)
        algorithm = "Insertion Sort"
    elif choice == "4":
        result = sort_obj.merge_sort(arr)
        algorithm = "Merge Sort"
    elif choice == "5":
        result = sort_obj.quick_sort(arr)
        algorithm = "Quick Sort"
    else:
        print("Pilihan tidak valid! Silakan pilih algoritma sorting 1-6.")
        return arr
    
    display_array(result, f"Array setelah {algorithm}")
    input("\nTekan Enter untuk kembali ke menu utama...")
    os.system('cls' if os.name == 'nt' else 'clear')
    return result

def searching_menu_with_array(arr):
    search_obj = Search()
    
    print("\n=== MENU SEARCHING ===")
    print("1. Linear Search")
    print("2. Binary Search (Iterative)")
    print("3. Binary Search (Recursive)")
    print("4. Jump Search")
    print("5. Interpolation Search")
    print("6. Kembali ke menu utama")
    
    choice = input("\nPilih algoritma searching (1-6): ")
    
    if choice == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
    if choice in ["2", "3", "4", "5"]:
        if arr == sorted(arr):
            print("\nArray sudah terurut, siap untuk searching.")
        else:
            print("\nArray akan diurutkan terlebih dahulu untuk searching ini...")
            sort_obj = Sort()
            arr = sort_obj.quick_sort(arr)
            display_array(arr, "Array setelah diurutkan")
    
    target = int(input("\nMasukkan nilai yang ingin dicari: "))
    
    display_array(arr, "Array")
    print(f"Nilai yang dicari: {target}")
    
    if choice == "1":
        result = search_obj.linear_search(arr, target)
        algorithm = "Linear Search"
    elif choice == "2":
        result = search_obj.binary_search(arr, target)
        algorithm = "Binary Search (Iterative)"
    elif choice == "3":
        result = search_obj.recursive_binary_search(arr, target)
        algorithm = "Binary Search (Recursive)"
    elif choice == "4":
        result = search_obj.jump_search(arr, target)
        algorithm = "Jump Search"
    elif choice == "5":
        result = search_obj.interpolation_search(arr, target)
        algorithm = "Interpolation Search"
    else:
        print("Pilihan tidak valid! Silakan pilih algoritma searching 1-6.")
        return
    
    if result != -1:
        print(f"\nNilai {target} ditemukan pada indeks: {result}")
    else:
        print(f"\nNilai {target} tidak ditemukan dalam array")
    
    print(f"Algoritma: {algorithm}")
    input("\nTekan Enter untuk kembali ke menu utama...")
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        print("\n" + "="*50)
        print("           PROGRAM SORTING & SEARCHING")
        print("="*50)
        
        print("\n=== PILIHAN INPUT ARRAY ===")
        print("1. Input manual")
        print("2. Generate random array")
        
        choice = input("\nPilih metode input (1-2): ")
        
        if choice == "1":
            try:
                arr = input_array_manually()
            except:
                print("Input tidak valid!")
                continue
        elif choice == "2":
            try:
                size = int(input("Masukkan ukuran array: "))
                min_val = int(input("Masukkan nilai minimum: "))
                max_val = int(input("Masukkan nilai maksimum: "))
                if size <= 0 or min_val >= max_val:
                    print("Input tidak valid! Ukuran harus > 0 dan minimum < maksimum.")
                    continue
                arr = generate_random_array(size, min_val, max_val)
            except ValueError:
                print("Input tidak valid! Masukkan angka yang benar.")
                continue
        else:
            print("Pilihan tidak valid!")
            continue
        
        if not arr:
            print("Array kosong! Silakan pilih array lagi.")
            continue
        
        display_array(arr, "Array yang dipilih")
        
        while True:
            print("\n=== PILIHAN MENU ===")
            print("1. Menu Sorting")
            print("2. Menu Searching")
            print("3. Pilih Array Baru")
            print("4. Keluar")
            
            menu_choice = input("\nPilih menu (1-4): ")
            
            if menu_choice == "1":
                arr = sorting_menu_with_array(arr)
            elif menu_choice == "2":
                searching_menu_with_array(arr)
            elif menu_choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif menu_choice == "4":
                print("\nTerima kasih telah menggunakan program ini!")
                return
            else:
                print("Pilihan tidak valid! Silakan pilih menu 1-4.")

if __name__ == "__main__":
    main_menu() 