from menustack import menu1
from menuqueue import menu2
from os import system
clear = system("cls")
clear

def main():
    while True:
        print("\n| Menu Aplikasi |")
        print("1. Stack")
        print("2. Queue")
        print("3. Exit dari Program")
        print("=" * 20)

        pilihan = input("Masukkan pilihan: ")
        print("\n")
        if pilihan == "1":
            menu1()
        elif pilihan == "2":
            menu2()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.\n")
            
if __name__ == "__main__":
    main()