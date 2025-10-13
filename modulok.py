import math 
import random 

a = 2
gyöka = math.sqrt(a)
print("gyök" , str(a) ,  "=", gyöka)

felkerekít = math.ceil(gyöka)
print("felsőegészrész:", felkerekít)

lekerekít = math.floor(gyöka)
print("alsóegészrész:", lekerekít) 

kerekítés = round(gyöka,2)
print("kerekítés 2 tizedes jegyre", kerekítés)

hatványozás1 = math.pow(gyöka, 2)
print("gyöka négyzete: ", hatványozás1)

alap = 2 
kitevő = 5
#hatványozás2 = math.pow(alap, kitevő)
hatványozás2 = alap ** kitevő 

print(alap, "^",kitevő, "=",hatványozás2)

vszám1 = random.randint(2,10)
print(vszám1)