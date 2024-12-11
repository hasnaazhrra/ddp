from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.jenis = jenis
        self.warna = warna

    def cetak_burung(self):
        super().cetak()
        print("Jenis \t: ", self.jenis,
              "\nWarna \t: ", self.warna)
    
elang = Burung("Elang", "kacang", "Udara", "Bertelur", "Elang jawa", "hitam")
elang.cetak_burung()

gereja = Burung("Gereja", "kacang", "Udara", "Bertelur", "Elang jawa", "hitam")
gereja.cetak_burung() 