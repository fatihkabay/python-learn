yeniMaas=0
maas=int(input("Maa�� Gir : "))
zam=int(input("Zam Oran�(%) : ")) #maa��n girilen de�ere g�re zaml� maa�� bulma kodu
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zaml� Maa� :",yeniMaas)