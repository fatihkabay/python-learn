#sayýnýn faktöriyelini hesaplayan kodlardýr.
i=1
sonuc=1
 
faktoriyel=int(input("Faktoriyeli hesaplanacak sayýyý giriniz: "))
 
while (i<=faktoriyel):
    sonuc=i*sonuc
    i=i+1
    
print("Sonuc=",sonuc)
 