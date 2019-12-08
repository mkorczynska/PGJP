import numpy
import matplotlib.pyplot as plt

towns = [(30, 70), (50, 60), (30, 50), (0, 40), (50, 20), (30, 0), (30, 20), (40, 30), (60, 30)]


def cartesian_matrix(coords):
    matrix = {}
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
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
t = [0, 8, 3, 2, 1, 5, 6, 7, 4]
print(t, "%8.3f" % tour_length(m, t))

wspx, wspy = zip(*cityList)
plt.scatter(wspx, wspy)
for j in range(len(t)):
    plt.annotate(j, cityList[t[j]])
plt.show()
