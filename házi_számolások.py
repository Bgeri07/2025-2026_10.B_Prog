#sima módszer
#(házi)
a = 5 
b = 7
terület = a* b
kerület =2 *(a + b)

print(f"a téglalap oldalai: a = {a}, b = {b}")
print(f"a téglalap kerülete = {kerület}")
print(f"a téglalap területe = {terület}")

import math
r=15
kerület = 2*r*math.pi
terület = r**2 * math.pi

print(f"a kör sugara {r}")
print(f"a kör kerülete = {kerület}")
print(f"a kör területe = {terület}")



#választós módszer
#szimpla gyakorlás

while True: 
    input("Nyomj enter a választások mejelenítéséhez! ")
    print("Válasz a számítások közül")
    print("1 - A téglalap kerület, területe")
    print("2 - A kör kerülete, területe")
    print("3 - Összeadás")
    print("4 - Kivonás")
    print("5 - Kilépés")

    választás = input("írd be az 1-es számot ha a téglalap kerületét, területét számolnád ki 2-es számot ha a kör kerületét, területét szeretnéd kiszámolni , 3-as számot ha össze szeretnél adni 4-es számot ha kiszeretnél vonni, 5-ös számot ha kilépnél.")

    if választás =="1":
 
        a = float(input("Írd be az a oldal hosszát (a): "))
        b = float(input("Írd be a b oldal hosszát (b):") )

        kerület = 2 *(a+b)
        terület = a*b 
        print(f"a téglalap oldalai, a = {a}, b = {b}") 
        print(f"a téglalap kerülete {kerület}") 
        print(f"a téglalap területe {terület}")

    elif választás =="2":

        r = float(input("A kör sugarát írd be! (r)"))
        import math
        kerület = 2*r * math.pi
        terület = r**2 *math.pi

        print(f"a kör sugar {r}")
        print(f"a kör területe{terület}")
        print(f"a kör kerülete{kerület}")

    elif választás =="3":
        a = float(input("Írd be az első számot!: "))
        b = float(input("Írd be a második számot!: "))
        összeg = a + b 
        print(f"A számok: a = {a}, b = {b}")
        print(f"Az eredmény: {összeg}")


    elif választás =="4":
        a= float(input("Írd be az első számot!: "))
        b= float(input("Írd be a második számot!: "))
        különbség = a - b
        print(f"A számok: a = {a}, b = {b}")
        print(f"Az eredmény: {különbség}")


    elif választás =="5": 
        print("Kilépés")
        break

    else: 
        print("HIBA")

