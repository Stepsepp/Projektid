print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Tere  tulemast Aarde jahile")
print("Sinu missioon on leida aare saarelt üles")

Valik_1 = input('Sa\' jõudsid saarele, kuhu sa soovid minna? Kas "Vasakule" või "Paremale".').lower()

if Valik_1 == "vasakule":
    Valik_2 = input('Sa\' jõudsid jõe äärde, seal on väikene saareke keset jõge. Kas sa soovid "Oodata" oodata paati või "Ujuda" üle jõe.').lower()

    if Valik_2 == "oodata":
        print("Jõepaat tuli ja viis sind üle jõe.")
        Valik_3 = input("Sa jõudsid saarele, seal on maja 3 uksega: üks punane, üks kollane, üks sinine. Millise värvi sa valid?").lower()

        if Valik_3 == "punane":
            print("Sa leidsid aare! Palju õnne, võidad mängu.")
        elif Valik_3 == "kollane":
            print("Majast lendas välja draakon. Game Over.")
        elif Valik_3 == "sinine":
            print("Majast tuli välja nõid. Game Over.")
        else:
            print("Sa kukkusid auku. Game Over.")

    elif Valik_2 == "ujuda":
        print("Sind ründas mürgine madu. Game Over.")
    else:
        print("Sa kukkusid auku. Game Over.")

elif Valik_1 == "paremale":
    print("Sa sattusid sügavasse džunglisse. Game Over.")

else:
    print("Sa kukkusid auku. Game Over.")