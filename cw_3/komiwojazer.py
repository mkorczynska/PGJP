import numpy
import math
import matplotlib.pyplot as plt
import random
from itertools import permutations
import copy

cities = ((123, 40), (234, 506), (56, 87), (22, 56), (231, 374), (456, 54), (648,639), (465,756), (630,876), (345,245), (20,539), (567,2))

x, y = zip(*cities)

LM = []
n = len(cities)


def Matierz_Dlugosci(n, x, y, DL):
    print(n * "---------")
    print("i", end="")
    for i in range(n):
        print("%8i" % i, end=" ")
    print()
    print(n * "---------")
    DL = []
    for i in range(n):
        DL.append([])
        for j in range(n):
            if i == j:
                r = 10000
            if i != j:
                r = math.sqrt((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2)
            DL[i].append(r)

    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            print(" %7.1f" % DL[i][j], end=" ")

        print()
    return DL

LM = Matierz_Dlugosci(n,x,y,LM)

road = [0,2,3,1,8,10,5,6,7,4,9,11]
road.append(road[0])

lenght = 0;

for i in range(len(road) - 1):
    lenght += LM[road[i]][road[i + 1]]

print(lenght)


def display_path(path, cities):
    xs, ys = zip(*cities)

    for i in range(len(path) - 1):
        plt.plot(
            (xs[path[i]], xs[path[i + 1]]),
            (ys[path[i]], ys[path[i + 1]]),
            color='pink'
        )

    plt.scatter(xs, ys, color='magenta')

    for i, city in enumerate(cities):
        plt.annotate(i, city)

    plt.show

display_path(road, cities)

def path_length(path, LM):
    return sum(LM[path[i]][path[i+1]] for i in range(len(path)-1))


def shortest_path(LM):
    shortest_path = None
    shortest_length = float('+inf')

    for path in permutations(list(range(len(LM)))):
        path = [*path, path[0]]
        l = path_length(path, LM)

        if l < shortest_length:
            shortest_length = l
            shortest_path = path

    return shortest_path

path = shortest_path(LM)

print('Shortest path:', path)
display_path(path, cities)

def scalar_multiplication(A, B):
    if(len(A) != len(B)):
        raise ValueError('Vectors has to have the same length')
    else:
        summ = 0
        for i in range(len(A)):
            summ += A[i]*B[i]
    return summ


def parent(descendant):
    parent = []
    index = []

    while (len(parent) < len(descendant)):
        i = random.randint(0, len(descendant) - 1)
        if (index.count(i) == 0):
            index.append(i)
            parent.append(descendant[i])

    return parent


def get_child(mother, father):
    child = copy.deepcopy(father)

    for i in range(len(mother)):
        a = i % (6 - 1) + 1
        child[i][:a] = mother[i][:a]

    return child


def mutate(child, coefficients, k):
    # szukam w którym wierszu jest najmniejszy wynik
    scalars = [scalar_multiplication(coefficients, r) for r in child]
    index = scalars.index(min(scalars))

    # Wyliczenie poszczegolnych wartości
    values = [child[index][i] * coefficients[i] for i in range(len(coefficients))]

    # mutacja k najgorszych
    for _ in range(k):

        # znajdowanie najgorszych
        i = values.index(min(values))

        # losowanie nowej (lepszej) wartości
        new_value = child[index][i]
        while new_value * coefficients[i] <= values[i]:
            new_value = random.uniform(-4.0, 4.0)
        child[index][i] = new_value


def optimize(descendant, coefficients):
    mother = parent(descendant)
    father = parent(descendant)

    descendant = get_child(mother, father)

    mutate(descendant, coefficients, int(0.1 * len(descendant) * len(descendant[0])))

    return descendant

# -------------------------------------------
# kod glowny
coefficients = [4, -3, 3.5, 5, -7, -4.2]

descendant = []

for i in range(10):
    l = []
    for j in range(6):
        r = round(random.uniform(-4.0, 4.0), 3)
        l.append(r)
    descendant.append(l)

print(*descendant, sep='\n')

scalars = []
for i in range(len(descendant)):
    scalars.append(scalar_multiplication(coefficients, descendant[i]))
print(scalars)

while len(descendant) > 6:
    index = scalars.index(min(scalars))
    del scalars[index]
    del descendant[index]

print(*descendant, sep="\n")

best_value = float('-inf')
best = None
for i in range(100):
    descendant = optimize(descendant, coefficients)
    scalars = [scalar_multiplication(r, coefficients) for r in descendant]

    i = scalars.index(max(scalars))

    if scalars[i] > best_value:
        best_value = scalars[i]
        best = descendant[i]

print(best)
print(best_value)
# -------------------------------------------

# def cartesian_matrix(coordinates):
#     matrix = {}
#     for l, (x1, y1) in enumerate(coordinates):
#         for k, (x2, y2) in enumerate(coordinates):
#             dx, dy = x1 - x2, y1 - y2
#             dist = (dx * dx + dy * dy) ** 0.5
#             matrix[l, k] = dist
#         return matrix
#
#
# def tour_length(matrix, tour):
#     total = 0
#     num_cities = len(tour)
#     for l in range(num_cities):
#         k = (l + 1) % num_cities
#         city_l = tour[l]
#         city_k = tour[k]
#         total += matrix[city_l, city_k]
#     return total
#
#
# m = cartesian_matrix(towns)
# t = [0, 8, 3, 2, 1, 5, 6, 7, 4]
# print(t, "%8.3f" % tour_length(m, t))
#
# wspx, wspy = zip(*towns)
# plt.scatter(wspx, wspy)
# for j in range(len(t)):
#     plt.annotate(j, towns[t[j]])
# plt.show()
#
# lines = plt.plot((x1, x2), (y1, y2))
# plt.setp(lines, color='r', linewidth=1.5)
#
# no_first_pop = 16
# new_population = []
#
# for i in range(0, no_first_pop):
#     rd.shuffle(t)
#     ax = list(t)
#     new_population.append(ax)
#
#
# def choice_for_crossover(pop, no_crossover):
#     pop_chosen = []
#     len_tours = [tour_length(m, os) for os in pop]
#     for j in range(0, len(pop)):
#         max_fitness_idx = len_tours.index(min(len_tours))
#         pop_chosen.append(pop[max_fitness_idx])
#         len_tours[max_fitness_idx] = 9999999999
#     return pop_chosen[:no_crossover]
#
#
# chosen_pop = choice_for_crossover(new_population, no_for_crossover)
#
# def crossover(parents, offspring_size):
#     offspring=[]
#     for i in range(0, offspring_size):
#         chrom = [0 for j in range(0, num_towns)]
#         offspring.append(chrom)
#     for k in range(0, int(offspring_size/2)):
#         p_1 = rd.randint(0, no_for_crossover-1)
#         p_2 = rd.randint(0, no_for_crossover-1)
#         c_point = rd.randint(0, len(parents[1]))
#         offspring[k] = parents[p_1][:c_point]
#         offspr_1 = [x for x in parents[p_2] if not x in offspring[k]]
#         offspring[k] += offspr_1
#         offspring[offspring_size-k-1] = parents[p_2][:c_point]
#         offspr_2 = [x for x in parents[p_1] if not x in offspring[offspring_size-k-1]]
#         offspring[offspring_size-k-1] += offspr_2
#     return offspring
#
#
# def mutation(offspring_crossover, p_mute, offspring_size):
#     for idx in range(0, offspring_size):
#         pr = rd.uniform(0, 1)
#         if pr < p_mute:
#             m_point1 = rd.randint(0, num_towns - 1)
#             m_point2 = rd.randint(0, num_towns - 1)
#             pom = offspring_crossover[idx][m_point1]
#             offspring_crossover[idx][m_point1] = offspring_crossover[idx][m_point2]
#             offspring_crossover[idx][m_point2] = pom
#         return offspring_crossover
#
# print(" -----------pop--------------")
# for i in range(0, no_first_pop):
#     print(new_population[i], "%8.3f" % tour_length(m, new_population[i]))
# print(" -----------pop-chosen--------")
# chosen_pop = choice_for_crossover(new_population, no_for_crossover)
# for i in range(0, no_for_crossover):
#     print(chosen_pop[i], "%8.3f" % tour_length(m, chosen_pop[i]))
# off = crossover(chosen_pop, no_for_crossover)
# print("------potomkowie---------")
# for i in range(0, no_for_crossover)
#     print(off[i], "%8.3f" % tour_length(m, off[i]))
# off = mutation(off, p_mute, no_for_crossover)
# print("----po mutacji----")
# for i in range(0, no_for_crossover):
#     print(off[i], "%8.3f" % tour_length(m, off[i]))
