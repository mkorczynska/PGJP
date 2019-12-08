from functools import reduce

names = ['Jan', 'Staszek', 'Marek', 'Ignacy', 'Zygmunt']
hours = [168, 176, 142, 154, 120]
h_wage = [30, 22, 28, 34, 58]
result = [x for x in list(zip(names, list(map(lambda x, y: x * y, hours, h_wage))))
          if x[1] > (reduce(lambda x, y: x + y, wyplaty)) / len(wyplaty)]
