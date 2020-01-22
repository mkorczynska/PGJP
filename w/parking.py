import shelve
import sys
from time import *


def sprzedaz(godz, rej):
    global baza
    abonament = input("Czy chcesz wykupic abonament <T/N>: ").upper()
    if abonament == 'T':
        baza[rej] = baza[rej][0], godz
    else:
        baza[rej] = baza[rej][0], 'brak'


def zmiana_stawki():
    global baza, stawka, okres
    print("\nZmiana wysokości opłat\n")
    print("Bieżąca stawka wynosi %.2f zł za %i minut(y)\n" % (stawka, okres))
    try:
        s = float(input("Podaj nową wysokość opłat: "))
        o = int(input("Podaj nowy czas naliczania w minutach: "))
    except:
        print("Błąd! Stawka nie została zmieniona!")
        return
    try:
        baza['_stawka'] = (s, o)
    except:
        print("Błąd! Stawka nie została zmieniona!")
    else:
        stawka = s
        okres = o


def init():
    global baza, stawka, okres
    try:
        baza = shelve.open('baza_parkingowa_2')
    except:
        print("Błąd! Baza danych nie została otwarta!")
        sys.exit(0)
    print("Baza danych została otwarta.")
    if '_stawka' in baza.keys():
        (stawka, okres) = baza['_stawka']
    else:
        (stawka, okres) = (0.0, 1)
        zmiana_stawki()


def menu():
    while True:
        print()
        print('_' * 100)
        print('PARKING'.center(100))
        print('_' * 100)
        print('[W] Wjazd [E] Wyjazd [P] Pojazdy [S] Stawka [K] Koniec'.center(100))
        print('_' * 100)
        w = input()[0].upper()
        if w in 'WEPSK':
            return w
        print('Nieznane polecenie -')


def pojazdy():
    global baza
    print()
    print('Lista pojazdów na parkingu'.center(33))
    print('_' * 58)
    print('|' + 'Nr rej.'.center(10) + '|' + 'Godz. parkowania'.center(20) + '|' + 'Data zakupu abonamentu'.center(
        25) + '|')
    print('_' * 58)
    for rej, godz in baza.items():
        if rej != '_stawka':
            if godz[1] == 'brak':
                print("|%9s|" % rej, strftime("%H:%M (%Y-%m-%d)", godz[0]), '|', godz[1].center(25), '|')
            else:
                print("|%9s|" % rej, strftime("%H:%M (%Y-%m-%d)", godz[0]), '|',
                      strftime("%Y-%m-%d", godz[0]).center(25), '|')
    print('_' * 58)


def wyjazd():
    global baza, stawka, okres, godz, rej, godz2
    print("Wyjazd pojazdu - godzina", strftime("%H:%M (%Y-%m-%d)"))
    rej = input("Podaj numer rejestracyjny pojazdu: ")
    if rej in baza.keys():
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
            jednostki = (minuty + okres - 1) / okres
            print("\n Do zapłaty: %.2f zł" % (jednostki * stawka))
            del baza[rej]
        else:
            dni = int(mktime(localtime()) - mktime(zakup_abonamentu)) // 43200
            baza[rej] = strptime("1 Jan 00", "%d %b %y"), baza[rej][1]
            print("Godzina wjazdu:", strftime("%H:%M (%Y-%m-%d)", godz))
            print("Do końca abonamentu pozostało %i dni." % (30 - dni))
    else:
        print("Błąd! Takiego pojazdu nie ma na parkingu!")


def wjazd():
    global baza, rej, godz
    godz = localtime()
    print("Wjazd pojadu - godzina", strftime("%H:%M (%Y-%m-%d)", godz))
    rej = input("Podaj numer rejestracyjny pojazdu: ")[:9]
    if rej == '_stawka':
        return
    if rej not in baza.keys():
        baza[rej] = godz, 'brak'
        sprzedaz(godz, rej)
        print("Wprowadzono.")
    elif baza[rej][0] != strptime("1 Jan 00", "%d %b %y"):
        print("Błąd! Taki pojazd już jest na parkingu")
    else:
        baza[rej] = godz, godz
        print("Wprowadzono")


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


init()
try:
    wybor()
except:
    print("Wystąpił błąd.")
baza.close()
