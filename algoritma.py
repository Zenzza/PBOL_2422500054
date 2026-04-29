# Persiapan
from dataclasses import dataclass, astuple
from frozendict import frozendict
from frozenlist2 import frozenlist
from typing import Self, overload, Any
from math import ceil


@dataclass
class PesanAcak:
    pesan: str
    flag: str

    def __init__(self: Self, pesan: str, flag: str | None = None) -> None:
        self.pesan = pesan
        self.flag = flag if flag is not None else "X" * len(pesan)

    def __iter__(self: Self):
        return iter(astuple(self))


def buat_template(dari_string: str, case_sensitive: bool = False) -> frozendict[str, int]:
    # Buat string template tanpa karakter duplikat
    string_template = ""
    for karakter in dari_string:
        karakter_baca = karakter if case_sensitive else karakter.upper()
        if karakter_baca not in string_template:
            string_template += karakter_baca

    # Buat template
    no_karakter = 1
    template = {}
    for karakter in string_template:
        template[karakter] = no_karakter
        no_karakter += 1
    return frozendict(template)


# Tahap 0 (enkripsi)
def buat_kunci_privat(dari_kunci_publik: str,
                      template_publik: frozendict[str, int],
                      template_privat: frozendict[str, int],
                      case_sensitive: bool = False) -> str:
    # Periksa karakter kunci publik
    for karakter in dari_kunci_publik:
        karakter_baca = karakter if case_sensitive else karakter.upper()
        if karakter_baca not in template_publik:
            raise ValueError(f"Karakter kunci publik '{karakter_baca}' tidak terdapat di template publik")

    # Enkode kunci publik
    kode = 0
    pangkat = len(dari_kunci_publik) - 1
    for karakter in dari_kunci_publik:
        karakter_baca = karakter if case_sensitive else karakter.upper()
        kode += template_publik[karakter_baca] * len(template_publik) ** pangkat
        pangkat -= 1

    # Pengubahan basis kode kunci publik
    kode_basis = []
    quotient = kode
    if len(template_privat) != 1:
        while quotient != 0:
            remainder = quotient % len(template_privat)
            kode_basis.insert(0, remainder)
            quotient //= len(template_privat)
    else:
        kode_basis = [1] * kode

    # Penghapusan nol dari kode kunci publik berbasis
    if len(kode_basis) > 1:
        while 0 in kode_basis:
            for i in range(1, len(kode_basis)):
                if kode_basis[i] == 0 and kode_basis[i - 1] != 0:
                    kode_basis[i - 1] -= 1
                    kode_basis[i] = len(template_privat)
            while kode_basis[0] == 0:
                del kode_basis[0]

    # Dekode kode kunci publik berbasis
    kunci_privat = ""
    for digit in kode_basis:
        for karakter in template_privat.keys():
            if template_privat[karakter] == digit:
                kunci_privat += karakter
                break
    return kunci_privat


# Tahap 1 (enkripsi)
@overload
def pindai_kata(plain_text: str,
                template_publik: frozendict[str, int],
                case_sensitive: bool = False) -> frozenlist[str]:
    pass


# Tahap 1 (dekripsi)
@overload
def pindai_kata(cipher_text: PesanAcak) -> frozenlist[PesanAcak]:
    pass


# Tahap 1 (enkripsi/dekripsi)
def pindai_kata(*args: Any) -> frozenlist[str] | frozenlist[PesanAcak]:
    if len(args) == 3:  # Enkripsi
        # 0 = plain_text; 1 = template_publik; 2 = case_sensitive
        daftar_kata = []
        kata = ""
        for karakter in args[0]:
            karakter_baca = karakter if args[2] else karakter.upper()
            if karakter_baca in args[1]:
                kata += karakter
            else:
                if kata != "":
                    daftar_kata.append(kata)
                daftar_kata.append(karakter)
                kata = ""
        if kata != "":
            daftar_kata.append(kata)
        return frozenlist(daftar_kata)
    elif len(args) == 1:  # Dekripsi
        # 0 = cipher_text
        daftar_kata = []
        pesan, flag = args[0]
        kata = ""
        tanda = ""
        for i in range(len(pesan)):
            if flag[i] in "UL":
                kata += pesan[i]
                tanda += flag[i]
            else:
                if kata != "" and tanda != "":
                    daftar_kata.append(PesanAcak(kata, tanda))
                daftar_kata.append(PesanAcak(pesan[i]))
                kata = ""
                tanda = ""
        if kata != "" and tanda != "":
            daftar_kata.append(PesanAcak(kata, tanda))
        return frozenlist(daftar_kata)


