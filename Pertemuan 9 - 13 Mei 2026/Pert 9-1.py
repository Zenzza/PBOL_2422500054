from dataclasses import dataclass

#Tugas: Menampung Data User
@dataclass
class User:
    username: str
    password: str

#Tugas : Mengotentikasi user yang mencoba login ke sistem
class Otentikasi:
    def sign_in(self, data_login):
        username_terdaftar = "Jordi"
        password_terdaftar = "2422500054"
        return data_login == User(username_terdaftar,password_terdaftar)

    def sign_out(self, data_login):
        print(f"Anda telah logout dari sesi {data_login.username}")
        exit()

otentik = Otentikasi()
while True:
    un = input("Username: ")
    pw = input("Password: ")
    user_login = User(un,pw)
    if otentik.sign_in(user_login):
        is_logged_out = input("Login berhasil! Tekan 'X' untuk logout ") in "Xx"
        while not is_logged_out:
            is_logged_out = input("Anda masih berada dalam sistem. Tekan 'X' untuk logout ") in "Xx"
        otentik.sign_out(user_login)
    else:
        print("Login gagal! Username atau password salah!")