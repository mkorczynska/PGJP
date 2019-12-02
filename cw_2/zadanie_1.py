import numpy

random_list = numpy.random.uniform(low=-4.0, high=4.0, size=6)
print("List of 6 random numbers: \n", random_list)

list_10 = []
for i in range(10):
    random_list = list(numpy.random.uniform(low=-4.0, high=4.0, size=6))
    list_10.append(random_list)
print("List of 10 lists:\n", *list_10, sep="\n")

vector = [4, -3, 3.5, 5, -7, 4.2]
dot = numpy.dot(random_list, vector)
print("Dot product: \n", dot)

dot_list = []
for j in range(10):
    dot = numpy.dot(vector, list_10[j])
    dot_list.append(dot)
print("List of dot products: \n", dot_list)

max_dots = []
for k in range(6):
    maximum = max(dot_list)
    index = dot_list.index(maximum)
    max_dots.append(list_10[index])
    dot_list.remove(maximum)
print("List of maximum dot products: ")
print(*max_dots, sep="\n")

new = []
for l in range(5):
    n1 = numpy.random.randint(0, 5)
    n2 = numpy.random.randint(0, 5)
    pc = numpy.random.randint(0, 5)

    p1 = max_dots[n1]
    p2 = max_dots[n2]

    tmp = p1[pc:].copy()
    p1[pc:], p2[pc:] = p2[pc:], tmp

    new.append(p1)
    new.append(p2)

print("List after crossover: \n", *new, sep="\n")

p_mute = 0.35
new_pop = []
for m in range(len(new)):
    pr = numpy.random.uniform(0, 1)
    if pr < p_mute:
        pm = numpy.random.randint(0, 5)
        rnd = numpy.random.uniform(-1, 1)
        new[m][pm] += rnd
        new_pop.append(new[m])
    else:
        new_pop.append(new[m])

print("New population:\n", *new_pop, sep="\n")

# losowanie poczatkowej (pierwsze 10 list)
# szesc list dajacych najwiekszy iloczyn skalarny
# losowanie pieciu par rodzicow
# krzyzowanie rodzicow (10 potomkow)
# dla kazdego potomka losowanie czy zajdzie mutacja - jesli tak, to mutowanie losowego genu
# wybor szesciu najlepszych potomkow
# jesli przekroczenie liczby pokolen, to koniec programu, jesli nie, to pkt 2