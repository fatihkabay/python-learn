#girilen boy ve kilo deðerlerini beden kitle indexine dönüþtüren kodlardýr.
boy=float(input("Boyunuzu giriniz(m): "))
kilo=float(input("Kilonuzu giriniz(kg): "))
bki=kilo/(boy**2)
print("Beden Kitle Ýndeksi Deðeriniz:",round(bki,2))