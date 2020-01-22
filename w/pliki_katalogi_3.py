import os
from collections import Counter

# path = os.getcwd()
os.chdir("C://Users/HP ENVY/Documents/PycharmProjects")
folder = input("Podaj nazwe folderu:")
path = os.path.join(os.getcwd(), folder)
print(path)
names = []

for root, dirs, files in os.walk(path):
    names += files

for name, i in Counter(names).items():
    if i != 1:
        print(name, i)
