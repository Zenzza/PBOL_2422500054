from os.path import exists

nama_file = "demo.txt"
if not exists(nama_file):
    open(nama_file,"x")
    print(f"File \"{nama_file}\" berhasil dibuat")
else:
    print(f"File \"{nama_file}\" gagal dibuat - file sudah ada")
