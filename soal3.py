def siapa_yang_mengambil_kue(ningguang, hutao, xiao, childe, kue_utuh):
    if ningguang and kue_utuh:
        return "Ningguang"
    elif hutao:
        return "Hutao"
    elif xiao and kue_utuh:
        return "Xiao"
    elif childe:
        return "Childe"
    else:
        return "Tidak dapat menentukan"

ningguang = True  # Ningguang memeriksa kue
hutao = False  # Hutao memberikan kado
xiao = True  # Xiao memotret kue
childe = True  # Childe meletakkan air mineral
kue_utuh = False  # Kue tidak utuh

pencuri_kue = siapa_yang_mengambil_kue(ningguang, hutao, xiao, childe, kue_utuh)

print("Berdasarkan informasi yang diberikan, kemungkinan besar kue diambil oleh:", pencuri_kue)