import numpy
import ga

# lista szesciu elementow z zakresu
random_list = numpy.random.uniform(low=-4.0, high=4.0, size=6)
print(random_list)

# lista dziesieciu szescioelementowych list
list_10 = []
for i in range(10):
    random_list = list(numpy.random.uniform(low=-4.0, high=4.0, size=6))
    list_10.append(random_list)
print(*list_10, sep="\n")

# iloczyn skalarny
vector = [4, -3, 3.5, 5, -7, 4.2]
dot = numpy.dot(random_list, vector)
print(dot)

# lista iloczynow skalarnych
dot_list = []
for j in range(10):
    dot = numpy.dot(vector, list_10[j])
    dot_list.append(dot)
print(dot_list)

# znalezienie szesciu najwiekszych
najwieksze_iloczyny = []
for k in range(6):
    naj = max(dot_list)
    ind = dot_list.index(naj)
    najwieksze_iloczyny.append(list_10[ind])
    dot_list.remove(naj)
print(*najwieksze_iloczyny, sep="\n")

# program genetyczny
nowe = []
for l in range(5):
    # losowanie liczb calkowitych - rodzicow
    l1 = numpy.random.randint(0, 5)
    l2 = numpy.random.randint(0, 5)
    pk = numpy.random.randint(0, 5)

    # krzyzowanie
    rodzic1 = najwieksze_iloczyny[l1]
    rodzic2 = najwieksze_iloczyny[l2]

    tmp = rodzic1[pk:].copy()
    rodzic1[pk:], rodzic2[pk:] = rodzic2[pk:], tmp

    nowe.append(rodzic1)
    nowe.append(rodzic2)

print("#####\n", *nowe, sep="\n")

# program genetyczny - mutacja

