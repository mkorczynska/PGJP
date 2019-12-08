from random import choice

numbers = set()

while len(numbers) < 6:
    numbers.add(choice(range(1, 50)))
numbers = sorted(numbers)

print("Posortowane:")
for x in numbers:
    print(x, end=" ")
