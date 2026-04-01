from abc import ABC, abstractmethod
from forbiddenfruit import curse

class Mobil(ABC):
    @abstractmethod
    def setir(self):
        pass

class MobilDasar(Mobil):
    def setir(self):
        print("Berangkat dari Pangkalpinang ke Sungailiat")

def dekorasi(_, inisialisasi):
    def setir_mobil(self):
        inisialisasi()
        MobilDasar.setir(self)
    return type("",(Mobil,),{"setir": setir_mobil})()

curse (Mobil, "dekorasi", dekorasi)
mobil_saya = MobilDasar()
mobil_offroad = mobil_saya.dekorasi(lambda: print("Mengkonfirmasi mode setir offroad"))
mobil_offroad.setir()

