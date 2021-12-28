def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    sayilar = list(range(min_sayi, max_sayi + 1))
    bolunensayilar = []
    for i in sayilar:
        if (i % bolunecek_sayi == 0):
            bolunensayilar.append(i)
    return bolunensayilar


while True:
    min_sayi = input("Min sayi:")
    max_sayi = input("Max sayi:")
    while (max_sayi <= min_sayi):
        print("Max sayi, min sayidan küçük ve eşit olamaz.Daha büyük bir sayi giriniz..")
        max_sayi = input("Max sayi:")
    sayi = input("Boluncek sayi:")
    if (sayi == "q"):
        print("Program sonlandırılıyor.")
        break
    else:
        sayi = int(sayi)
        max_sayi = int(max_sayi)
        min_sayi = int(min_sayi)
        print("Bölünen sayılar:", bolunenSayiBulma(min_sayi, max_sayi, sayi))
