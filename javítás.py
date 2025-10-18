import math
import random

szám = random.randint(0,9)
print(szám)
if(szám== 1 or szám ==6): 
    print("labda")
elif(szám== 2 or szám ==7):
    print("ceruza")
elif(szám== 3 or szám ==8):
    print("színes papír")
elif(szám == 1 or szám ==6):
    print("bicikli")
else: 
    print("nem nyert")

#2. feladat

óra= int(input("óra:"))
hét = óra// 168
nap = (hét * 168) // 24 
óra2 = (óra - hét * 168) - nap * 24

print(hét, "hét", nap ,"nap", óra2,"nap")

#3. feladat 

szám = random.randint(100, 999)
print("Generlát 3 jegyű szám:", szám)
első = szám /100
második = (szám - első * 100) // 10
harmadik = szám % 10

if(első **3 + második **3 + harmadik **3== szám ):
    print("jó") 
else:
    print("nem jó")

# 4.feladat 

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
print("számok:", a,b,c )
if(a != 0 and b !=0 and c !=0):
    harmonk= 3 / (1/a + 1/b + 1/c)
elif(a == 0 and b != 0 and c !=0 ):
    harmonk= 2 / (1/b + 1/c)
elif(a != 0 and b == 0 and c !=0 ):
    harmonk= 2 / (1/a + 1/c)
elif(a != 0 and b != 0 and c ==0 ):
    harmonk= 2 / (1/a + 1/b)
    
elif(a != 0 and b == 0 and c ==0 ):
    harmonk = 2 / (1/a)
elif(a == 0 and b != 0 and c ==0 ):
    harmadik =2 / (1/b)
elif(a == 0 and b == 0 and c !=0 ):
     harmadik =2/ (1/c)
else: 
    print("nincs megoldás")
print("harmónikus közép:", round(harmonk,3))