#hangi say�lar�n 5'in kat� oldu�unu s�yleyen python kodu

sayilar = [18,15,22,19,85,32,65,30,95,10,12,20,32,55,34,28,101,5,4,32]
sayac=0 
for sayi in sayilar:
  if sayi%5 == 0:
    print ( "{} say�s� 5'in kat�d�r.".format(sayi))
    sayac=sayac+1
 
print("5'in kat� olan say� adeti : "+str(sayac))