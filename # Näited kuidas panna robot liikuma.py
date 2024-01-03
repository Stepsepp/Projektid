# Näited kuidas panna robot liikuma enda soovide järgi ja kasutame enda loodud koodiplokki def jne
# Link https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Näidis kood 1
def turn_around():
    turn_left()
    turn_left()  
move()
move()
turn_around()
move()
move()
turn_around()


# Näidis kood 2

# Antud  esitatud koodis defineerime funktsiooni turn_right(), mis pöörab robotit paremale,
# tehes kolm vasakpööret järjest. Seejärel kasutate seda funktsiooni, et joonistada ruut, kasutades turn_left(), move() ja turn_right() funktsioone.

Siin on koodi sammude selgitus:

turn_left(): # Pöörab robotit esimese ruudu nurga poole (vasakule).
 move(): # Liigutab robotit edasi.
 turn_right(): # Pöörab robotit paremale, kasutades enne defineeritud turn_right() funktsiooni (teeb kolm vasakpööret).
 move(): # Liigutab robotit edasi.
 turn_right(): # Pöörab robotit paremale.
 move(): # Liigutab robotit edasi.
 turn_right(): # Pöörab robotit paremale.
 move(): # Liigutab robotit edasi.
 # Selle tulemusena peaks robot liikuma nelja sammu võrra,
 # pöörama end paremale, liikuma veel nelja sammu võrra, pöörama end taas paremale, liikuma ja nii edasi, moodustades ruudu.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Link 2 https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

 turn_right(): # Funktsioon, mis pöörab robotit paremale, tehes kolm vasakpööret järjest.
 koodis kasutatakse for tsüklit, et kutsuda kuus korda järjest funktsiooni jump().
 Iga tsükli samm tekitab ühe hüppe, sest jump() funktsioon sisaldab liikumist ja pöördeid, nagu eelnevalt selgitatud.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): 
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

#  esitatud koodis kasutatakse while tsüklit, et teha hüppeid seni, kuni number_of_hurdles on suurem kui 0.
# Iga tsükli iteratsioon kutsub välja funktsiooni jump(), vähendab seejärel number_of_hurdles väärtust ühe võrra ja väljastab sellejärel selle uue väärtuse.

# Siin on koodi töö selgitus:

jump(): # Funktsioon, mis teeb ühe hüppe.
 number_of_hurdles -= 1: # Vähendab number_of_hurdles väärtust ühe võrra.
 print(number_of_hurdles): # Väljastab uue väärtuse pärast hüpet.
 # Tsükkel jätkub seni, kuni number_of_hurdles jõuab väärtuseni 0.
 # Seega tehakse jump() tsükkel kuus korda (arvestades, et alustatakse väärtusega 6)
 # ja iga kord vähendatakse number_of_hurdles väärtust, kuni see jõuab 0-ni.
 print(number_of_hurdles) # käsk annab teile tagasisidet selle kohta, kui mitu takistust on veel hüpata.
    
    number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# Link 3 https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
    
# esitatud koodis kasutatakse while tsüklit, et hüpata seni, kuni robot ei ole veel eesmärgini jõudnud.
#  at_goal() on funktsioon, mis tagastab tõeväärtuse (True või False), näidates, kas robot on eesmärgini jõudnud või mitte.
# Tsükli sees kutsutakse välja funktsioon jump().

#Siin on koodi selgitus:

while not at_goal(): # Tsükkel jätkub seni, kuni at_goal() tagastab False (robot ei ole veel eesmärgini jõudnud).
jump(): # Iga tsükli iteratsioon kutsub välja funktsiooni jump(), mis tõenäoliselt teeb roboti liikumise ja pöörded.
# Tsükkel jätkub, kuni at_goal() tagastab True (robot on jõudnud eesmärgini).
# See on efektiivne viis kirjutada koodi, kui soovite, et robot liiguks eesmärgini seni, kuni see jõuab sinna.

# Hurdle 4 (saab valida browseris )


