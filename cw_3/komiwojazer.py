import numpy
import matplotlib.pyplot as plt
import random as rd

towns = [(30, 70), (50, 60), (30, 50), (0, 40), (50, 20), (30, 0), (30, 20), (40, 30), (60, 30)]


def cartesian_matrix(coordinates):
    matrix = {}
    for l, (x1, y1) in enumerate(coordinates):
        for k, (x2, y2) in enumerate(coordinates):
            dx, dy = x1 - x2, y1 - y2
            dist = (dx * dx + dy * dy) ** 0.5
            matrix[l, k] = dist
        return matrix


def tour_length(matrix, tour):
    total = 0
    num_cities = len(tour)
    for l in range(num_cities):
        k = (l + 1) % num_cities
        city_l = tour[l]
        city_k = tour[k]
        total += matrix[city_l, city_k]
    return total


m = cartesian_matrix(towns)
t = [0, 8, 3, 2, 1, 5, 6, 7, 4]
print(t, "%8.3f" % tour_length(m, t))

wspx, wspy = zip(*towns)
plt.scatter(wspx, wspy)
for j in range(len(t)):
    plt.annotate(j, towns[t[j]])
plt.show()

lines = plt.plot((x1, x2), (y1, y2))
plt.setp(lines, color='r', linewidth=1.5)

no_first_pop = 16
new_population = []

for i in range(0, no_first_pop):
    rd.shuffle(t)
    ax = list(t)
    new_population.append(ax)


def choice_for_crossover(pop, no_crossover):
    pop_chosen = []
    len_tours = [tour_length(m, os) for os in pop]
    for j in range(0, len(pop)):
        max_fitness_idx = len_tours.index(min(len_tours))
        pop_chosen.append(pop[max_fitness_idx])
        len_tours[max_fitness_idx] = 9999999999
    return pop_chosen[:no_crossover]


chosen_pop = choice_for_crossover(new_population, no_for_crossover)

def crossover(parents, offspring_size):
    offspring=[]
    for i in range(0, offspring_size):
        chrom = [0 for j in range(0, num_towns)]
        offspring.append(chrom)
    for k in range(0, int(offspring_size/2)):
        p_1 = rd.randint(0, no_for_crossover-1)
        p_2 = rd.randint(0, no_for_crossover-1)
        c_point = rd.randint(0, len(parents[1]))
        offspring[k] = parents[p_1][:c_point]
        offspr_1 = [x for x in parents[p_2] if not x in offspring[k]]
        offspring[k] += offspr_1
        offspring[offspring_size-k-1] = parents[p_2][:c_point]
        offspr_2 = [x for x in parents[p_1] if not x in offspring[offspring_size-k-1]]
        offspring[offspring_size-k-1] += offspr_2
    return offspring


def mutation(offspring_crossover, p_mute, offspring_size):
    for idx in range(0, offspring_size):
        pr = rd.uniform(0, 1)
        if pr < p_mute:
            m_point1 = rd.randint(0, num_towns - 1)
            m_point2 = rd.randint(0, num_towns - 1)
            pom = offspring_crossover[idx][m_point1]
            offspring_crossover[idx][m_point1] = offspring_crossover[idx][m_point2]
            offspring_crossover[idx][m_point2] = pom
        return offspring_crossover

print(" -----------pop--------------")
for i in range(0, no_first_pop):
    print(new_population[i], "%8.3f" % tour_length(m, new_population[i]))
print(" -----------pop-chosen--------")
chosen_pop = choice_for_crossover(new_population, no_for_crossover)
for i in range(0, no_for_crossover):
    print(chosen_pop[i], "%8.3f" % tour_length(m, chosen_pop[i]))
off = crossover(chosen_pop, no_for_crossover)
print("------potomkowie---------")
for i in range(0, no_for_crossover)
    print(off[i], "%8.3f" % tour_length(m, off[i]))
off = mutation(off, p_mute, no_for_crossover)
print("----po mutacji----")
for i in range(0, no_for_crossover):
    print(off[i], "%8.3f" % tour_length(m, off[i]))
