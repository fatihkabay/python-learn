saniye=int(input("Saniye Giriniz:"))
saat=saniye//3600 #1saat 3600 saniyeye e�ittir.
saniye=saniye%3600
dakika=saniye//60
saniye=saniye%60
print("Girdi�iniz Saniyenin Saat D�n���m�:",saat,"sa",dakika,"dk",saniye,"sn")