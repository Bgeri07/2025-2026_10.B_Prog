"""
elöltesztelős ciklus, azaz while ciklus. 
nem tudtjuk hányszor fog lefutni, ismételni
akkor ismétel, ha a feltétel igaz

while(feltétel):
    utasítások(szekvencia)

"""

# generáljon véletlen számokat [0-10] között, amíg nullát nem kapunk!

import random 

vélszám = random.randint (0 , 10)
print(vélszám)
while(vélszám != 0 ):
    vélszám = random.randint (0 , 10)
    print(vélszám, end= " ")
print()


# kérjen be számokat!, addig amíg nullát nem adnak meg
összeg = 0 
darab = 0
szám = int(input("add meg a számot (0-nál kilép:)"))
# összeg += szám 
# darab += 1 
while (szám != 0): 
    összeg += szám
    darab += 1 
    szám = int(input("add meg a számot (0-nál kilép:)"))
    print(round(összeg / darab , 2))
    

# Adott egy szöveg. Adaj meg, hogy van-e benne x betű!
szöveg = input("írjon be egy szöveget:")






