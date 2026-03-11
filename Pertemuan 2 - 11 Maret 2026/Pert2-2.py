from abc import ABC, abstractmethod

class ProdukC(ABC):
    @abstractmethod
    def operasi_c(self):
        pass

class ProdukC1(ProdukC):
    def operasi_c(self):
        return "Indomie Soto Ayam"

class ProdukC2(ProdukC):
    def operasi_c(self):
        return "Mie Sedap Ayam Bawang"

class ProdukD(ABC):
    @abstractmethod
    def operasi_d(self):
        pass

class ProdukD1(ProdukD):
    def operasi_d(self):
        return "Indomie Goreng"

class ProdukD2(ProdukD):
    def operasi_d(self):
        return "Mie Sedap Korean Spicy Chicken"

class Pabrik(ABC):
    @abstractmethod
    def buat_produk_c(self):
        pass

    @abstractmethod
    def buat_produk_d(self):
        pass

class Pabrik1(Pabrik):
    def buat_produk_c(self):
        return ProdukC1()

    def buat_produk_d(self):
        return ProdukD1()


class Pabrik2(Pabrik):
    def buat_produk_c(self):
        return ProdukC2()

    def buat_produk_d(self):
        return ProdukD2()

indofood: Pabrik = Pabrik1()
indomie_kuah = indofood.buat_produk_c()
indomie_goreng = indofood.buat_produk_d()
print(indomie_kuah.operasi_c())
print(indomie_goreng.operasi_d())

wings_food : Pabrik = Pabrik2()
mie_sedaap_kuah = wings_food.buat_produk_c()
mie_sedaap_goreng = wings_food.buat_produk_d()
print(mie_sedaap_kuah.operasi_c())
print(mie_sedaap_goreng.operasi_d())