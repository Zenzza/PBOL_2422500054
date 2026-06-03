class Pengguna:
    __old_value:str
    __new_value = "<Tak Ada Nama>"

    @property
    def nama(self):
        return

    @nama.setter
    def nama(self, value):
        self.__old_value = self.__new_value
        self.__new_value = value
        print(f"{self.__old_value} -> {self.__new_value}")

user = Pengguna()
nama_saya = ("Eza", "Budi", "Perkasa")
for kata in nama_saya:
    user.nama = kata