x=float(input("Birinci Say�y� Giriniz: "))
y=float(input("�kinci Say�y� Giriniz: "))
sec=input("Se�iminizi Yap�n�z(+,-,*,/): ")
 
if (sec=="+"):
    print(x, "+" ,y, "=", x+y)
if (sec=="-"):
    print(x, "-" ,y, "=", x-y)
if (sec=="*"):
    print(x, "*" ,y, "=", x*y)
if (sec=="/"):
    print(x, "/" ,y, "=", x/y)