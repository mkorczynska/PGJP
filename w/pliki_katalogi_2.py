import os

# path = os.getcwd()
os.chdir("C://Users/HP ENVY/Documents/PycharmProjects")
folder = input("Podaj nazwe folderu:")
path = os.path.join(os.getcwd(), folder)
print(path)
max_size = 0
min_time = float("+inf")
f_max = 0
f_old = 0
for root, dirs, files in os.walk(path):
    for f in files:
        stats = os.stat(os.path.join(root, f))
        if stats.st_size>max_size:
            max_size = stats.st_size
            f_max = f
        if stats.st_ctime < min_time:
            min_time = stats.st_ctime
            f_old = f

print(f"Najstarszy: {f_old}")
print(f"Najdluzszy: {f_max}")

