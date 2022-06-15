#girilen iki sayýnýn girilen iþlemi yapma kodlarýdýr.
x=float(input("Birinci Sayýyý Giriniz: "))
y=float(input("Ýkinci Sayýyý Giriniz: "))
sec=input("Seçiminizi Yapýnýz(+,-,*,/): ")
 
if (sec=="+"):
    print(x, "+" ,y, "=", x+y)
if (sec=="-"):
    print(x, "-" ,y, "=", x-y)
if (sec=="*"):
    print(x, "*" ,y, "=", x*y)
if (sec=="/"):
    print(x, "/" ,y, "=", x/y)