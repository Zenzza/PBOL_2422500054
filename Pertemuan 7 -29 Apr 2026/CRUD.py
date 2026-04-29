from os.path import exists


class Medali:
    __nama_file = "medali.dat"

    kd_kontingen: str
    nm_kontingen: str
    emas: int
    perak: int
    perunggu: int

    def __init__(self):
        if not exists(self.__nama_file):
            open(self.__nama_file, "x")

    def simpan(self):
        with open(self.__nama_file, "a") as file:
            if ',' not in self.kd_kontingen and ',' not in self.nm_kontingen:
                file.write(f"{self.kd_kontingen},{self.nm_kontingen},{self.emas},{self.perak},{self.perunggu}\n")
            else:
                raise ValueError("Nilai field tidak boleh mengandung koma")

    def ubah(self, var_kode):
        with open(self.__nama_file, "r") as file:
            isi = file.read().strip().split('\n')
            for baris in isi:
                record = baris.split(',')
                if record[0] == var_kode:
                    indeks_ubah = isi.index(baris)
                    if ',' not in self.nm_kontingen:
                        isi[indeks_ubah] = f"{var_kode},{self.nm_kontingen},{self.emas},{self.perak},{self.perunggu}"
                    else:
                        raise ValueError("Nilai field tidak boleh mengandung koma")
        with open(self.__nama_file, "w") as file:
            file.write(f"{'\n'.join(isi)}\n")

    def hapus(self, var_kode):
        with open(self.__nama_file, "r") as file:
            isi = file.read().strip().split('\n')
            for baris in isi:
                record = baris.split(',')
                if record[0] == var_kode:
                    indeks_hapus = isi.index(baris)
                    isi[indeks_hapus] = ""
            isi = [x for x in isi if len(x) != 0]
        with open(self.__nama_file, "w") as file:
            file.write(f"{'\n'.join(isi)}\n")

    def tampil(self):
        with open(self.__nama_file, "r") as file:
            isi = file.read().strip().split('\n')
        print(f"{'Kode  '} {'Nama Kontingen         '} {'Emas '} {'Perak '} {'Perunggu  '}")
        print("-" * 50)
        for baris in isi:
            if baris:
                record = baris.split(',')
                print(f"{record[0]:<6} {record[1]:<20} {record[2]:>5} {record[3]:>6} {record[4]:>8}")

data_medali = Medali()
data_medali.tampil()