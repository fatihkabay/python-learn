print("""

HESAP MAK�NES�

TOPLAMA ��LEM� YAPMAK ���N 1 'e BASIN.
�IKARMA ��LEM� YAPMAK ���N 2 'e BASIN.
�ARPMA ��LEM�  YAPMAK ���N 3 'e BASIN.
B�LME ��LEM�   YAPMAK ���N 4 'e BASIN.

""")

islem = str(input("��lem se�iniz: "))

if islem == "1":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonu�:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonu�:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonu�:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonu�:", sayi1/sayi2)
else:
    print("ge�ersiz i�lem girdiniz...")