#say�n�n fakt�riyelini hesaplayan kodlard�r.
i=1
sonuc=1
 
faktoriyel=int(input("Faktoriyeli hesaplanacak say�y� giriniz: "))
 
while (i<=faktoriyel):
    sonuc=i*sonuc
    i=i+1
    
print("Sonuc=",sonuc)
 