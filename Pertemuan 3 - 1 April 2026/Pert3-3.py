class Prossesor:
    def proses_data(self):
        print("Memproses Data...")

class Memori:
    def muat(self):
        print("Memuat data dari memori...")

class HardDrive:
    def baca_data(self):
        print("Membaca data dari hard drive...")

class FasadKomputer:
    def __init__(self, cpu, ram, hdd):
        self.__cpu = cpu
        self.__ram = ram
        self.__hdd = hdd

    def mulai(self):
        print("Fasad Komputer Dimulai")
        self.__cpu.proses_data()
        self.__ram.muat()
        self.__hdd.baca_data()
        print("Fasad Komputer Berhasil Dimulai")

cpu_ = Prossesor()
ram_ = Memori()
hdd_ = HardDrive()
fasad = FasadKomputer(cpu_,ram_,hdd_)
fasad.mulai()