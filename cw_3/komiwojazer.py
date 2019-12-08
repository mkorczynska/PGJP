import numpy
import matplotlib.pyplot as plt

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
