saniye=int(input("Saniye Giriniz:"))
saat=saniye//3600 #1saat 3600 saniyeye eşittir.
saniye=saniye%3600
dakika=saniye//60
saniye=saniye%60
print("Girdiğiniz Saniyenin Saat Dönüşümü:",saat,"sa",dakika,"dk",saniye,"sn")