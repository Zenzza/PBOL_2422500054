from abc import ABC, abstractmethod

class StrategiPembayaran(ABC):
    @abstractmethod
    def bayar(self, nominal):
        pass

class StrategiPembayaranKartuKredit(StrategiPembayaran):
    def __init__(self, no_kartu):
        self.__no_kartu = no_kartu

    def bayar(self, nominal):
        print(f"{nominal} dibayar menggunakan kartu kredit [{self.__no_kartu}]")

class StrategiPembayaranDompetDigital(StrategiPembayaran):
    def __init__(self,email):
        self.__email = email

    def bayar(self, nominal):
        print(f"{nominal} dibayar menggunakan dompet digital dengan e-mail {self.__email}")

class KeranjangBelanja:
    def __init__(self, strategi):
        self.__strategi = strategi

    def checkout(self,nominal):
        self.__strategi.bayar(nominal)

strategi_kartu_kredit = StrategiPembayaranKartuKredit("1234-5678-9012-3456")
strategi_dompet_digital = StrategiPembayaranDompetDigital("python@pbo.com")
keranjang_kuning = KeranjangBelanja(strategi_kartu_kredit)
keranjang_hijau = KeranjangBelanja(strategi_dompet_digital)
keranjang_kuning.checkout(100_000)
keranjang_hijau.checkout(50.000)