# Tahap 2 (enkripsi)
@overload
def enkode(daftar_kata_plain_text: frozenlist[str],
           template_publik: frozendict[str, int],
           case_sensitive: bool = False) -> frozenlist[int]:
    pass


# Tahap 2 (dekripsi)
@overload
def enkode(daftar_kata_cipher_text: frozenlist[PesanAcak],
           template_privat: frozendict[str, int],
           kunci_privat: str,
           case_sensitive: bool = False) -> frozenlist[int]:
    pass


# Tahap 2 (enkripsi/dekripsi)
def enkode(*args: Any) -> frozenlist[int]:
    if len(args) == 3:  # Enkripsi
        # 0 = daftar_kata_plain_text; 1 = template_publik; 2 = case_sensitive
        daftar_kode = []
        for kata in args[0]:
            kode = 0
            karakter_pertama = kata[0] if args[2] else kata[0].upper()
            if karakter_pertama in args[1]:
                pangkat = len(kata) - 1
                for karakter in kata:
                    karakter_baca = karakter if args[2] else karakter.upper()
                    kode += args[1][karakter_baca] * len(args[1]) ** pangkat
                    pangkat -= 1
            daftar_kode.append(kode)
        return frozenlist(daftar_kode)
    elif len(args) == 4:  # Dekripsi
        # 0 = daftar_kata_cipher_text; 1 = template_privat; 2 = kunci_privat; 3 = case_sensitive
        daftar_kode = []
        for kata, flag in args[0]:
            kode = 0
            if flag != "X":
                kode_kunci_terbalik = \
                    tuple(reversed(tuple(map(lambda x: args[1][x if args[3] else x.upper()], args[2]))))
                kode_kata_terbalik = tuple(reversed(tuple(map(lambda x: args[1][x if args[3] else x.upper()], kata))))
                indeks = 0
                for _ in kata:
                    pengali = 1
                    for i in range(1, indeks + 1):
                        pengali *= kode_kunci_terbalik[(i - 1) % len(args[2])]
                    kode += kode_kata_terbalik[indeks % len(kata)] * pengali
                    indeks += 1
            daftar_kode.append(kode)
        return frozenlist(daftar_kode)


# Tahap 3 (enkripsi)
@overload
def ubah_basis(daftar_kode_kata_plain_text: frozenlist[int],
               kunci_privat: str,
               template_privat: frozendict[str, int],
               case_sensitive: bool = False) -> frozenlist[frozenlist[int]]:
    pass


# Tahap 3 (dekripsi)
@overload
def ubah_basis(daftar_kode_kata_cipher_text: frozenlist[int],
               template_publik: frozendict[str, int]) -> frozenlist[frozenlist[int]]:
    pass


# Tahap 3 (enkripsi/dekripsi)
def ubah_basis(*args: Any) -> frozenlist[frozenlist[int]]:
    if len(args) == 4:  # Enkripsi
        # 0 = daftar_kode_kata_plain_text; 1 = kunci_privat; 2 = template_privat; 3 = case_sensitive
        daftar_kode_basis = []
        kode_kunci_terbalik = tuple(reversed(tuple(map(lambda x: args[2][x if args[3] else x.upper()], args[1]))))
        if kode_kunci_terbalik != tuple([1] * len(kode_kunci_terbalik)):
            for kode in args[0]:
                kode_basis = []
                quotient = kode
                indeks = 0
                while True:
                    remainder = quotient % kode_kunci_terbalik[indeks % len(args[1])]
                    kode_basis.insert(0, remainder)
                    quotient //= kode_kunci_terbalik[indeks % len(args[1])]
                    indeks += 1
                    if quotient == 0:
                        break
                daftar_kode_basis.append(frozenlist(kode_basis))
        else:
            for kode in args[0]:
                daftar_kode_basis.append(frozenlist([1] * kode))
        return frozenlist(daftar_kode_basis)
    elif len(args) == 2:  # Dekripsi
        # 0 = daftar_kode_kata_cipher_text; 1 = template_publik
        daftar_kode_basis = []
        if len(args[1]) > 1:
            for kode in args[0]:
                kode_basis = []
                quotient = kode
                while True:
                    remainder = quotient % len(args[1])
                    kode_basis.insert(0, remainder)
                    quotient //= len(args[1])
                    if quotient == 0:
                        break
                daftar_kode_basis.append(frozenlist(kode_basis))
        else:
            for kode in args[0]:
                daftar_kode_basis.append(frozenlist([1] * kode))
        return frozenlist(daftar_kode_basis)


