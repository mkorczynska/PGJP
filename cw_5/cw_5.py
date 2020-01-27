import math
import random as rd
import time
import pandas as pd


def dziesietne_binarne(liczba, n):
    top = (2 ** n) - 1
    if liczba > top:
        print("Liczba poza zakresem.")
        string = "1" * n
        return string
    else:
        s = bin(liczba)
        return s[2:len(s)].zfill(n)


def binarne_dziesietne(liczba, n):
    wynik = 0
    for i in range(n):
        wynik += (2 ** i) * int(liczba[len(liczba) - i - 1])
    return wynik


def dost(start, stop, n, liczba):
    zasieg = stop - start
    top = (2 ** n) - 1
    wynik = liczba * (zasieg / top) + start
    return wynik


def funkcja(x):
    wynik = 2 * math.sin(x) - 3 * math.sin(x ** 2) + 1
    return wynik


def populacja(n1, n2):
    wynik = []
    temp3 = []
    temp = (2 ** n1)
    for i in range(n2):
        while True:
            temp2 = rd.randrange(0, temp)
            check = 0
            if i == 0:
                temp3.append(temp2)
                wynik.append(dziesietne_binarne(temp2, n1))
                break
            else:
                for i in range(len(temp3)):
                    if temp2 == temp3[i]:
                        check = 1
                if check == 0:
                    temp3.append(temp2)
                    wynik.append(dziesietne_binarne(temp2, n1))
                    break

    return wynik


def selekcja_elitarna(populacja, n1, n2, start, stop):
    temp = []
    wynik = populacja
    for i in range(len(populacja)):
        temp2 = binarne_dziesietne(populacja[i], n1)
        temp2 = dost(start, stop, n1, temp2)
        temp.append(funkcja(temp2))
    dl = len(temp)
    for i in range(n2):
        tempmin = min(temp)
        for j in range(dl):
            if temp[j] == tempmin:
                wynik.pop(j)
                temp.pop(j)
                dl -= 1
                break
    return wynik


def selekcja_czesciowa(populacja, n1, n2, start, stop):
    temp = []
    temp3 = []
    tempN = int(n2 / 2)
    tempN2 = n2 - tempN
    for i in range(tempN):
        if i == 0:
            temp.append(rd.randrange(0, len(populacja)))
            temp3.append(populacja[temp[0]])
        else:
            while True:
                check = 0
                temp2 = rd.randrange(0, len(populacja))
                for i in range(len(temp)):
                    if temp2 == temp[i]:
                        check = 1
                if check == 0:
                    temp.append(temp2)
                    temp3.append(populacja[temp2])
                    break
    wynik = populacja
    for i in range(len(temp3)):
        for j in range(len(populacja)):
            if populacja[j] == temp3[i]:
                wynik.pop(i)
                break
    wynik = selekcja_elitarna(wynik, n1, tempN2, start, stop)
    return wynik


def krzyzowanie_1(rodzic1, rodzic2, n):
    los = rd.randrange(0, n)
    temp_rodzic1 = list(rodzic1)
    temp_rodzic2 = list(rodzic2)
    dl = len(temp_rodzic1)
    wynik1 = []
    wynik2 = []
    wynik = []
    for i in range(dl):
        if i >= los:
            wynik1.append(temp_rodzic2[i])
            wynik2.append(temp_rodzic1[i])
        else:
            wynik1.append(temp_rodzic1[i])
            wynik2.append(temp_rodzic2[i])
    temp_str1 = "".join(wynik1)
    temp_str2 = "".join(wynik2)
    wynik.append(temp_str1)
    wynik.append(temp_str2)
    return wynik


def krzyzowanie_2(rodzic1, rodzic2, n):
    los1 = rd.randrange(0, n)
    while True:
        los2 = rd.randrange(0, n)
        if los1 != los2:
            break
    if los1 > los2:
        temp = los1
        los1 = los2
        los2 = temp
    temp_rodzic1 = list(rodzic1)
    temp_rodzic2 = list(rodzic2)
    dl = len(temp_rodzic1)
    wynik1 = []
    wynik2 = []
    wynik = []
    for i in range(dl):
        if i >= los1:
            if i >= los2:
                wynik1.append(temp_rodzic1[i])
                wynik2.append(temp_rodzic2[i])
            else:
                wynik1.append(temp_rodzic2[i])
                wynik2.append(temp_rodzic1[i])
        else:
            wynik1.append(temp_rodzic1[i])
            wynik2.append(temp_rodzic2[i])
    temp_str1 = "".join(wynik1)
    temp_str2 = "".join(wynik2)
    wynik.append(temp_str1)
    wynik.append(temp_str2)
    return wynik


def mutacja_rownomierna(x, n, p_mute):
    los1 = rd.randrange(0, n)
    los2 = rd.randint(0, 1)
    los3 = rd.randint(0, 1)
    temp = list(x)
    if los3 < p_mute:
        temp[los1] = str(los2)
    wynik = "".join(temp)
    return wynik


def mutacja_gaussowska(x, n, p_mute):
    los = rd.randint(0, 1)
    temp = binarne_dziesietne(x, n)
    range = (2 ** n) - 1
    range = range * 0.1
    if los < p_mute:
        while True:
            gauss = int(rd.gauss(temp, range))
            if gauss > 0:
                if gauss < (2 ** n) - 1:
                    break
        wynik = dziesietne_binarne(gauss, n)
    else:
        wynik = dziesietne_binarne(temp, n)
    return wynik


