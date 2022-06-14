yeniMaas=0
maas=int(input("Maaþý Gir : "))
zam=int(input("Zam Oraný(%) : ")) #maaþýn girilen deðere göre zamlý maaþý bulma kodu
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlý Maaþ :",yeniMaas)