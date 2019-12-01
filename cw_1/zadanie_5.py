mozliwe_oceny = [2, 2.5, 3, 3.5, 4, 4.5, 5]
oceny = input("Wprowadz oceny: ")

if oceny.find(', ') != -1:
    oceny = [float(x) for x in oceny.split(', ')]
elif oceny.find(' ') != -1:
    oceny = [float(x) for x in oceny.split(' ')]
elif oceny.find(',') != -1:
    oceny = [float(x) for x in oceny.split(',')]
else:
    oceny = [float(x) for x in oceny.split()]

suma = 0
otrzymane_oceny = []
for i in oceny:
    if i in mozliwe_oceny:
        otrzymane_oceny.append(i)
        suma += i
else:
    if len(otrzymane_oceny) == 0:
        print("Brak ocen.")
    else:
        srednia = suma / len(otrzymane_oceny)
        print("Otrzymane oceny:", end=" ")
        for j in otrzymane_oceny:
            print(j, end=", ")
        else:
            print("\nSrednia otrzymanych ocen:", srednia)
