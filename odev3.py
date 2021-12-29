print("Not Hesaplama.. ")
vize1 = int(input("1.Vize notu:"))
while (vize1 < 0 or vize1 > 100):
    vize1 = int(input("Hata! 0-100 arası not giriniz:"))
vize2 = int(input("2.Vize notu:"))
while (vize2 < 0 or vize2 > 100):
    vize2 = int(input("Hata! 0-100 arası not giriniz:"))
final = int(input("Final notu(0-100):"))
while (final < 0 or final > 100):
    final = int(input("Hata! 0-100 arası not giriniz:"))

ortalama = (vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10)

if (ortalama >= 90):
    print("AA")
elif (ortalama >= 85):
    print("BA")
elif (ortalama >= 80):
    print("BB")
elif (ortalama >= 75):
    print("CB")
elif (ortalama >= 70):
    print("CC")
elif (ortalama >= 65):
    print("DC")
elif (ortalama >= 60):
    print("DD")
elif (ortalama >= 55):
    print("FD")
else:
    print("FF")
