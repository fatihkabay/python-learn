saat = int(input("Kald���n�z S�reyi Girin:"))
 
ucret = 0
 
if saat <= 1:
  ucret = 5
elif saat <= 5:
  ucret = 4 * saat
else:
  ucret = 3 * saat
 
print("�demeniz Gereken �cret :{}".format(ucret))