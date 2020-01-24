import pandas as pd
import random as rd

kapital_poczatkowy = 600
data = {"piwo": ["Porter", "Pszeniczne", "Pale Ale",
                 "Lager", "Pilzner", "Koźlak", "Stout", "Klasztorne"],
        "kod": ["000", "001", "010", "011", "110", "111", "100", "101"],
        "popyt 0,5": [2, 8, 5, 4, 8, 2, 2, 2],
        "popyt 0,7": [1, 10, 8, 8, 10, 5, 1, 1]}
df = pd.DataFrame(data)
print(df)

wielkosc_populacji = 20
osobniki = []

for i in range(wielkosc_populacji):
    s = ""
    for j in range(5):
        s += str(rd.randint(0, 1))
    osobniki.append(s)
print(osobniki)


def fitness(a):
    numer_piwa = 0
    for i in range(8):
        if a[0:3] == df['kod'][i]:
            numer_piwa = i
    koszt_07 = 0
    koszt_sok = 0
    przychod_07 = 0
    przychod_sok = 0
    if int(a[3]) == 1:
        popyt = df['popyt 0,7'][numer_piwa]
        przychod_07 = 2
        koszt_07 = 1
    else:
        popyt = df['popyt 0,5'][numer_piwa]
    if int(a[4]) == 1:
        popyt -= 1
        przychod_sok = 1
        koszt_sok = 0.25
    wartosc = (5 + przychod_07 + przychod_sok) * popyt
    koszt = (3 + koszt_07 + koszt_sok) * popyt
    przychod_koszt = [wartosc, koszt]
    return przychod_koszt


def statystyki(osobniki):
    wartosci_fitness = []
    procentowy_udzial = []
    suma_udzialow = []
    sumy_fitness = []
    wartosci_kosztow = []
    sumy_kosztow = []
    for i in osobniki:
        pom = fitness(i)
        wartosci_fitness.append(pom[0])
        wartosci_kosztow.append(pom[1])
        sumy_fitness.append(sum(wartosci_fitness))
        sumy_kosztow.append(sum(wartosci_kosztow))
    suma_fitness = sum(wartosci_fitness)
    suma_kosztow = sum(wartosci_kosztow)
    for i in wartosci_fitness:
        procentowy_udzial.append(100 * i / suma_fitness)
    for i in range(1, wielkosc_populacji + 1):
        suma_udzialow.append(sum(procentowy_udzial[0:i]))
    dane = [osobniki, wartosci_fitness, procentowy_udzial,
            suma_udzialow, sumy_fitness, sumy_kosztow]
    df_osobniki = pd.DataFrame(dane).T
    df_osobniki.columns = ["osobniki", "wartosci fitness",
                           "procentowy udział", "suma udzialow, narastajaco",
                           "Sumy fitness", "Sumy kosztow"]
    print(df_osobniki)
    print("Suma wartosci fitness:   ", suma_fitness)
    print("Suma kosztow:            ", suma_kosztow)
    return df_osobniki


def reprodukcja(osobniki, df_osobniki):
    for i in range(wielkosc_populacji):
        losowa = rd.random() * 100
        for j in range(wielkosc_populacji):
            if losowa < df_osobniki['suma udzialow, narastajaco'][j]:
                osobniki[i] = df_osobniki['osobniki'][j]
                break
    return osobniki


def krzyzowanie(osobniki):
    osobniki_do_krzyzowania = []
    numery_osobnikow_do_krzyzowania = []
    nowy_osobnik = []
    for i in range(len(osobniki)):
        if rd.random() >= 0.5:
            osobniki_do_krzyzowania.append(osobniki[i])
            numery_osobnikow_do_krzyzowania.append(i)
    print("Wybrane osobniki do krzyzowania:  ", osobniki_do_krzyzowania)
    pary_dla_osobnikow = []
    for i in osobniki_do_krzyzowania:
        para = osobniki[rd.randint(0, wielkosc_populacji - 1)]
        pary_dla_osobnikow.append(para)
        pkt_przeciecia = rd.choice([3, 4])
        nowy_osobnik.append(i[0:pkt_przeciecia] + para[pkt_przeciecia:5])
    print("Pary osobnikow do krzyzowania:  ", pary_dla_osobnikow)
    print("Potomkowie:  ", nowy_osobnik)
    for i in range(len(numery_osobnikow_do_krzyzowania)):
        osobniki[numery_osobnikow_do_krzyzowania[i]] = nowy_osobnik[i]
    print("Nowa populacja po krzyzowaniu:  ", osobniki)
    return osobniki


def mutacja(osobniki):
    geny_do_mutacji = []
    liczba_genow = wielkosc_populacji * 5
    for i in range(liczba_genow):
        if rd.random() < 0.02:
            geny_do_mutacji.append(i)
    for i in geny_do_mutacji:
        if int(osobniki[i // 5][i % 5]) == 0:
            nowy_osobnik = osobniki[i // 5][0:i % 5] + \
                           "1" + osobniki[i // 5][(i % 5) + 1:5]
            osobniki[i // 5] = nowy_osobnik
        else:
            nowy_osobnik = osobniki[i // 5][0:i % 5] + \
                           "0" + osobniki[i // 5][(i % 5) + 1:5]
            osobniki[i // 5] = nowy_osobnik
    print("Nowa populacja po mutacji: ", osobniki)
    return osobniki


i = 0
df_osobniki = statystyki(osobniki)
while ((df_osobniki['Sumy kosztow'][19] < (kapital_poczatkowy - 200) or
        df_osobniki['Sumy kosztow'][19] < (kapital_poczatkowy - 200 + 50))
       and df_osobniki['Sumy fitness'][19] < 2*kapital_poczatkowy):
    i += 1
    print('-' * 100)
    print("Cykl: ", i)
    print('_' * 100)
    df_osobniki = statystyki(osobniki)
    print('_' * 100)
    osobniki = reprodukcja(osobniki, df_osobniki)
    print('_' * 100)
    osobniki = krzyzowanie(osobniki)
    print('_' * 100)
    osobniki = mutacja(osobniki)

print("Ostateczna populacja: ")
ostateczne_osobniki = statystyki(osobniki)

nazwy = []
for i in range(wielkosc_populacji):
    for j in range(8):
        if osobniki[i][0:3] == df['kod'][j]:
            nazwy.append(df['piwo'][j])
    if osobniki[i][3] == '1':
        nazwy[i] = nazwy[i] + ' 0,7'
    if osobniki[i][4] == '1':
        nazwy[i] = nazwy[i] + ' z sokiem'

nazwy_unique = list(set(nazwy))
ilosc = [0 for i in range(len(nazwy_unique))]
for i in range(wielkosc_populacji):
    for j in range(len(nazwy_unique)):
        if nazwy[i] == nazwy_unique[j]:
            ilosc[j] += 1
data = [nazwy_unique, ilosc]
koncowe = pd.DataFrame(data).T
koncowe.columns = ["Piwo", "Ilość"]
print(koncowe)
