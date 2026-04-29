import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
from konfigurasi import *

with open(enkripsi_nama("demo.txt"), "r") as file_in:
    daftar_baris_out = []
    print("Mendekripsi file...")
    for baris in file_in:
        daftar_baris_out.append(f"{dekripsi_isi(baris.strip())}")
with open("demo_decrypted.txt", "w") as file_out:
    file_out.write('\n'.join(daftar_baris_out))
print(f"File berhasil didekripsi -> {file_out.name}")