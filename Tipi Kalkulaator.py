print("Tere tulemast arvutama tippi")
try:
    arve = float(input("Mis on arve summa €: "))
    tip = int(input("Kui palju tippi soovid anda? Vali 10, 12 või 15: "))

    # Kontrolli, kas sisestatud tipi protsent on kehtiv
    if tip not in [10, 12, 15]:
        raise ValueError("Palun vali tipi protsent ainult 10, 12 või 15.")

    inimesed = int(input("Mitu inimeste vahel tuleb arve jagada? "))

    # Kontrolli, et inimeste arv ei oleks negatiivne ega null
    if inimesed <= 0:
        raise ValueError("Inimeste arv peab olema positiivne ja suurem kui null.")

    tippTuleksJätta = (tip / 100 * arve + arve) / inimesed
    print(f"Iga inimese osa, arvestades tippi, on: {tippTuleksJätta:.2f} €")

except ValueError as ve:
    print(f"Viga: {ve}. Palun sisesta korrektseid väärtusi.")
except Exception as e:
    print(f"Viga: {e}. Midagi läks valesti.")
