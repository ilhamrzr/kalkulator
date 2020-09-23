# Kalkulator persen untuk menghitung harga diskon di python

import pyfiglet
from os import system
# Format rupiah di python
# https://gist.github.com/ilhamrzr/378f57268141f5837b884d39f9149b52
import rupiah

system("cls")
kalkulator = pyfiglet.figlet_format("Kalkulator", font="slant")
print(kalkulator)
print("Created by Ilham\n")
print("")

harga = input("Masukan Haraga Barang : ")
diskon = input("Diskon Berapa : ")
total_diskon = int(harga) * int(diskon)//100
bayar = int(harga) - int(total_diskon)

system("cls")
print(kalkulator)
print("Created by Ilham\n")

# Penggunaan format rupiah
rp = rupiah.rupiah_format(bayar, True)  # Contoh Output : Rp. 100.00,00
rp2 = rupiah.rupiah_format(int(harga))  # Contoh Output : 10.000,00
print("Harga Barang = {}".format(rp2))
print("Diskon {}% dari pembelian".format(diskon))
print("Total = {}".format(rp))
