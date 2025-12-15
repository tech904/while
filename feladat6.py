import random

print("3-mal osztható számok:")

szamlalo = 0
db = 0

while szamlalo < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        db += 1
    szamlalo += 1

print("Ennyi darab 3-mal osztható szám volt:", db)
