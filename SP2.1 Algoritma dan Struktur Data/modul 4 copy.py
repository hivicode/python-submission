class Stack: #menetapkan class dengan nama Stack
    def __init__(self): 
        self.items = [] 
    
    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0 

    def Peek(self):
        return self.items[-1]
    
    def Size(self):
        return len(self.items)
    
def MainMenu():
    s = Stack()
    while True:
        print("| Menu Aplikasi Stack |")
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Object Terakhir")
        print("5. Panjang Dari Stack")
        print("="*20)

        pilihan = str(input("Masukkan pilihan: "))
        if pilihan == "1":
            print("Hello")
            obj = str(input("Object yang ingin ditambahkan: "))
            s.Push(obj)
            print("Object " + obj + " telah ditambahkan")
        elif pilihan == "2":
            print("Object " + s.Pop() + " telah dihapus")
        elif pilihan == "3":
            print(s.isEmpty())
        elif pilihan == "4":
            print("Object terakhir: " + s.Peek())
        elif pilihan == "5":
            print("Panjang dari Stack adalah "+ str(s.Size()))
        else:
           print("Pilihan tidak valid")

MainMenu()