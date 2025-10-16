# Három szám bekérése a felhasználótól
a = float(input("Add meg az első oldalt: "))
b = float(input("Add meg a második oldalt: "))
c = float(input("Add meg a harmadik oldalt: "))

# Ellenőrizzük, hogy a háromszög egyáltalán létezhet-e
if a + b > c and a + c > b and b + c > a:
    print("\nEz egy létező háromszög.")
    
    # Rendezés a derékszög ellenőrzéséhez (legnagyobb oldal legyen 'c')
    oldalak = sorted([a, b, c])
    x, y, z = oldalak  # z lesz a legnagyobb oldal

    # 1. Derékszögű-e?
    if abs(z**2 - (x**2 + y**2)) < 1e-9:  # kis eltérés engedélyezve lebegőpontos számok miatt
        print("→ Derékszögű háromszög.")
    else:
        print("→ Nem derékszögű háromszög.")

    # 2. Egyenlő szárú-e?
    if a == b or b == c or a == c:
        print("→ Egyenlő szárú háromszög.")
    else:
        print("→ Nem egyenlő szárú háromszög.")

    # 3. Szabályos-e?
    if a == b == c:
        print("→ Szabályos (egyenlő oldalú) háromszög.")
    else:
        print("→ Nem szabályos háromszög.")

else:
    print("Ez a háromszög nem létezhet (nem teljesül a háromszög-egyenlőtlenség).")
