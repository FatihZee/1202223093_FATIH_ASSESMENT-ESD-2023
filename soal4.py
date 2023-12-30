def cek_duplikat(data):
    data_set = set()
    
    for angka in data:
        if angka in data_set:
            return True
        else:
            data_set.add(angka)
            
    return False

input_data = input("Masukkan data angka (pisahkan dengan koma dan spasi): ")
data = [int(angka) for angka in input_data.replace(',', '').split()]

output = cek_duplikat(data)
print("Output:", output)