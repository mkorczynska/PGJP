import os
import fnmatch

folder = input("Podaj nazwe folderu:")
path = os.path.join(os.getcwd(), folder)
print(path)
text = input("Podaj tekst:")

for root, dirs, files in os.walk(path):
    for f in files:
        if fnmatch.fnmatch(f, f"*{text}"):
            print(f)
