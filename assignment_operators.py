from os import system
system("cls")
import time
def main():
    print()
    while True: # for repeat until the input is integer//untuk mengulang input jika bukan integer/valueerror
        try:
            num = int(input("input first number: "))
            same = int(input("input second number: "))
        except ValueError:
            print("Please input number only, try again!")
            time.sleep(3)
            system("cls")
        else:
            break
    system("cls")
    print("First Number:", num, "\nSecond Number:", same)
    print()
    num += same
    print("add", same, "=", num) # tambah
    num -= same
    print("sub", same, "=", num) # kurang
    num *= same
    print("multi", same, "=", num) # kali
    num /= same
    print("div", same, "=", int(num)) # bagi
    num //= same
    print("floor div", same, "=", int(num)) # pembagian bulat bawah
    num %= same
    print("modulus", same, "=", int(num)) # sisa hasil bagi
    num **= same
    print("exponent", same, "=", int(num)) # pangkat
while True:
    time.sleep(1) # pause for 1 second to repeat the program//jeda 1 detik untuk mengulang program
    main()