from random import randint
import classes

# Global variables
choices = []
lastChoice = -1
roll = -1

# Lisää kysymykset listaan
def AddChoice(txt = "", q = [], ending = False):
    global choices
    choices.append(classes.choice(txt, q, ending))

# Kysymysvalinnat
choices.clear()
#0
AddChoice("Heräät pimeästä huoneesta, huoneessa on kaksi ovea ulos.", [classes.question("1. Mene vasemmalla olevasta ovesta", 1, 0), classes.question("2. Mene oikealla olevasta ovesta", 2, 0)])
#1
AddChoice("Kävelet vasemmalla olevasta ovesat läpi, huoneessa on velho joka käy kimppuusi.", [classes.question("1. Taistele", 3, 7), classes.question("2. Pakene", 11, 0)])
#2
AddChoice("Kävelet oikealla olevasta ovesta läpi, huoneessa on zombie joka haluaa syödä sinut.", [classes.question("1. Taistele", 4, 7), classes.question("2. Pakene", 11, 0)])
#3
AddChoice("Päihitit velhon, nyt edessäsi on suora käytävä ja ovi.", [classes.question("1. Kävele käytävän päähän", 5, 0), classes.question("2. Mene ovesta", 6, 0)])
#4
AddChoice("Päihitit zombien, huoneen nurkassa on ilmastointikanava johon mahdut.", [classes.question("1. Yritä paeta ilmastointikanavoiden läpi", 8, 0), classes.question("2. Mene aikasemman huoneen vasemmasta ovesta sittenkin", 1, 0)])
#5
AddChoice("Kävelet käytävän päähän, yhtäkkiä yläpuoleltasi ilmastointikanavasta tippuu ihmissusi.", [classes.question("1. Taistele", 9, 11), classes.question("2. Pakene", 11, 0)])
#6
AddChoice("Menet ovesta, löydät laboraation jossa on tehty kokeita erilaisiin eläimiin. Eteesi ilmestyy mutatoitunut rotta.", [classes.question("1. Taistele", 7, 11), classes.question("2. Pakene", 11, 0)])
#7
AddChoice("Päihitit rotan, laboratooriossa on ilmastointikanava johon saatat mahtua.", [classes.question("1. Yritä paeta ilmastointikanavoiden läpi", 8, 0), classes.question("2. Palaa aikasempaan huoneeseen ja jatka käytävää pitkin", 5, 0)])
#8
AddChoice("Ilmastokanavat vievät ulos, löysit tiesi ulos tästä sokkelosta. Läpäisit pelin!", [classes.question()], True)
#9
AddChoice("Päihität ihmissuden ja jatkat käytävän päähän, käytävän päässä on ovi ulos. Löysit tiesi ulos tästä sokkelosta. Läpäisit pelin!", [classes.question()], True)
#10
AddChoice("Onneksi olkoon, löysit tiesi ulos tästä sokkelosta. Läpäisit pelin!", [classes.question()], True)
#11
AddChoice("Yrität paeta, mutta paikka on sokkelo ja sinulla ei ole paikkaa mihin paeta. Häviät pelin, yritä uudelleen.", [classes.question()], True)

# Printtaa kysymyksen muotoiltuna ja etenee seuraavaan kysymykseen käyttäjän syetteen perusteella
def Prompt(c = classes.choice("", [], False), lockRolling = False):
    global roll
    global lastChoice
    
    # Printtaa kysymyksen ja mahdollisen nopanheitto vaihtoehdon
    if (not c.questions and c.last == False):
        print("Cringe error")
    elif (c.last == True):
        print("\n{0}\n".format(c.prompt))
        return
    else:
        print("\n{0}".format(c.prompt))
        allowDiceRoll = False
        for q in c.questions:
            if (q.req <= 0):
                print(q.txt)
            else:
                print(q.txt, "[{0}]".format(q.req))
                allowDiceRoll = True
        if (lockRolling == False and allowDiceRoll == True):
            roll = int(input("Heitä noppaa? \n1. Kyllä\n2. Ei\n"))
            if (roll == 1):
                roll = randint(0,20)
                print("Heitit {0}.".format(roll))
            else:
                roll = -1
                print("Et heittänyt noppaa.")
        elif (allowDiceRoll == True):
            print("Tämän hetkinen nopanheitto on {0}.".format(roll))
        
        # Ottaa käyttäjän syetteen ja siirtyy seuraavaan kysymykseen sen perusteella
        chosen = int(input("Valitse: ")) - 1
        if (c.questions[chosen].req > 0):
            if (c.questions[chosen].req <= roll):
                lastChoice = c.questions[chosen].nextChoice
                Prompt(choices[c.questions[chosen].nextChoice])
            else:
                print("\nEt voi valita tuota valintaa! Nopanheittosi ei ole tarpeeksi iso numero.")
                Prompt(choices[lastChoice], True)
        else:
            lastChoice = c.questions[chosen].nextChoice
            Prompt(choices[c.questions[chosen].nextChoice])

# Ensimmäinen kysymys
lastChoice = 0
Prompt(choices[0])