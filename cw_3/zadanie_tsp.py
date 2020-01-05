import matplotlib.pyplot as plt
import random as rd

towns = [(30, 70), (50, 60), (30, 50), (0, 40), (50, 20), (30, 0), (30, 20), (40, 30), (60, 30)]


def cartesian_matrix(coordinates):
    matrix = {}
    for i, (x1, y1) in enumerate(coordinates):
        for j, (x2, y2) in enumerate(coordinates):
            dx, dy = x1 - x2, y1 - y2
            dist = (dx * dx + dy * dy) ** 0.5
            matrix[i, j] = dist
    return matrix


def tour_length(matrix, tour):
    total = 0
    num_cities = len(tour)
    for i in range(num_cities):
        j = (i + 1) % num_cities
        city_i = tour[i]
        city_j = tour[j]
        total += matrix[city_i, city_j]
    return total


m = cartesian_matrix(towns)
print("M:", m)

t = [0, 8, 3, 2, 1, 5, 6, 7, 4]
print(t, "%8.3f" % tour_length(m, t))

wspx, wspy = zip(*towns)
plt.scatter(wspx, wspy)
for j in range(len(t)):
    plt.annotate(j, towns[t[j]])

for i in range(len(t)-1):
    lines = plt.plot((wspx[i], wspx[i+1]), (wspy[i], wspy[i+1]))
    plt.setp(lines, color='r', linewidth=1.5)
plt.show()

no_first_pop = 16
new_population = []

for i in range(0, no_first_pop):
    rd.shuffle(t)
    ax = list(t)
    new_population.append(ax)

print("Populacja początkowa: ")
for i in range(len(new_population)):
    print(new_population[i], "%8.3f" % tour_length(m, new_population[i]))


def choice_for_crossover(pop, no_crossover):
    pop_chosen = []
    len_tours = [tour_length(m, os) for os in pop]
    for j in range(0, len(pop)):
        max_fitness_idx = len_tours.index(min(len_tours))
        pop_chosen.append(pop[max_fitness_idx])
        len_tours[max_fitness_idx] = 9999999999
    return pop_chosen[:no_crossover]


no_for_crossover = 10
chosen_pop = choice_for_crossover(new_population, no_for_crossover)

print("Wybrane: ")
for i in range(len(chosen_pop)):
    print(chosen_pop[i], "%8.3f" % tour_length(m, chosen_pop[i]))


def crossover(parents, offspring_size):
    offspring = []
    for i in range(0, offspring_size):
        chrom = [0 for j in range(0, len(towns))]
        offspring.append(chrom)
    for k in range(0, int(offspring_size / 2)):
        p_1 = rd.randint(0, no_for_crossover - 1)
        p_2 = rd.randint(0, no_for_crossover - 1)
        c_point = rd.randint(0, len(parents[1]))
        offspring[k] = parents[p_1][:c_point]
        offspr_1 = [x for x in parents[p_2] if x not in offspring[k]]
        offspring[k] += offspr_1
        offspring[offspring_size - k - 1] = parents[p_2][:c_point]
        offspr_2 = [x for x in parents[p_1] if x not in offspring[offspring_size - k - 1]]
        offspring[offspring_size - k - 1] += offspr_2
    return offspring


off = crossover(chosen_pop, no_for_crossover)
print("Potomkowie")
for i in range(0, no_for_crossover):
    print(off[i], "%8.3f" % tour_length(m, off[i]))


def mutation(offspring_crossover, p_m, offspring_size):
    for idx in range(0, offspring_size):
        pr = rd.uniform(0, 1)
        if pr < p_m:
            m_point1 = rd.randint(0, len(towns) - 1)
            m_point2 = rd.randint(0, len(towns) - 1)
            pom = offspring_crossover[idx][m_point1]
            offspring_crossover[idx][m_point1] = offspring_crossover[idx][m_point2]
            offspring_crossover[idx][m_point2] = pom
        return offspring_crossover


p_mute = 0.5
m_off = mutation(off, p_mute, no_for_crossover)
print("Potomkowie po mutacji: ")
for i in range(0, no_for_crossover):
    print(m_off[i], "%8.3f" % tour_length(m, m_off[i]))


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
