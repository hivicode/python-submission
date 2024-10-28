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