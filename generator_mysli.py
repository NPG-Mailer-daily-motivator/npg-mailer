import random

ilosc_linii = sum(1 for line in open('zlote-mysli.txt'))

linia = random.randint(0, ilosc_linii)

mysli_plik = open("zlote-mysli.txt", "r", encoding="utf-8")
mysli_plik_linie = mysli_plik.readlines()
mysli_plik.close()

random_mysl = mysli_plik_linie[linia]
del mysli_plik_linie[linia]
mysli_plik_wrt = open("zlote-mysli.txt", "w+", encoding="utf-8")
for lin in mysli_plik_linie:
    mysli_plik_wrt.write(lin)
mysli_plik_wrt.close()

print (random_mysl)
