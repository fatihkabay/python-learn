#bilgileri doldurduktan sonra iþe alýnýp alýnmadýðýný söyleyen kodlardýr.
ad_soyad=input("Adýnýz-Soyadýnýz: ")
yabanci_dil=input("Bildiðiniz yabancý dil: ")
yas=int(input("Yaþýnýz: "))
 
if ((yabanci_dil=="Ýngilizce" or yabanci_dil=="Türkçe") and yas<40):
    print(" Sonuç baþarýlý")
else:
    print("Sonuç baþarýsýz")