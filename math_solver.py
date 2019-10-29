import math
print("Program Solver Math\n","1. Perhitungan Keliling Lingkaran \n","2. Volume Balok\n","3. Volume Bola\n","4. Volume Kerucut\n")
pilihan = int(input("Masukan Solver Yang Anda Inginkan : "))

if pilihan == 1 :
    a = float(input("jari - jari : "))
    luas = 2 * math.pi * a * a
    print("Luas Lingkaran : ", luas)
elif pilihan == 2:
    a = float(input("Panjang : "))
    b = float(input("Lebar   : "))
    c = float(input("Tinggi  : "))
    volume = a * b * c
    print("Hasilnya adalah : " , volume)
elif pilihan == 3:
    a = float(input("Masukan Jari Jari : "))
    volume = 4/3 * math.pi * a * a * a
    print("Hasilnya adalah : ", volume)
elif pilihan == 4:
    a = float(input("Masukan Jari Jari      : "))
    b = float(input("Masukan Tinggi Kerucut : "))
    volume = 1/3 * math.pi * a * a * b
    print("hasilnya adalah : ", volume)
else : 
    print("pilihan tidak ada , coba perhatikan baik\" menu yang ada")