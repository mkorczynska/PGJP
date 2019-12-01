SPK = float(input("Poczatkowy stan konta: "))
P = float(input("Roczna stopa oprocentowania: "))
N = float(input("Liczba lat: "))
SKK = SPK*((1+(P/12)/100)**(N*12))
print("Stan poczatkowy konta: ", SPK, "\n",
      "oprocentowanie: ", P, "%\n",
      "Stan konta za", N, "lat: ", SKK)
