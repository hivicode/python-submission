class Pegawai:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Pegawai.empCount += 1

    def displayCount(self):
        print("Total Pegaway %d" % Pegawai.empCount)

    def displayEmployee(self):
        print("Nama : ", self.name, ", Pendapatan: ", self.salary)
        
