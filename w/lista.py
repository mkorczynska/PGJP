try:
    f = open("lista2.txt", 'r+')
except IOError:
    f = open("lista2.txt", 'w')
lista = []
t = ''
while t != 'y':
    t = input("Podaj liste studentow > [koniec: y ]")
    lista.append(t)
lista = lista[:len(lista)-1]
if f.mode == 'w':
    for line in lista:
        f.write(line + '\n')
else:
    f.seek(0,2)
    for line in lista:
        f.write(line + '\n')
f.close()
