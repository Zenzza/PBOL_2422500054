from abc import ABC, abstractmethod

class Pengamat(ABC):
    @abstractmethod
    def perbarui(self,cuaca):
        pass

class Subjek(ABC):
    @abstractmethod
    def tambah_pengamat(self, pengamat):
        pass

    @abstractmethod
    def hapus_pengamat(self, pengamat):
        pass

    @abstractmethod
    def beritahu_pengamat(self):
        pass

class StasiunCuaca(Subjek):
    __daftar_pengamat = []
    __cuaca : str

    @property
    def cuaca(self):
        return

    @cuaca.setter
    def cuaca(self, value):
        self.__cuaca = value
        self.beritahu_pengamat()

    def tambah_pengamat(self, pengamat):
        self.__daftar_pengamat.append(pengamat)

    def hapus_pengamat(self, pengamat):
        self.__daftar_pengamat.remove(pengamat)

    def beritahu_pengamat(self):
        for pengamaat in self.__daftar_pengamat:
            pengamaat.perbarui(self.__cuaca)

class TampilanTelepon(Pengamat):
    __cuaca : str

    def perbarui(self,cuaca):
        self.__cuaca = cuaca
        self.tampil()

    def tampil(self):
        print(f"Tampilan Telepon: Cuaca diperbarui - {self.__cuaca}")

class TampilanTV(Pengamat):
    __cuaca : str

    def perbarui(self,cuaca):
        self.__cuaca = cuaca
        self.tampil()

    def tampil(self):
        print(f"Tampilan TV : Cuaca diperbarui - {self.__cuaca}")

bmkg = StasiunCuaca()
telepon = TampilanTelepon()
tv = TampilanTV()

bmkg.tambah_pengamat(telepon)
bmkg.tambah_pengamat(tv)
bmkg.cuaca = "Cerah Berawan"
        