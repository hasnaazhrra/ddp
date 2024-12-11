from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t: ", self.design, 
              "\nRacun \t: ", self.racun)
    
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak Berbisa")
anaconda.cetak_ular()

piton = Ular("Piton", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak Berbisa")
piton.cetak_ular()