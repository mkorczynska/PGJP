try:
    file = open("lista.txt", 'r+')
    print(open("lista.txt", 'r+').read())
except IOError:
    file = open("lista.txt", 'w')
students = []
t = ''
while t != 'K':
    t = input("Podaj liste studentow: [koniec: K ]")
    students.append(t)
students = students[:len(students)-1]
if file.mode == 'w':
    for line in students:
        file.write(line + '\n')
else:
    file.seek(0, 2)
    for line in students:
        file.write(line + '\n')
file.close()
