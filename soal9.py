from collections import Counter

def deteksi_anak_nakal(daftar_nama):
    counter_nama = Counter(daftar_nama)
    jumlah_kemunculan = counter_nama.most_common()

    if jumlah_kemunculan[0][1] == 1:
        return "Semuanya anak baik"
    elif jumlah_kemunculan[0][1] == jumlah_kemunculan[1][1]:
        anak_nakal = " dan ".join([nama for nama, count in jumlah_kemunculan if count == jumlah_kemunculan[0][1]])
        return f"{anak_nakal} Nackal"
    else:
        anak_nakal = jumlah_kemunculan[0][0]
        return f"{anak_nakal} Nackal"

input_test = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
output_test = deteksi_anak_nakal(input_test)
print(output_test)

input_test2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
output_test2 = deteksi_anak_nakal(input_test2)
print(output_test2)

input_test3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]
output_test3 = deteksi_anak_nakal(input_test3)
print(output_test3)
