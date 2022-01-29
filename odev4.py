class Ogrenci():
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

    def bilgileriGoster(self):
        print("""
        Ad   : {}
        Soyad: {}
        Sınıf: {}
        """.format(self.ogrenciAdi, self.ogrenciSoyadi, self.ogrenciSinifi))


class Soru():
    def __init__(self, dogru, yanlis):
        self.dogru = int(dogru)
        self.yanlis = int(yanlis)

    def NetSayisi(self):
        self.net = self.dogru - (self.yanlis / 4)
        return self.net

    def Hesapla(self,net):
        self.sonuc = net * 2
        return self.sonuc

    def puan(self):
        print("""
        Net   : {}
        Puan  : {}
        """.format(self.net,self.sonuc))

sınavSonucu = Soru(30, 20)
ogrenci1 = Ogrenci("Betül", "Yaldiz", 12)
ogrenci1.bilgileriGoster()
sınavSonucu.puan()

