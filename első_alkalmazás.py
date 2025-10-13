# egy soros komment
"""
Több 
soros 
komment!!
"""

# crtl ü a kijelölt sor kommentelése

print("Szöveg kiírása")

print("Barta Gergely", end="@@@@")
print("10/B", end="-----")
print("2025.09.05", end="++++")
print()
print("alma", "körte", "szilva", "labda", sep="")

# jelenítsd meg a következő ábrát a terminálon!
# *
# **
# ***
# ****
print("*", "**", "***", "****", sep="\n")

print("*", end="\n")
print("**", end="\n")
print("***", end="\n")
print("****", end="\n")

# konkatenálás, concat, összefűzés - két szöveget fog összefűzni
összefűzés = "alma" + " körte"
print(összefűzés)

# többszörözés
soknev = "alma" * 5
print(soknev)

"""
 - szöveg - string - str 
 - szám - egész (integer - int)
 - lebegőpontos (float)
 - logika - True / False 
"""

aEgesz = 123
bTort = 34.23
szSzam = "12"
logikai = True

print("aEgesz:", aEgesz)
print("bTort:", bTort)
print("szSzam:", szSzam)
print("logikai:", logikai)

print("aEgesz * 2 =", aEgesz * 2)
print("aEgesz - 2 =", aEgesz - 2)
print("aEgesz * 2 =", aEgesz * 2)
print("aEgesz / 2 =", aEgesz / 2)

#div - egészrész, mod - modulurs(maradék)
#div // 
#mod - %%
print("a div 8", aEgesz // 8 )
print("a mod 8", aEgesz % 8)

print(int(szSzam)+aEgesz)
print(szSzam+str (aEgesz))

print(str(aEgesz)+szSzam)
print(aEgesz+int(szSzam))
15%7