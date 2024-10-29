# Python Submission 
<p style="text-align: left;"><span style="font-size: 10pt;"><span style="font-size: 8pt;">udah gw update!</span></span></p>
<p style="text-align: left;"><img src="https://media.tenor.com/NeubPwLVK94AAAAM/ace-attorney-phoenix-wright.gif" border="0" alt="ace-attorney-phoenix-wright.gif" width="135" height="93"></p>
<p style="text-align: left;"><span style="font-size: 8pt;">update readme doang 😝</span></p>
<p style="text-align: left;"><span style="font-size: 8pt;"><img src="https://media.tenor.com/twOolAiM02kAAAAM/edge-worth-ace-attorney.gif" border="0" alt="edge-worth-ace-attorney.gif" width="135" height="105"></span></p>

List
=================

* [Reference](#reference)
* [1. Input & Output](#1-input-output)
* [2. Data Types](#2-data-types)
* [3. Data Types Conversion](#3-data-types-conversion)
* [4. Arithmetic Operators](#4-arithmetic-operators)
* [5. Assignment Operators](#5-assignment-operators)
* [6. Find Total & Change](#6-find-total-and-change)
* [7. Math Module](#7-math-module)
* [8. Pythagoras](#8-pythagoras)
  
---
## Reference
<a href = "https://www.w3schools.com/python" target= "_blank"> W3Schools </a>

<a href = "https://python-forum.io/" target= "_blank"> python-forum.io </a>

---
## 1. Input Output
enter an input to be printed as output.
<details>
<summary>Example</summary>
  
Code
```
from os import system
nama = input("Nama anda: ")
pt = input("Nama Perguruan Tinggi: ")
tahun_masuk = int(input("Tahun Masuk: "))
nim = int(input("NIM: "))
prodi = input("Program Studi: ")
system ("cls")
print ("Halo, nama saya", nama+".", "\nSaya adalah mahasiswa", pt, "Angkatan", tahun_masuk, "\nDengan NIM", nim, "\nSaya mengambil Program Studi", prodi+".")
```
Input
```
Nama anda: Bintang 
Nama Perguruan Tinggi: Stikom
Tahun Masuk: 2000
NIM: 1234567890
Program Studi: Informatika
```
Output after system ("cls") func
```
Halo, nama saya Bintang.
Saya adalah mahasiswa Stikom Angkatan 2000
Dengan NIM 1234567890
Saya mengambil Program Studi Informatika.
```
</details>

---
## 2. Data Types
just, how to know which type is the data.
<details>
<summary>Example</summary>
  
Code
```
var_1 = True
var_2 = "hello sekai"
var_3 = 66
var_4 = 6.66
var_5 = complex(1j)
var_6 = list(("kucing", "landak", "tupai"))
var_7 = tuple(("kucing", "landak", "tupai"))
var_8 = range(6)
var_9 = dict(nama="Jane", umur=37)
var_10 = set(("kucing", "landak", "tupai"))
var_11 = frozenset(("kucing", "landak", "tupai"))
var_12 = bytes(5)
var_13 = bytearray(5)
var_14 = memoryview(bytes(5))

print(("tipedata: "), type(var_), type(var_)) # type: choose var or ignore
```
Choosing var, example: var_2 and var_3, print
```
print(("tipedata: "), type(var_2), type(var_3))
```
Output
```
tipedata:  <class 'str'> <class 'int'>
```
</details>

---
## 3. Data Types Conversion
convert data to other type.
<details>
<summary>Example</summary>
  
Code
```
harga = input("Harga Barang: ")
int_harga = int(harga) #adding *integer* to convert
float_harga = float(harga) #addding *float* to convert
```
Input & Print
```
print (harga, type(harga))
print (int_harga, type(int_harga))
print (float_harga, type(float_harga))
```
Output
```
Harga Barang: 5000
5000 <class 'str'>
5000 <class 'int'>
5000.0 <class 'float'>
```
</details>

---
## 4. Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations.
<details>
<summary>Example</summary>
  
Code
```
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
```
Input & Print
```
input first number: 2
input second number: 3
```
Output
```
2 + 3 = 5
2 - 3 = -1
2 * 3 = 6
2 / 3 = 0.6666666666666666
2 % 3 = 2
2 ** 3 = 8
2 // 3 = 0
Repeat? (Y/N)
```
</details>

---
## 5. Assignment Operators
Assignment operators are used to assign values to variables.
<details>
<summary>Example</summary>
  
Code
```
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
```
Input & Print
```
input first number: 20
input second number: 4

```
Output
```
First Number: 20
Second Number: 4

add 4 = 24
sub 4 = 20
multi 4 = 80
div 4 = 20
floor div 4 = 5
modulus 4 = 1
exponent 4 = 1
```
</details>

---
## 6. Find Total and Change
Another simple program, using arithmetic operators.
<details>
<summary>Example</summary>
  
Code
```
harga = int(input("Harga Barang: ")) 
jumlah = int(input("Jumlah Barang: ")) 
total = harga*jumlah
print("Total Harga: ", total)
bayar = int(input("Jumlah Pembayaran: "))
kembalian = bayar-total
print("Kembalian: ", kembalian)
```
Input, Print, Output
```
Harga Barang: 5000
Jumlah Barang: 2
Total Harga:  10000
Jumlah Pembayaran: 24500
Kembalian:  14500
```
</details>

---
## 7. Math Module
math module is math module.
<details>
<summary>Example</summary>
  
Code
```
import math
a = float(input("input float number: "))
print(math.ceil(a)) # literal ceil, you put 5.3 it'll print 6 at end.
print(math.floor(a)) # literal floor, you put 5.3 it'll print 5 at end. 
```
Input, Print, Output
```
input float number: 5.4
6 #ceil
5 #floor
```
</details>

---
## 8. Pythagoras
find value of c from square root of two powered value after adding them.
<details>
<summary>Example</summary>
  
Code
```
from math import pow, sqrt
a = int(input("angka pertama: "))
b = int(input("angka kedua: "))
print()

a2= int(pow(a, 2))
b2= int(pow(b, 2))
print(f"{a}\u00b2 =", a2)
print(f"{b}\u00b2 =", b2)
print()

c2 = a2 + b2
print(f"\u221A{a}\u00b2+{b}\u00b2 = \u221A{a2}+{b2} =", sqrt(c2))
```
Input, Print, Output
```
angka pertama: 2
angka kedua: 3

2² = 4
3² = 9

√2²+3² = √4+9 = 3.605551275463989
```
</details>