# Tahap 4 (enkripsi)
@overload
def hapus_nol(daftar_kode_basis_plain_text_dengan_nol: frozenlist[frozenlist[int]],
              template_privat: frozendict[str, int],
              kunci_privat: str,
              case_sensitive: bool = False) -> frozenlist[frozenlist[int]]:
    pass


# Tahap 4 (dekripsi)
@overload
def hapus_nol(daftar_kode_basis_cipher_text_dengan_nol: frozenlist[frozenlist[int]],
              template_publik: frozendict[str, int]) -> frozenlist[frozenlist[int]]:
    pass


# Tahap 4 (enkripsi/dekripsi)
def hapus_nol(*args: Any) -> frozenlist[frozenlist[int]]:
    if len(args) == 4:  # Enkripsi
        # 0 = daftar_kode_basis_plain_text_dengan nol; 1 = template_privat; 2 = kunci_privat; 3 = case_sensitive
        daftar_kode_basis = list(args[0])
        kode_kunci_terbalik = tuple(reversed(tuple(map(lambda x: args[1][x if args[3] else x.upper()], args[2]))))
        for i in range(len(args[0])):
            if len(args[0][i]) != 1:
                kode_basis = list(args[0][i])
                topeng_basis = []
                for j in range(len(args[0][i])):
                    topeng_basis.insert(0, kode_kunci_terbalik[j % len(args[2])])
                if len(kode_basis) > 1:
                    while 0 in kode_basis:
                        for j in range(1, len(kode_basis)):
                            if kode_basis[j] == 0 and kode_basis[j - 1] != 0:
                                kode_basis[j - 1] -= 1
                                kode_basis[j] = topeng_basis[j]
                        while kode_basis[0] == 0:
                            del kode_basis[0]
                daftar_kode_basis[i] = frozenlist(kode_basis)
            else:
                daftar_kode_basis[i] = args[0][i]
        return frozenlist(daftar_kode_basis)
    elif len(args) == 2:  # Dekripsi
        # 0 = daftar_kode_basis_cipher_text_dengan_nol; 1 = template_publik
        daftar_kode_basis = list(args[0])
        for i in range(len(args[0])):
            if len(args[0][i]) != 1:
                kode_basis = args[0][i]
                if len(kode_basis) > 1:
                    while 0 in kode_basis:
                        for j in range(1, len(kode_basis)):
                            if kode_basis[j] == 0 and kode_basis[j - 1] != 0:
                                kode_basis[j - 1] -= 1
                                kode_basis[j] = len(args[1])
                        while kode_basis[0] == 0:
                            del kode_basis[0]
                daftar_kode_basis[i] = frozenlist(kode_basis)
            else:
                daftar_kode_basis[i] = args[0][i]
        return frozenlist(daftar_kode_basis)


# Tahap 5 (enkripsi/dekripsi)
def dekode[T](daftar_kode_basis_asal_tanpa_nol: frozenlist[frozenlist[int]],
              template_tujuan: frozendict[str, int],
              daftar_kata_asal: frozenlist[T]) -> frozenlist[frozenlist[str]]:
    daftar_karakter = []
    for i in range(len(daftar_kode_basis_asal_tanpa_nol)):
        kode = daftar_kode_basis_asal_tanpa_nol[i]
        match (origin_word := daftar_kata_asal[i]):
            case x if type(x) is str:
                kata_asal = origin_word
            case x if type(x) is PesanAcak:
                kata_asal = origin_word.pesan
            case _:
                raise ValueError("Tipe elemen pada daftar kata tidak valid")
        karakter = []
        if kode != frozenlist([0]):
            for digit in kode:
                for kar, kd in template_tujuan.items():
                    if kd == digit:
                        karakter.append(kar)
                        break
        else:
            karakter.append(kata_asal[0])
        daftar_karakter.append(frozenlist(karakter))
    return frozenlist(daftar_karakter)


