a = int(input("Podaj poczatek zakresu >"))
b = int(input("Podaj koniec zakresu >"))
n = int(input("Podaj liczbe lini do wygenerowani >"))
f = open("losowanie2.txt",'w')
lib1 = 0
listalib = []
if n > b-a+1:
    n = b-a+1
from random import randint
for x in range(n):
    lib1 = randint(a,b)
    while lib1 in listalib:
        lib1 = randint(a,b)
    listalib.append(lib1)
    f.write(str(lib1)+'\n')
f.close()