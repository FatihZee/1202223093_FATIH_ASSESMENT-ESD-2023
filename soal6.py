class Menu:
    def __init__(self, nama, tipe, harga):
        self.nama = nama
        self.tipe = tipe
        self.harga = harga

class Restoran:
    def __init__(self):
        self.menu = {
            "Ayam Goreng Krispi": Menu("Ayam Goreng Krispi", "Makanan", 15000),
            "Ayam Puk Puk": Menu("Ayam Puk Puk", "Makanan", 13000),
            "Ayam Bakar": Menu("Ayam Bakar", "Makanan", 20000),
            "Es Teh": Menu("Es Teh", "Minuman", 5000),
            "Es Jeruk": Menu("Es Jeruk", "Minuman", 7000)
        }

    def hitung_biaya_pesanan(self, pesanan):
        total_biaya = 0
        for item, qty in pesanan.items():
            menu = self.menu[item]
            sub_total = qty * menu.harga
            if menu.tipe == "Makanan":
                sub_total += sub_total * 0.05
            elif menu.tipe == "Minuman":
                sub_total += sub_total * 0.03
            total_biaya += sub_total

        total_biaya += total_biaya * 0.15
        return total_biaya

jmk_restoran = Restoran()

rehan_pesanan = {"Ayam Bakar": 2, "Es Teh": 1}
rehan_biaya = jmk_restoran.hitung_biaya_pesanan(rehan_pesanan)

amba_pesanan = {"Ayam Puk Puk": 1, "Es Teh": 3}
amba_biaya = jmk_restoran.hitung_biaya_pesanan(amba_pesanan)

faiz_pesanan = {"Ayam Goreng Krispi": 1, "Ayam Puk Puk": 1, "Ayam Bakar": 1, "Es Teh": 1, "Es Jeruk": 1}
faiz_biaya = jmk_restoran.hitung_biaya_pesanan(faiz_pesanan)

print("Biaya pesanan Rehan Whangsap:", rehan_biaya)
print("Biaya pesanan Amba Roni:", amba_biaya)
print("Biaya pesanan Faiz Ngawi:", faiz_biaya)