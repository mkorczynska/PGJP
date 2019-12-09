roman_num = input("Podaj liczbę w postaci rzymskiej:")
print("Liczba", roman_num, "to:", end=" ")
roman_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
              "V": 5, "IV": 4, "I": 1}
r = list(roman_dict.keys())
lr = 0

while len(roman_num) != 0:
    for i in r:
        if roman_num.find(i) == 0:
            lr += roman_dict[i]
            if len(i) == 1:
                roman_num = roman_num[roman_num.find(i) + 1:]
            else:
                roman_num = roman_num[roman_num.find(i) + 2:]
print(lr)
