from collections import Counter

def deteksi_anak_nakal(anak):
    hasil_analisis = analisis_anak(anak)
    
    maksimal_sebutan = max(hasil_analisis.values())
    nama_nakal = [nama for nama, jumlah in hasil_analisis.items() if jumlah == maksimal_sebutan]
    
    if len(nama_nakal) > 1:
        return " dan ".join(nama_nakal) + " Nackal"
    elif len(nama_nakal) == 1:
        return f"{nama_nakal[0]} Nackal"
    else:
        return "Semuanya anak baik"

def analisis_anak(anak):
    return Counter(anak)

nama_anak_input = input("Masukkan nama-nama anak (pisahkan dengan spasi): ")
nama_anak = nama_anak_input.replace("“", "").replace("”", "").replace(",", "").split()

hasil_deteksi = deteksi_anak_nakal(nama_anak)

print(f"Nama anak yang nakal: {hasil_deteksi}")