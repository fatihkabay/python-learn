#while d�ng�s� ile �ifre olu�turma kodlar�d�r.
while True:
    sifre = input("Bir �ifre giriniz: ")
    if len(sifre) < 4 or len(sifre) > 4:
        print("4 karakterden olu�an bir �ifre girmelisiniz.")
        continue
    else:
        print("�ifreniz olu�turuldu: ", sifre)
        break;
print("�ifrenizi while d�ng�s� i�inde olu�turdunuz. ")