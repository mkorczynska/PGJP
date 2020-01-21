import os

folder = input("Podaj nazwe folderu:")
path = os.path.join(os.getcwd(), folder)
max_size = 0
min_time = float("+inf")

