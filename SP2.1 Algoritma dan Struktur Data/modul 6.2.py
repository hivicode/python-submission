from collections import deque

setak = deque()
setak.append("a") 
setak.append("b") 
setak.append("c") 
print("Data pada stack: ") 
print(setak)

print("\n Elemen yang dikeluarkan dari stack: ") 
print(setak.pop()) 
print(setak.pop()) 
print(setak.pop())

print("\nStack setelah elemen dikeluarkan: ") 
print(setak)