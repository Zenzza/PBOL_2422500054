from typing import TypeVar
from dataclasses import dataclass

class Binatang:
    pass

@dataclass
class Kucing(Binatang):
    def __str__(self):
        return self.__class__.__name__

T = TypeVar("T", covariant=True)

class Kandang[T: Binatang]:
    def __init__(self, hewan: T):
        self.__hewan = hewan

    def dapatkan_hewan(self) -> T:
        return self.__hewan

U = TypeVar("U", covariant=True)

class PenjagaKandang[U: Binatang]:
    def urus_hewan(self, hewan: U):
        print(f"{hewan} harus diberi makan dan diajak berjalan setiap hari")

kandang_kucing = Kandang(Kucing())
kandang_binatang: Kandang[Binatang] = kandang_kucing
print(f"Saya mempunyai kandang untuk {kandang_binatang.dapatkan_hewan()}")

penjaga_kandang = PenjagaKandang[Binatang]()
penjaga_kandang.urus_hewan(Kucing())