def selekcja(x, populacja, n1, n2, start, stop):
    if x == 0:
        wynik = selekcja_czesciowa(populacja, n1, n2, start, stop)
    else:
        wynik = selekcja_elitarna(populacja, n1, n2, start, stop)
    return wynik


x = populacja(5, 10)


def rodzice(populacja):
    dl = len(populacja)
    wynik = []
    temp = rd.randrange(0, dl)
    wynik.append(temp)
    while True:
        temp2 = rd.randrange(0, dl)
        if temp2 != temp:
            wynik.append(temp2)
            break
    return wynik


def krzyzowanie(x, populacja, n):
    indexes = rodzice(populacja)
    rodzic1 = populacja[indexes[0]]
    rodzic2 = populacja[indexes[1]]
    if x == 0:
        wynik = krzyzowanie_1(rodzic1, rodzic2, n)  # krzyzowanie jednopunktowe
    else:
        wynik = krzyzowanie_2(rodzic1, rodzic2, n)  # krzyzowanie dwupunktowe
    return wynik


def mutacja(x, x2, n, p_mute):
    if x == 0:
        wynik = mutacja_rownomierna(x2, n, p_mute)
    else:
        wynik = mutacja_gaussowska(x2, n, p_mute)
    return wynik


selekcja_typ = input("Wybierz rodzaj selekcji : 0 - selekcja z czesciowym zastępowaniem, 1 - elitarna ")
selekcja_typ = int(selekcja_typ)
krzyzowanie_typ = input("Wybierz rodzaj krzyzowania: 0 - jednopunktowe, 1 - dwupunktowe")
krzyzowanie_typ = int(krzyzowanie_typ)
mutacja_typ = input("Wybierz rodzaj mutacji: 0 - rownomierna, 1 - gaussowska ")
mutacja_typ = int(mutacja_typ)
pokolenia = 2000
populac = 100
wynik = 8
pm = 0.3
przedzial_1 = 5
przedzial_2 = 10
nbin = 15

time1 = time.time()
x_st = populacja(nbin, populac)

for i in range(pokolenia):
    y_st = krzyzowanie(krzyzowanie_typ, x_st, nbin)
    z_st1 = mutacja(mutacja_typ, y_st[0], nbin, pm)
    z_st2 = mutacja(mutacja_typ, y_st[1], nbin, pm)
    x_st.append(z_st1)
    x_st.append(z_st2)
    nil = len(x_st) - wynik
    x_st = selekcja(selekcja_typ, x_st, nbin, nil, przedzial_1, przedzial_2)
time2 = time.time()
time_score = time2 - time1
print("Czas wykonania zadania: ", round(time_score, 2), "sekund")
print("Wynik: ")
licznik = 0
x1 = 0
x2 = 0
for i in range(len(x_st)):
    x1 += dost(przedzial_1, przedzial_2, binarne_dziesietne(x_st[i], nbin), nbin)
    x2 += funkcja(dost(przedzial_1, przedzial_2, nbin, binarne_dziesietne(x_st[i], nbin)))
    licznik += 1
print(x2 / licznik)

analiza = []
ile_powtorzen = 100
print("Analiza")
for z in range(ile_powtorzen):
    for w in range(2):
        for j in range(2):
            for k in range(2):
                wyniki = []
                time1 = time.time()
                selekcja_typ = w
                krzyzowanie_typ = j
                mutacja_typ = k
                for i in range(pokolenia):
                    y_st = krzyzowanie(krzyzowanie_typ, x_st, nbin)
                    z_st1 = mutacja(mutacja_typ, y_st[0], nbin, pm)
                    z_st2 = mutacja(mutacja_typ, y_st[1], nbin, pm)
                    x_st.append(z_st1)
                    x_st.append(z_st2)
                    nil = len(x_st) - wynik
                    x_st = selekcja(selekcja_typ, x_st, nbin, nil, przedzial_1, przedzial_2)
                time2 = time.time()
                time_score = time2 - time1
                print("_" * 100)
                print("Czas wykonania zadania: ", round(time_score, 2), "sekund")
                print("Wynik: ")
                licznik = 0
                x1 = 0
                x2 = 0
                for i in range(len(x_st)):
                    x1 += dost(przedzial_1, przedzial_2, binarne_dziesietne(x_st[i], nbin), nbin)
                    x2 += funkcja(dost(przedzial_1, przedzial_2, nbin, binarne_dziesietne(x_st[i], nbin)))
                    licznik += 1
                rezultat = x2 / licznik
                print(w, j, k)
                print(rezultat)
                wyniki.append(time_score)
                wyniki.append(rezultat)
                analiza.append(wyniki)

print(*analiza, sep="\n")

wszystkie_sumy = []
wszystkie_czasy = []
for u in range(0, 8):
    suma = 0
    czas = 0
    for t in range(u, 8 * ile_powtorzen - 1, 8):
        suma = suma + analiza[t][1]
        czas = czas + analiza[t][0]
    wszystkie_sumy.append(suma)
    wszystkie_czasy.append(czas)
print(wszystkie_sumy)
print(wszystkie_czasy)

sredni_wynik = []
sredni_czas = []
for i in range(0, 8):
    sc = wszystkie_czasy[i] / ile_powtorzen
    sredni_czas.append(sc)

    sw = wszystkie_sumy[i] / ile_powtorzen
    sredni_wynik.append(sw)

print(sredni_czas)
print(sredni_wynik)

nazwy = ["000", "001", "010", "011", "100", "101", "110", "111"]

df = pd.DataFrame(list(zip(nazwy, sredni_wynik, sredni_czas)),
                  columns=['Nazwa', 'Sredni wynik', 'Sredni czas'])

print(df)
