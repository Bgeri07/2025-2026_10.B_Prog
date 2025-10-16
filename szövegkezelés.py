import random
# lebegőpontos - float - tört 
a = 1.25
b = float(input("adjon meg egy tizedes törtet:"))

print(b*4)

#generáljon ki [1,9[ közötti tört számot 2 tizedesjegyere 
#pl. 1.36, 2.3

#c = random.randint(100,999)/100
c = random.random() #]0,1[
print(round(c,2))

#hf megcsinálni ezt a feladatot

#szövegkezelés
szöveg = input("adja meg a szöveget:")
print(szöveg)
print("szöveg hossza", len(szöveg)) # len= karakter szám
print("első karakter", szöveg[0])

#szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szöveg[0]
kod = ord(szöveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

a = chr(random.randint(97,122))
b = chr(random.randint(97,122))
c = chr(random.randint(97,122))
print(a,b,c)

#Kérje a felhasználó keresztnevét! Generáljon neki egy jelszót, 
# az első 3 karakterének ascii kódjának a szorzatát! Ha nincs név 3 jegyű, akkor kettő esetén a hossz értékét legyen a szorzat 3. tagja
# 1 esetén pedig a szám köbe legyen. 
# alma - 65 * 108 * 109
# Co - 67 *111 * 2 
# G  -71 * 71 *71 

