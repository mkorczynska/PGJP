from random import randint

a = int(input("Poczatek zakresu (liczba a): "))
b = int(input("Koniec zakresu (liczba b): "))
n = int(input("Liczba linii do wygenerowania (n): "))

f = open("losowanie_2.txt", 'w')
number = 0
numlist = []
if n > b-a+1:
    n = b-a+1

print("Liczba linii do wygenerowania: ", n)

for x in range(n):
    number = randint(a, b)
    while number in numlist:
        number = randint(a, b)
    numlist.append(number)
    f.write(str(number)+'\n')
f.close()
