#while döngüsü ile þifre oluþturma kodlarýdýr.
while True:
    sifre = input("Bir þifre giriniz: ")
    if len(sifre) < 4 or len(sifre) > 4:
        print("4 karakterden oluþan bir þifre girmelisiniz.")
        continue
    else:
        print("Þifreniz oluþturuldu: ", sifre)
        break;
print("Þifrenizi while döngüsü içinde oluþturdunuz. ")