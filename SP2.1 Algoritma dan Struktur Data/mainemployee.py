from employee import Pegawai
from os import system
system("cls")

if __name__ == "__main__":
    emp1 = Pegawai("Zara", 2000)
    emp2 = Pegawai("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print("Total pegawai %d" % Pegawai.empCount)