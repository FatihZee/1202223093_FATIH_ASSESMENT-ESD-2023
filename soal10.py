def hitung_kembalian(total_pembayaran, total_belanja):
    denominasi_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_pembayaran - total_belanja

    hasil_kembalian = {}

    for denominasi in denominasi_uang:
        jumlah = kembalian // denominasi
        if jumlah > 0:
            hasil_kembalian[str(denominasi)] = jumlah
            kembalian %= denominasi

    return hasil_kembalian

total_pembayaran = int(input("Masukkan total pembayaran: "))
total_belanja = int(input("Masukkan total belanja: "))

hasil_kembalian = hitung_kembalian(total_pembayaran, total_belanja)
print(f"{total_pembayaran} - {total_belanja} = {hasil_kembalian}")