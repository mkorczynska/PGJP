# %%writefile parking2.py
# imporujemy shelve - do obslugi bazy
# sys - do wychodzeniania z programu
# time - do obslugi czasu
import shelve, sys
from time import *


def sprzedaz(godz, rej):
    global baza
    abonament = input("Czy chcesz wykupic abonament <Y/N>: ").upper()
    if abonament == 'Y':
        baza[rej] = baza[rej][0], godz
    else:
        baza[rej] = baza[rej][0], 'brak'


# zmiana oplat
def zmiana_stawki():
    global baza, stawka, okres  # zmienne globalne
    print("\nZmiana wysokości opłat\n")
    print("Bieżąca stawka wynosi %.2f zł za %i minut(y)\n" % (stawka, okres))
    try:
        s = float(input("Podaj nową wysokość opłat: "))
        o = int(input("Podaj nowy czas naliczania w minutach: "))
    except:
        print("Błąd wprowadzania danych! Stawka nie została zmieniona!")
        return
    try:
        baza['_stawka'] = (s, o)  # zapisujemy w bazie
    except:
        print("Błąd zapisu danych! Stawka nie została zmieniona!")
    else:
        stawka = s  # kopiujemy do
        okres = o  # zmiennych globalnych


# inicjaliazcja bazy danych
def init():
    global baza, stawka, okres
    try:
        baza = shelve.open('baza_parkingowa_2')  # otwarcie
    except:
        print("Błąd krytyczny! Baza danych nie została otwarta!")
        sys.exit(0)  # wyjście z programu
    print("Inicjalizacja udana. Baza danych została otwarta.")
    if '_stawka' in baza.keys():  # czy już istnieje?
        (stawka, okres) = baza['_stawka']  # tak - kopiujemy stawki
    else:
        (stawka, okres) = (0.0, 1)  # nie -
        zmiana_stawki()  # wczytujemy od użytkownika


# menu główne programu
def menu():
    while True:
        print()
        print('-' * 70)
        print('PARKING'.center(70))
        print('-' * 70)
        print('[W] Wjazd [E] Wyjazd [P] Pojazdy [S] Stawka [K] Koniec'.center(70))
        print('-' * 70)
        w = input()[0].upper()  # pierwszy znak (duża litera)
        if w in 'WEPSK':  # znany?
            return w  # tak - zwracamy go
        print('Nieznane polecenie -')


# lista pojazdów na parkingu
def pojazdy():
    global baza
    print()
    print('Lista pojazdów na parkingu'.center(33))
    print('-' * 58)
    print('|' + 'Nr rej.'.center(10) + '|' + 'Godz. parkowania'.center(20) + '|' + 'Data zakupu abonamentu'.center(
        25) + '|')
    print('-' * 58)
    for rej, godz in baza.items():
        if rej != '_stawka':
            if godz[1] == 'brak':
                print("|%9s|" % rej, strftime("%H:%M (%Y-%m-%d)", godz[0]), '|', godz[1].center(25), '|')
            else:
                print("|%9s|" % rej, strftime("%H:%M (%Y-%m-%d)", godz[0]), '|',
                      strftime("%Y-%m-%d", godz[0]).center(25), '|')
    print('-' * 58)


# rejestracja wyjazdu pojazdu
def wyjazd():
    global baza, stawka, okres, godz, rej, godz2
    print("Wyjazd pojazdu - godzina", strftime("%H:%M (%Y-%m-%d)"))
    rej = input("Podaj numer rejestracyjny pojazdu: ")
    if rej in baza.keys():  # czy taki byl zaparkowany?
        zakup_abonamentu = baza[rej][1]
        godz = baza[rej][0]
        if zakup_abonamentu != 'brak':
            dni = int(mktime(localtime()) - mktime(zakup_abonamentu)) // 43200
        if zakup_abonamentu == 'brak' or dni > 30:
            godz2 = localtime()
            sprzedaz(godz2, rej)
        zakup_abonamentu = baza[rej][1]
        godz = baza[rej][0]
        if zakup_abonamentu == 'brak':
            print("Godzina wjazdu:", strftime("%H:%M (%Y-%m-%d)", godz))
            minuty = int(mktime(localtime()) - mktime(godz)) / 60
            jednostki = (minuty + okres - 1) / okres  # naliczamy za rozpoczeta godzine
            print("\n Do zapłaty: %.2f zł" % (jednostki * stawka))
            del baza[rej]  # usuwamy wpis
        else:
            dni = int(mktime(localtime()) - mktime(zakup_abonamentu)) // 43200
            baza[rej] = strptime("1 Jan 00", "%d %b %y"), baza[rej][1]
            print("Godzina wjazdu:", strftime("%H:%M (%Y-%m-%d)", godz))
            print("Do końca abonamentu pozostało %i dni." % (30 - dni))
    else:
        print("Błąd! Takiego pojazdu nie ma na parkingu!")


# rejestracja wjazdu pojazdu
def wjazd():
    global baza, rej, godz
    godz = localtime()
    print("Wjazd pojadu - godzina", strftime("%H:%M (%Y-%m-%d)", godz))
    rej = input("Podaj numer rejestracyjny pojazdu: ")[:9]
    if rej == '_stawka':
        return  # zabezpieczenie
    if rej not in baza.keys():  # nie jest zaparkowany?
        baza[rej] = godz, 'brak'
        sprzedaz(godz, rej)
        print("Wprowadzono.")
    elif baza[rej][0] != strptime("1 Jan 00", "%d %b %y"):
        print("Błąd! Taki pojazd już jest na parkingu")
    else:
        baza[rej] = godz, godz
        print("Wprowadzono")


# realizacja wyboru użytkownika
def wybor():
    while True:
        w = menu()
        if w == 'K':
            break
        elif w == 'S':
            zmiana_stawki()
        elif w == 'P':
            pojazdy()
        elif w == 'E':
            wyjazd()
        elif w == 'W':
            wjazd()


#program główny
init() #otwiercie bazy
try:
    wybor() #interfejs uzytkownika
except:
    print("Wystąpił poważny błąd.")
baza.close() #zamykanie bazy