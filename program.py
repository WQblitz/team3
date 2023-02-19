# v.1.0 dzialajacej aplikacji

from curses.ascii import isdigit
from sre_compile import isstring
from traceback import print_tb


wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba całkowitą
if wiek.isdigit() == False:
    exit("wiek musi być liczbą całkowitą. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
    print("Witamy w apce. Możesz u nas kupować alkohol")
elif wiek>40 and wiek<120:
    print("witamy w apce. Możesz u nas kupować alkohol")
    print("Proszę korzystaj z produktów z umiarem")
elif wiek>=120:
    print("Kup se trumna, a nie gorzoła czoeku")
else:
    exit("Jesteś za młody/a na alkohol. Zapraszamy na disney.com :)")
plec = input("Podaj swoją płeć: M/K ")
#sprawdzenie czy płeć jest literą:
if plec.isdigit() == True:
    exit("Proszę podać płeć: M / K ")
plec=str(plec)
if plec==str("M"):
    print("Wybrano płeć: M")
elif plec==str("K"):
    print("Wybrano płeć: K")
else:
    exit("Proszę podać poprawną formę: M / K")

