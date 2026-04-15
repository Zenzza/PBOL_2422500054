from abc import ABC, abstractmethod
from frozenlist2 import frozenlist
from frozendict import frozendict


class Kalender(ABC):
    def __init__(self, tahun, bulan, hari):
        self.tahun = tahun
        self.bulan = bulan
        self.hari = hari

    @property
    @abstractmethod
    def nm_bulan(self):
        pass


class KalenderMasehi(Kalender):
    def __init__(self, tahun, bulan, hari):
        super().__init__(tahun, bulan, hari)

    @property
    def nm_bulan(self):
        return frozenlist(["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September",
                           "Oktober", "November", "Desember"])


def baca_tanggal[T: (KalenderMasehi, KalenderMasehi)](tanggal: T):
    return f"{tanggal.hari} {tanggal.nm_bulan[tanggal.bulan - 1]} {tanggal.tahun}"


tanggal_masuk_asean = frozendict({
    "Thailand": KalenderMasehi(1967, 8, 8),
    "Indonesia": KalenderMasehi(1967, 8, 8),
    "Malaysia": KalenderMasehi(1967, 8, 8),
    "Singapura": KalenderMasehi(1967, 8, 8),
    "Filipina": KalenderMasehi(1967, 8, 8),
    "Brunei": KalenderMasehi(1984, 1, 7),
    "Vietnam": KalenderMasehi(1995, 7, 28),
    "Laos": KalenderMasehi(1997, 7, 23),
    "Myanmar": KalenderMasehi(1997, 7, 23),
    "Kamboja": KalenderMasehi(1999, 4, 30),
    "Timor Leste": KalenderMasehi(2022, 11, 11)
})

print("Tanggal Masuk ASEAN setiap Negara Anggota:")
for negara, tanggal in tanggal_masuk_asean.items():
    print(f"{negara} -> {baca_tanggal(tanggal)}")
