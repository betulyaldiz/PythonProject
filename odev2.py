birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"] #sıfır için ilk index boş
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def sayiAtama():
    sayi = int(input("İki basamaklı bir sayi giriniz:"))
    basamak = 0
    while (sayi > 0 and basamak != 2):
        basamak += 1
        sayi = int(input("Hata! İki basamaklı bir sayi giriniz:"))
    if (basamak == 2):
        return sayiOkunusu(sayi)


def sayiOkunusu(sayi):
    birlerBas = sayi % 10
    onlarBas = sayi // 10
    print("Sayinin okunusu:" + onlar[onlarBas] + birler[birlerBas])


while True:
    karsila = input("--------------------- \nSayı okuma programı.. \n(Çıkmak için q, devam etmek için enter basınız)")
    if (karsila == "q"):
        print("Programdan çıkılıyor")
        break
    else:
        sayiAtama()

#
