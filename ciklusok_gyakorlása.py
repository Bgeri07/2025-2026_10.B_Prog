# generálj ki 10 db egyjegyű nem nulla véletlen számot!
# írassa ki a számok összegét!
import math 
import random

osszeg = 0
for a in range(1,11,1):
    velSzam= random.randint (1,9)
    osszeg += velSzam
    print(velSzam, end = " ")
print()
print("Összeg:", osszeg)

# hány db páros véletlen számot generált ki 
# melyik a legnagyobb véletlen szám?