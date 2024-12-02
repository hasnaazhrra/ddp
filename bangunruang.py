import math

def luas_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'luas balok adalah {hitung}')

def luas_prismasegitiga(luas, keliling, tinggi):
    hitung = 2 * luas + keliling * tinggi 
    print(f'luas prisma segitiga adalah {hitung}')

def luas_limas(luas, luassisi ):
    hitung = luas + luassisi
    print(f'luas limas adalah {hitung}')

def luas_tabung(r, t):
    hitung = 2 * r + 2 * t
    print(f'luas tabung adalah {hitung} ')

def luas_kubus(sisi):
    hitung = 6 * sisi * sisi
    print(f'luas kubus adalah {hitung}')
