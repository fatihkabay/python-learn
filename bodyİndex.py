#girilen boy ve kilo de�erlerini beden kitle indexine d�n��t�ren kodlard�r.
boy=float(input("Boyunuzu giriniz(m): "))
kilo=float(input("Kilonuzu giriniz(kg): "))
bki=kilo/(boy**2)
print("Beden Kitle �ndeksi De�eriniz:",round(bki,2))