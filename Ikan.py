from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.jenis = jenis
        self.warna = warna

    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t: ", self.jenis,
              "\nWarna \t: ", self.warna)
    
Hiu = Ikan("Ikan Hiu", "Anjing laut", "Laut", "Beranak", "Hiu Paus", "Biru")
Hiu.cetak_ikan()

Gabus = Ikan("ikan gabus", "cacing", "kali", "beranak", "Gabus Micropeltes", "hitam")
Gabus.cetak_ikan()