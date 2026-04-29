from konfigurasi import *

with open("demo.txt", "r") as file_in:
    daftar_baris_out = []
    print("Mengenkripsi file...")
    for baris in file_in:
        daftar_baris_out.append(f"{enkripsi_isi(baris.strip())}")
with open(enkripsi_nama("demo.txt"), "w") as file_out:
    file_out.write('\n'.join(daftar_baris_out))
print(f"File berhasil dienkripsi -> {file_out.name}")