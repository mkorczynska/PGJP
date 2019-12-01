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

