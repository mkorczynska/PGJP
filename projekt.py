kapital_poczatkowy = 400
import pandas as pd

data = {"Piwo": ["Porter", "Pszeniczne", "Pale Ale", "Lager", "Pilzner", "Koźlak", "Stout"],
        "kod binarny": ["000", "001", "010", "011", "110", "111", "100"],
        "popyt": [6, 5, 7, 7, 4, 5, 2, 1],
        "popyt sok": [1, 5, 8, 8, 1, 7, 2, 1]}
df = pd.DataFrame(data)
print(df)