# Tahap 6 (enkripsi)
@overload
def ubah_kapitalisasi(daftar_karakter_cipher_text: frozenlist[frozenlist[str]],
                      daftar_kata_plain_text: frozenlist[str],
                      template_publik: frozendict[str, int],
                      case_sensitive: bool = False) -> PesanAcak:
    pass


# Tahap 6 (dekripsi)
@overload
def ubah_kapitalisasi(daftar_karakter_plain_text: frozenlist[frozenlist[str]],
                      daftar_kata_cipher_text: frozenlist[PesanAcak]) -> str:
    pass


# Tahap 6 (enkripsi/dekripsi)
def ubah_kapitalisasi(*args: Any) -> PesanAcak | str:
    if len(args) == 4:  # Enkripsi
        # 0 = daftar_karakter_cipher_text; 1 = daftar_kata_plain_text; 2 = template_publik; 3 = case_sensitive
        cipher = ""
        flag_cipher = ""
        for kata in args[1]:
            flag_plain = ""
            karakter_cek = kata[0] if args[3] else kata[0].upper()
            if karakter_cek in args[2]:
                for karakter in kata:
                    flag_plain += 'U' if karakter.isupper() or args[3] else 'L'
            else:
                flag_plain += 'X'
            if flag_plain != "X":
                daftar_karakter_cipher = args[0][args[1].index(kata)]
                if len(flag_plain) != 1:
                    lp = len(kata)
                    lc = len(daftar_karakter_cipher)
                    isp = 1
                    for i in range(1, len(flag_plain)):
                        if flag_plain[i] != flag_plain[i - 1] or i == len(flag_plain) - 1:
                            ifp = i if i != len(flag_plain) - 1 else len(flag_plain)
                            isc = (isp - 1) * lc // lp + 1
                            ifc = ifp * lc // lp
                            flag = flag_plain[i - 1] * (ifc - isc + 1)
                            flag_cipher += flag
                            for j in range(isc - 1, ifc):
                                cipher += args[0][args[1].index(kata)][j] if flag_plain[i - 1] == 'U' else \
                                    args[0][args[1].index(kata)][j].lower()
                            isp = ifp + 1
                else:
                    flag = flag_plain[0] * len(args[0][args[1].index(kata)])
                    flag_cipher += flag
                    for i in range(len(args[0][args[1].index(kata)])):
                        cipher += args[0][args[1].index(kata)][i] if flag_plain[0] == 'U' else \
                            args[0][args[1].index(kata)][i].lower()
            else:
                cipher += kata
                flag_cipher += flag_plain
        return PesanAcak(cipher, flag_cipher)
    elif len(args) == 2:  # Dekripsi
        # 0 = daftar_karakter_plain_text; 1 = daftar_kata_cipher_text
        plain = ""
        for kata in args[1]:
            if kata.flag != "X":
                daftar_karakter_plain = args[0][args[1].index(kata)]
                if len(kata.flag) != 1:
                    lc = len(kata.pesan)
                    lp = len(daftar_karakter_plain)
                    isc = 1
                    for i in range(1, len(kata.flag)):
                        if kata.flag[i] != kata.flag[i - 1] or i == len(kata.flag) - 1:
                            ifc = i if i != len(kata.flag) - 1 else len(kata.flag)
                            isp = ceil((isc - 1) * lp / lc) + 1
                            ifp = ceil(ifc * lp / lc)
                            for j in range(isp - 1, ifp):
                                plain += args[0][args[1].index(kata)][j] if kata.flag[i - 1] == 'U' else \
                                    args[0][args[1].index(kata)][j].lower()
                            isc = ifc + 1
                else:
                    for i in range(len(args[0][args[1].index(kata)])):
                        plain += args[0][args[1].index(kata)][i] if kata.flag[0] == 'U' else \
                            args[0][args[1].index(kata)][i].lower()
            else:
                plain += kata.pesan
        return plain
