from random import randint

a = int(input("Poczatek zakresu (liczba a): "))
b = int(input("Koniec zakresu (liczba b): "))
n = int(input("Liczba linii do wygenerowania (n): "))

f = open("losowanie.txt", 'w')

for x in range(n):
    number = randint(a, b)
    f.write(str(number) + '\n')
f.close()
