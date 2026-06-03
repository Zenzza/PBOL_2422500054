from collections import namedtuple

Pengguna = namedtuple("Pengguna", ["nama", "usia"])
user = Pengguna("Eza Pastro", 32)
print(user.nama)
print(user.usia)