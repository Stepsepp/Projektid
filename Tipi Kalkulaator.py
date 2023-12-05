print("Tere tulemast arvutama tippi")
arve = float(input("Mis on arve summa €: "))
tip = int(input("Kui palju tippi soovid anda? Vali 10, 12 või 15: "))
inimesed = int(input("Mitu inimeste vahel tuleb arve jagada? "))
tippTuleksJätta = (tip / 100 * arve + arve) / inimesed
print(f"Iga inimese osa, arvestades tippi, on: {tippTuleksJätta:.2f} €")
