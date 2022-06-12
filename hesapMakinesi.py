print("""

HESAP MAKÝNESÝ

TOPLAMA ÝÞLEMÝ YAPMAK ÝÇÝN 1 'e BASIN.
ÇIKARMA ÝÞLEMÝ YAPMAK ÝÇÝN 2 'e BASIN.
ÇARPMA ÝÞLEMÝ  YAPMAK ÝÇÝN 3 'e BASIN.
BÖLME ÝÞLEMÝ   YAPMAK ÝÇÝN 4 'e BASIN.

""")

islem = str(input("Ýþlem seçiniz: "))

if islem == "1":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
else:
    print("geçersiz iþlem girdiniz...")