"""
ciklusok - ismétlés - loop
számlálós - for ciklusok 
Végig megy a megadott elemeken vagy intervallumon! 
for  elem in range(mettől, meddig , hányasával):
ismétő folyamat
tesztelős - While
for karakter in szöveg:
ismétendlő folyamat
"""



import math
import random as r
for i in range(1,11,1):
    print(i, end=" ")
print()

for i in range(0,19,2):
    print(i, end=" ")

szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter, end = ",")
    print()
# szoveg[0]
# szoveg[1]
# szoveg[2]
for index in range(0, len(szoveg)-1, 1):
    print(szoveg[index]+",",end= "")
print(szoveg[-1])

print()

for i in range(28,51,4):
    print(i,end=" ")

print()

for i in range(10,0,-1):
    print(i, end=" ")
print()
# kalapács visszafele első megoldás
for i in range(len(szoveg)-1, -1, -1):
    print(szoveg[i], end="")

# második megoldás
n = len(szoveg)
for index in range(0, -n-1 ,1):
    print(szoveg[n-index-1],end="")
print()




# írassa ki a szöveget az helyével társítva! (1k 2 a 3l 4a 5p 6á 7c 8s)
# be : kalapács
# ki : 1k 2a 3l ....
for index in range(0, n , 1):
    print(str(index+1)+szoveg[index],end=" ")
print()
# írasson ki 5 db véletelen karakter a szövegből

for db in range(0,5,1):
    szam =r.randint(0,n-1)
    print(szoveg[szam], end="")
print()


#HF 17-21
n= len(szoveg)
for index in range(0, n , 1):
    print(szoveg[szam], end=" ")

