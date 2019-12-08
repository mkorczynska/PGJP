a = int(input("Podaj poczatek zakresu >"))
b = int(input("Podaj koniec zakresu >"))
n = int(input("Podaj liczbe lini do wygenerowani >"))
f = open("losowanie.txt",'w')
lib1 = 0
lib2 = 0
from random import randint
for x in range(n):
    lib1 = randint(a,b)
    lib2 = randint(a,b)
    while lib1 == lib2:
        lib2 = randint(a,b)
    f.write(str(lib1)+' '+str(lib2)+'\n')
f.close()