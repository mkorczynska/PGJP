import math

print("Wspolczynniki rownania kwadratowego:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a == 0:
    print("To nie jest równanie kwadratowe.")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b-(math.sqrt(delta)))/(2*a)
        x2 = (-b + (math.sqrt(delta))) / (2 * a)
        print("Dwa rozwiązania rzeczywiste: \nx1 = ", x1, "\nx2 = ", x2)
    elif delta == 0:
        x0 = (-b/2)*a
        print("Jedno rozwiązanie rzeczywiste: \nx =", x0)
    else:
        print("Brak rozwiązan w zbiorze liczb rzeczywistych.")
