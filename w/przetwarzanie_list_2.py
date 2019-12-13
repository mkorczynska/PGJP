names = ['Jan', 'Adam', 'Karol', 'Jakub', 'Edmund']
hours = [168, 176, 142, 154, 120]
h_wage = [30, 22, 28, 34, 58]

result = [x for x in list(zip(names, list(map(lambda x, y: x * y, hours, h_wage))))]
payments = list(map(lambda x: x[0]*x[1], zip(hours, h_wage)))
mean = sum(payments)/len(payments)

for i in range(len(payments)):
    if payments[i] > mean:
        print(result[i])
