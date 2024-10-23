from os import system
def operasi():
    #declaration
    num1 = 0
    num2 = 0
    add = 0
    sub = 0
    multi = 0
    div = 0.0
    mod = 0
    exponent = 0
    floordiv = 0
    #input2
    num1 = int(input("input first number: "))
    num2 = int(input("input second number: "))
    #process
    add = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    mod = num1 % num2
    exponent = num1 ** num2
    floordiv = num1 // num2
    #output
    print()
    print(num1, "+", num2, "=", add)
    print(num1, "-", num2, "=", sub)
    print(num1, "*", num2, "=", multi)
    print(num1, "/", num2, "=", div)
    print(num1, "%", num2, "=", mod)
    print(num1, "**", num2, "=", exponent)
    print(num1, "//", num2, "=", floordiv)
while True: # condition
    system("cls")
    operasi()
    if input("Repeat? (Y/N)").strip().upper() != 'Y':
        system("cls")
        break
# strip() untuk menghapus spasi pada input
# upper() untuk mengubah input lowercase menjadi uppercase
# != if not
# Bintang Fathir_1124102166