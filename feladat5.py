print("Adj meg egy páros számot!")

szam = int(input("Szám: "))

while szam % 2 != 0:
    print("Ez nem páros szám!")
    szam = int(input("Adj meg egy páros számot: "))

print("Helyes! Páros számot adtál meg.")
