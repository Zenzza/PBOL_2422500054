from algoritma import *

template_isi = buat_template(
    "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ ~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVVVBNM<>?", True
)

template_nama = buat_template(
    "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKLZXCVVVBNM<>?", True
)

kunci = "AtmaLuhur"
case_sensitive = True

def enkripsi_isi(isi):
    daftar_kata = pindai_kata(isi, template_isi, case_sensitive)
    kode_kata = enkode(daftar_kata, template_isi, case_sensitive)
    kode_kata_basis = ubah_basis(kode_kata, kunci, template_isi, case_sensitive)
    kode_kata_basis = hapus_nol(kode_kata_basis,template_isi, kunci, case_sensitive)
    daftar_kata_acak = dekode(kode_kata_basis,template_isi, daftar_kata)
    return ubah_kapitalisasi(daftar_kata_acak,daftar_kata, template_isi, case_sensitive).pesan

def enkripsi_nama(nama):
    daftar_kata = pindai_kata(nama, template_nama, case_sensitive)
    kode_kata = enkode(daftar_kata, template_nama, case_sensitive)
    kode_kata_basis = ubah_basis(kode_kata, kunci, template_nama, case_sensitive)
    kode_kata_basis = hapus_nol(kode_kata_basis,template_nama, kunci, case_sensitive)
    daftar_kata_acak = dekode(kode_kata_basis,template_nama, daftar_kata)
    return ubah_kapitalisasi(daftar_kata_acak,daftar_kata, template_nama, case_sensitive).pesan

def dekripsi_isi(isi):
    flag = ''
    for karakter in isi:
        karakter_baca = karakter if case_sensitive else karakter.upper()
        flag += 'U' if karakter_baca in template_isi else 'X'
    daftar_kata_acak = pindai_kata(PesanAcak(isi, flag))
    kode_kata_acak = enkode(daftar_kata_acak, template_isi, kunci, case_sensitive)
    kode_kata_basis = ubah_basis(kode_kata_acak, template_isi)
    kode_kata_basis = hapus_nol(kode_kata_basis, template_isi)
    daftar_kata = dekode(kode_kata_basis, template_isi, daftar_kata_acak)
    return ubah_kapitalisasi(daftar_kata, daftar_kata_acak)
