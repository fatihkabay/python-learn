#bilgileri doldurduktan sonra i�e al�n�p al�nmad���n� s�yleyen kodlard�r.
ad_soyad=input("Ad�n�z-Soyad�n�z: ")
yabanci_dil=input("Bildi�iniz yabanc� dil: ")
yas=int(input("Ya��n�z: "))
 
if ((yabanci_dil=="�ngilizce" or yabanci_dil=="T�rk�e") and yas<40):
    print(" Sonu� ba�ar�l�")
else:
    print("Sonu� ba�ar�s�z")