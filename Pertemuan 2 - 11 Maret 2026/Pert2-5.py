from dataclasses import dataclass

@dataclass
class Komputer:
    processor : str
    ram : str
    penyimpanan : str
    kartu_grafis : str

class PembangunKomputer:
    __processor : str
    __ram : str
    __penyimpanan : str
    __kartu_grafis : str

    def processor(self,detail):
        self.__processor = detail
        return self

    def ram(self,detail):
        self.__ram = detail
        return self

    def penyimpanan(self,detail):
        self.__penyimpanan = detail
        return self

    def kartu_grafis(self, detail):
        self.__kartu_grafis = detail
        return self

    def bangun(self):
        return Komputer(self.__processor, self.__ram, self.__penyimpanan, self.__kartu_grafis)

pembangun = PembangunKomputer()
komputer_gaming = pembangun \
    .processor("Intel Core i9") \
    .ram("32 GB DDR4") \
    .penyimpanan("1 TB SSD") \
    .kartu_grafis("NVIDIA RTX 3080") \
    .bangun()
print("Spesifikasi Komputer Gaming Saya:")
print(f"""Processor : {komputer_gaming.processor}
RAM: {komputer_gaming.ram}
Penyimpanan : {komputer_gaming.penyimpanan}
Kartu Grafis : {komputer_gaming.kartu_grafis}""")