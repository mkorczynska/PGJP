from functools import reduce

factors_3 = [x for x in range(1, 33) if not x % 3]

no_even = list(filter(lambda x: x % 2, factors_3))

power_3 = list(map(lambda x: x**3, no_even))

mean = (reduce(lambda x, y: x+y, power_3))/len(power_3)

print("Liczby podzielne przez 3:")
for i in factors_3:
    print(i, end=" ")

print("\nLiczby podzielne przez 3, nieparzyste:")
for i in no_even:
    print(i, end=" ")

print("\nLiczby podzielne przez 3, nieparzyste, podniesione do sześcianu:")
for i in power_3:
    print(i, end=" ")

print("\nŚrednia:", mean)
