class Insan():
    def __init__(self,ad,soyad,yas,ulke,sehir):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.ulke=ulke
        self.sehir=sehir

    def kisi_Bilgileri (self):
        print("""Ad: {}\nSoyad: {}\nYas: {}\nUlke: {}\nSehir: {}\nYetenek: {}"""
              .format(self.ad,self.soyad,self.yas,self.ulke,self.sehir,self.yetenek))
    def yetenek_ekle (self,yetenek):
        self.yetenek=yetenek

human= Insan("Betül","Yaldiz","12","Türkiye","Ankara")
human.yetenek_ekle(["Dans","Müzik"])
human.kisi_Bilgileri()
