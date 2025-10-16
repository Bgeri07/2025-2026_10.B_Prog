import math 
import random 
#Téglalap kerület, terület
a = 5
b = 4
terület = a * b
kerület = 2*a+b

print("Kerülte:"+ str (kerület))
print("Területe:"+ str (terület))

#Kör kerület, terület 
r = 4
pi = math.pi
Kerület = 2 * r * pi
Terület = pi * r ** 2 

print("Kör területe:" + str(Kerület))
print("Kör területe:"+str (Terület))

#Háromszög kerület, terület
a = 5
b = 6
c = 7 
s = kerület / 2 
terület = math.sqrt(s*(s - a)*(s - b)*(s - c))
kerület = a+b+c
 
print("Háromszög területe:"+ str(terület))
print ("Háromszög kerület"+ str(kerület))

# háromszög magassága
magasság = terület * 2 / a 
print("Magasság:"+ str(magasság))


# nég kiíratás 
Vezetéknév = str(input("Vezetéknév:"))
Keresztnév = str(input("Keresztnév:"))

print(Vezetéknév, Keresztnév)

#páros vagy nem páros? 
szám = int(input("Szám:"))
if(szám % 2 == 0):
    print("páros")
else: 
    print("páratlan")

#segítség az osztályfőnöknek
Érdemjegy = int(input("Éredemjegy:"))
if Érdemjegy == 1:
    print("elégtelen")

elif Érdemjegy == 2: 
    print("elégséges")

elif Érdemjegy == 3:
    print("Közepes")

elif Érdemjegy == 4:
    print("jó")

elif Érdemjegy == 5 :
    print("jeles")

#Víz hőfok
víz = int(input("víz hőfok:"))

if víz  >0 <100:
    print("folyékony")

elif víz >=100: 
    print("gáz")

else:
    print("szilárd")

#Szerkeszthetőe a háromszög 
a = int(input("Első szám:"))
b = int(input("Második szám:")) 
c = int(input("Harmadik szám:"))

if(a+b > c and a+c > b and b+c > a): 
    print("Szerkeszthető")
else: 
    print("Nem szerkeszthető")

#hőfok átválltás
fahrenheit = int(input("fahrenheit hőfok= "))
a = 32 
celsius = (fahrenheit - 32)*5 / 9 
print("Celsius= "+ str(celsius))


#most fordítva
celsius = int(input("celsius hőfok="))
a = 32
fahrenheit = celsius*9 / 5 + 32
print("fahrenheit="+str(fahrenheit))

#idő
másodperc = int(input("Másodperc"))
óra = másodperc // 3600
maradék_másodperc = másodperc % 3600
perc = maradék_másodperc // 60
másodperc_végső = maradék_másodperc % 60
print(óra, "óra,", perc, "perc,", másodperc_végső, "másodperc")
