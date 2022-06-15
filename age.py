#girilen yaþ sayýsýnýn yaþlýmý gençmi yoksa yetiþkinmi olduðunu belirleyen kodlardýr.
yas=int(input("Yaþýnýzý Giriniz: "))
if yas<18:
  print("Çocuksunuz")
if 18<yas<40:
  print("Gençsiniz")
if 40<yas<60: 
  print("Orta Yaþlýsýnýz") 
if yas>60 :
  print("Yaþlýsýnýz")