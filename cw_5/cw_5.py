import numpy
import random as rd
import math

# algorytm ewolucyjny
# generations = int(input("number of generations: "))
pop_size = 10
size = 6
populacja_poczatkowa = []
p_mute = 0.35
end = 0
iteration = 0


############################################################


def ile_bitow_rzeczywiste(granica_a, granica_b, c):
    r = (granica_b - granica_a) * (10 ^ c)
    ile_bitow = 0
    while r > 2 ** ile_bitow:
        ile_bitow = ile_bitow + 1
    return ile_bitow


def zamiana_rzeczywiste(populacja, ile_bitow, granica_a, granica_b):
    rzeczywiste = []
    for i in range(len(populacja)):
        wartosc_osobnika = 0
        osobnik = populacja[i]
        osobnik = osobnik[::-1]
        for j in range(ile_bitow):
            wartosc_bit = osobnik[j] * (2 ** j)
            wartosc_osobnika = wartosc_osobnika + wartosc_bit
        wartosc_rzeczywista = granica_a + ((granica_b - granica_a) * wartosc_osobnika) / ((2 ** ile_bitow) - 1)
        rzeczywiste.append(wartosc_rzeczywista)
    return rzeczywiste


##########################################################
# -------------------- kodowanie logarytmiczne

# -------------------- kodowanie zmiennoprzecinkowe

# -------------------- algorytm ewolucyjny
m = ile_bitow_rzeczywiste(0, 31, 6)
for j in range(pop_size):
    osobnik = numpy.random.choice([0, 1], size=m)
    populacja_poczatkowa.append(osobnik)
print("List of 10 lists:\n", *populacja_poczatkowa, sep="\n")
rzeczywiste = zamiana_rzeczywiste(populacja_poczatkowa, m, 0, 31)
for i in range(pop_size):
    print(populacja_poczatkowa[i])
    print(rzeczywiste[i])


def ruletka(liczby_rzeczywiste, populacja):
    suma_ocen = sum(liczby_rzeczywiste)
    prawdopodobienstwa = [x / suma_ocen for x in liczby_rzeczywiste]
    dystr = 0
    kolo_ruletki = []
    for i in range(len(liczby_rzeczywiste)):
        dystr = dystr + prawdopodobienstwa[i]
        kolo_ruletki.append(dystr)
    licznik = 0
    rodzice = []
    for j in range(2):
        los = rd.uniform(0, 1)
        print(los)
        while los > kolo_ruletki[licznik]:
            licznik = licznik + 1
        rodzic = populacja[licznik]
        rodzice.append(rodzic)
    return rodzice


rodzice_ruletka = ruletka(rzeczywiste, populacja_poczatkowa)
print(rodzice_ruletka)


def turniej(liczby_rzeczywiste, rozmiar_turnieju, populacja):
    wartosci = []
    rodzice = []
    for j in range(2):
        for i in range(rozmiar_turnieju):
            los = rd.randint(0, len(liczby_rzeczywiste))
            wartosci.append(liczby_rzeczywiste[los])
        najwieksza_wartosc = max(wartosci)
        indeks = liczby_rzeczywiste.index(najwieksza_wartosc)
        rodzic = populacja[indeks]
        rodzice.append(rodzic)
    return rodzice


rodzice_turniej = turniej(rzeczywiste, 2, populacja_poczatkowa)
print(rodzice_turniej)
# ------------------- metody reprodukcji i sukcesji

# kolo ruletki

# selekcja turniejowa


# sukcesja z czesciowym zastepowaniem

# sukcesja elitarna

# -------------------- operatory krzyzowania

# krzyzowanie jednopuntkowe

# krzyzowanie dwupunktowe

# krzyzowanie arytmetyczne

# --------------------- operatory mutacji

# mutacja rownomierna

# mutacja gaussowska

# --------------------- analiza
