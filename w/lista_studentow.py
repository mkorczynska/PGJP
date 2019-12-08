class Student:
    name = " "
    surname = " "
    grade = " "


students = []
no = 0

while True:
    sn = input('Podaj nazwisko studenta nr %i (ENTER=koniec):' % (no + 1))
    if not sn:
        break
    students.append(Student())
    students[no].surname = sn
    students[no].name = input('Podaj imię studenta nr %i > ' % (no + 1))
    students[no].grade = float(input('Podaj ocene studenta nr %i > ' % (no + 1)))
    no += 1
print('%-4s%-14s%-10s%7s' % ('L.p', 'Nazwisko', 'Imię', 'Ocena'))
mean = 0
for student in students:
    mean += student.grade
    print("%3i.%-14s%-10s%7.1f" % (students.index(student) + 1, student.surname, student.name, student.grade))
print("Średnia ocen studentów wynosi: %.2f" % (mean / len(students)))
