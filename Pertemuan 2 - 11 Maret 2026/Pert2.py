from abc import  ABC, abstractmethod

class Produk(ABC):
    @abstractmethod
    def buat(self):
        pass

class ProdukA(Produk):
    def buat(self):
        return "Kacang Garuda"

class ProdukB(Produk):
    def buat(self):
        return "Kacang Dua Kelinci"

class PabrikProduk(ABC):
    @abstractmethod
    def buat_produk(self):
        pass

class PabrikA(PabrikProduk):
    def buat_produk(self):
        return ProdukA()

class PabrikB(PabrikProduk):
    def buat_produk(self):
        return ProdukB()

garudafood: PabrikProduk = PabrikA()
kacang_garuda = garudafood.buat_produk()
print(kacang_garuda.buat())

pt_dua_kelinci: PabrikProduk = PabrikB()
kacang_dua_kelinci = pt_dua_kelinci.buat_produk()
print(kacang_dua_kelinci.buat())

