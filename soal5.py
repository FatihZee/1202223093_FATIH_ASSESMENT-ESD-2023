from math import factorial

def hitung_kombinasi(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def jumlah_kombinasi_username(nama_lengkap):
    username = nama_lengkap.replace(" ", "").lower()

    panjang_username = len(username)

    total_kombinasi = 0
    for i in range(1, min(7, panjang_username + 1)):
        total_kombinasi += hitung_kombinasi(panjang_username, i)

    return total_kombinasi

nama_lengkap = input("Masukkan nama lengkap: ")

jumlah_kombinasi = jumlah_kombinasi_username(nama_lengkap)
print("Jumlah kombinasi username yang mungkin:", jumlah_kombinasi)