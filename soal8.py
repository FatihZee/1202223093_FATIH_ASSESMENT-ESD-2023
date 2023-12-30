produk = {
    "TV": {"kategori": "elektronik", "harga": 1000},
    "headphone": {"kategori": "elektronik", "harga": 200},
    "baju": {"kategori": "fashion", "harga": 50},
    "gitar": {"kategori": "musik", "harga": 300},
    "sepatu": {"kategori": "olahraga", "harga": 80},
    "kamera": {"kategori": "elektronik", "harga": 600}
}

pelanggan = {
    "Rina": {"minat": ["elektronik", "musik"], "beli": ["TV", "headphone"]},
    "Budi": {"minat": ["fashion", "musik"], "beli": ["baju", "gitar"]},
    "Hartono": {"minat": ["olahraga", "elektronik"], "beli": ["sepatu", "kamera"]}
}

def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = pelanggan[nama_pelanggan]["minat"]
    beli_pelanggan = pelanggan[nama_pelanggan]["beli"]

    produk_rekomendasi = []

    for nama_produk, info_produk in produk.items():
        if info_produk["kategori"] in minat_pelanggan and nama_produk not in beli_pelanggan:
            produk_rekomendasi.append(nama_produk)

    return beli_pelanggan + produk_rekomendasi

nama_pelanggan = input("Masukkan nama pelanggan: ")

if nama_pelanggan in pelanggan:
    rekomendasi = rekomendasi_produk(nama_pelanggan)
    print(f"{nama_pelanggan} bisa tertarik dengan produk berikut: {rekomendasi}")
else:
    print(f"Data pelanggan {nama_pelanggan} tidak ditemukan.")