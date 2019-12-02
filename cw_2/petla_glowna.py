import numpy

generations = int(input("number of generations: "))
pop_size = 10
size = 6
weights = [4, -3, 3.5, 5, -7, 4.2]
start_list = []
p_mute = 0.35

for j in range(pop_size):
    element = list(numpy.random.uniform(low=-4.0, high=4.0, size=size))
    start_list.append(element)
print("List of 10 lists:\n", *start_list, sep="\n")

for i in range(generations):
    dot_list = []
    for k in range(len(start_list)):
        dot = numpy.dot(weights, start_list[k])
        dot_list.append(dot)
    print("List of dot products: \n", dot_list)

    max_dots = []
    for l in range(6):
        maximum = max(dot_list)
        index = dot_list.index(maximum)
        max_dots.append(start_list[index])
        dot_list.remove(maximum)
    print("List of maximum dot products: ", *max_dots, sep="\n")

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
    start_list = new_pop

print("Last population: \n", *start_list, sep="\n")



