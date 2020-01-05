import matplotlib.pyplot as plt
import random as rd

# FUNKCJE ------------------------------


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


def choice_for_crossover(pop, no_crossover):
    pop_chosen = []
    len_tours = [tour_length(m, os) for os in pop]
    for j in range(0, len(pop)):
        max_fitness_idx = len_tours.index(min(len_tours))
        pop_chosen.append(pop[max_fitness_idx])
        len_tours[max_fitness_idx] = 9999999999
    return pop_chosen[:no_crossover]


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


def display_path(path, cities):
    wspx, wspy = zip(*cities)

    for i in range(len(path) - 1):
        plt.plot(
            (wspx[path[i]], wspx[path[i + 1]]),
            (wspy[path[i]], wspy[path[i + 1]]),
            color="r"
        )
        plt.scatter(wspx, wspy)
        for j, city in enumerate(cities):
            plt.annotate(j, city)
    plt.show()


towns = [(30, 70), (50, 60), (30, 50), (0, 40), (50, 20), (30, 0), (30, 20), (40, 30), (60, 30)]
m = cartesian_matrix(towns)
no_first_pop = 16
new_population = []
t = [0, 8, 3, 2, 1, 5, 6, 7, 4]
no_for_crossover = 10
p_mute = 0.5

# losowanie populacji poczatkowej (16 drog)
for i in range(0, no_first_pop):
    rd.shuffle(t)
    first = t[0]
    ax = list(t)
    ax.append(first)
    new_population.append(ax)

print("Populacja początkowa: ")
for i in range(len(new_population)):
    print(new_population[i], "%8.3f" % tour_length(m, new_population[i]))

for j in range(len(new_population)):
    new_population[j].pop()

for i in range(10):
    # wybor nalepszych 10 drog
    chosen_pop = choice_for_crossover(new_population, no_for_crossover)
    # losowanie par rodzicow i krzyzowanie
    off = crossover(chosen_pop, no_for_crossover)
    # mutacja
    m_off = mutation(off, p_mute, no_for_crossover)
    # wybor szesciu najlepszych dzieci
    best_off = choice_for_crossover(m_off, 6)
    # wybor szesciu najlepszych rodzicow
    best_par = choice_for_crossover(chosen_pop, 6)
    new_population = best_off+best_par

for j in range(len(new_population)):
    first_elem = new_population[j][0]
    new_population[j].append(first_elem)

print("Populacja końcowa: ")
for i in range(len(new_population)):
    print(new_population[i], "%8.3f" % tour_length(m, new_population[i]))

best = choice_for_crossover(new_population, 1)
display_path(best[0], towns)
