# Bugs:
# 
# 
# 
# 
# =======================================================================================================================================
# Notes:
# Daekrahm Village, add something for choosing not to follow the footprints
# 
#
#
# =======================================================================================================================================
# Imports:
# =======================================================================================================================================
import os
import random
import time
bootObtained = False
phraseObtained = False
yResponses = ["yes","ye","yeah","y","yea","ok","k","kk","okay","okie","oki","correct","corrct","si","sure"]
nResponses = ["no","n","nah","nein","non","pass","never"]

# =======================================================================================================================================
# Health and Damage Stat Variables
# =======================================================================================================================================
characterHealth = 10
characterDamage = 2
frostGiantHealth = 15
frostGiantDamage = 3
spiderHealth = 5
spiderDamage = 2
boy1Damage = 1
boy2Damage = 2
boy3Damage = 3
gunDamage = 10

# =======================================================================================================================================
# Start of Game Introduction
# =======================================================================================================================================
time.sleep(1)
print("""
    INTRODUCTION:

    Welcome to The Citadel! Founded back in 1302 The Citadel is home to many residents from many lands
    who have all come here to start a new life and enhance their living. The days are long and the nights
    are longer, food is sparse, but the Citadens make do with what they have. 
    """)
time.sleep(1)#Set to 15 seconds once done
print("To proceed, please head over to The Traveller! He can normally be found under the Old Oak Tree!")
time.sleep(1)
loadingTravellerChoice = input("Would you like to visit The Traveller? - ")

# =======================================================================================================================================
# Location Directions
# =======================================================================================================================================
def locationDirections():
    if bootObtained == True and phraseObtained == True:
        print()
        print("Where would you like to go?")
        print(" 3 - Daekrahm Village")
        print()
    elif bootObtained == True and phraseObtained == False:
        print()
        print("Where would you like to go?")
        print(" 2 - Lockwood Village")
        print(" 3 - Daekrahm Village")
        print()
    elif bootObtained == False and phraseObtained == True:
        print()
        print("Where would you like to go?")
        print(" 1 - Oar's Rest")
        print(" 3 - Daekrahm Village")
        print()
    else:
        print()
        print("Where would you like to go?")
        print(" 1 - Oar's Rest")
        print(" 2 - Lockwood Village")
        print(" 3 - Daekrahm Village")
        print()
    choiceOne = input("- ")
    if choiceOne == "1":
        loadingOarRest()
    elif choiceOne == "2":
        loadingLockwoodVillage()
    elif choiceOne == "3":
        loadingDaekrahmVillage()
    else:
        locationDirections()

# =======================================================================================================================================
# Second Location Directions
# =======================================================================================================================================
def secondLocationDirections():
    print("1 - Bryxton Town")
    print("2 - Azalea Village")
    print("3 - The Snowy Mountains")
    print()
    choiceTwo = input("- ")
    if choiceTwo == "1":
        loadingBryxtonTown()
    elif choiceTwo == "2":
        loadingAzaleaVillage()
    elif choiceTwo == "3":
        loadingTheSnowyMountains()
    else:
        secondLocationDirections()

# =======================================================================================================================================
# The Traveller (CONTINUED)
# =======================================================================================================================================
def travellerContinued():
    print("    It is lovely to meet you " + characterName + "!")
    time.sleep(0.5)
    print()
    startQuest = input(characterName + " do you accept my quest? - ")
    if startQuest.lower() in yResponses:
        time.sleep(0.5)
        print()
        print("Excellent! Let's get this started!")
        locationDirections()
    else:
        print("I am sorry to hear that, please, excuse me")

# =======================================================================================================================================
# The Traveller
# =======================================================================================================================================
def theTraveller():
    global characterHealth
    characterHealth = 10
    print("""
    THE TRAVELLER:

    Greetings young explorer! I heard you were new around here, I hope you are finding your way
    around The Citadel alright. The people here are very kind, I am sure they would be willing to
    help you if you got lost or confused! Anyway, enough of the introductions, I have a small 
    problem, but you see, I am not an explorer, I was wondering if you would be able to help me?
    In fact, let's make this a bit more professional, what should I call you explorer?
    """)
    time.sleep(1)#Set to 15 seconds once done
    global characterName
    characterName = input("- ")
    print()
    travellerContinued()

# =======================================================================================================================================
# Boot Phrase Traveller
# =======================================================================================================================================
def bootPhrase():
        if bootObtained == True and phraseObtained == True:
            print("1 - I have the boot")
            print("2 - I have the phrase")
            print("3 - Continue Locations")
            rChoice = input("- ")
            if rChoice == "1":
                time.sleep(.05)
                print("""
    THE TRAVELLER: Oh wow! I haven't seen this in a while! This belonged to the Explorer I have
                   you looking for. My oh my, this has aged. But do you see how it is torn? It
                   is like something with brute force broke it. Now that you have found it, do
                   you think you could go find more information? It may help us track him down!
                   """)
                input("- ")
                print()
                bootPhrase()
            elif rChoice == "2":
                time.sleep(0.5)
                print()
                print("*Recites the Phrase to The Traveller*")
                print("""
    THE TRAVELLER: I have never heard that before! But that is actually helpful, we might have a 
                   hope at finding the Explorer with that! Keep going out to different locations
                   and see what you can find! Sound good?
                    """)
                input("- ")
                print()
                bootPhrase()
            elif rChoice == "3":
                print()
                locationDirections()
        elif bootObtained == True and phraseObtained == False:
            print("1 - I have the boot")
            print("2 - Continue Locations")
            rChoice = input("- ")
            if rChoice == "1":
                time.sleep(.05)
                print("""
    THE TRAVELLER: Oh wow! I haven't seen this in a while! This belonged to the Explorer I have
                   you looking for. My oh my, this has aged. But do you see how it is torn? It
                   is like something with brute force broke it. Now that you have found it, do
                   you think you could go find more information? It may help us track him down!
                   """)
                input("- ")
                print()
                bootPhrase()
            elif rChoice == "2":
                print()
                locationDirections()
        elif bootObtained == False and phraseObtained == True:
            print("1 - I have the phrase")
            print("2 - Continue Locations")
            rChoice = input("- ")
            if rChoice == "1":
                time.sleep(0.5)
                print()
                print("*Recites the Phrase to The Traveller*")
                print("""
    THE TRAVELLER: I have never heard that before! But that is actually helpful, we might have a 
                   hope at finding the Explorer with that! Keep going out to different locations
                   and see what you can find! Sound good?
                    """)
                input("- ")
                print()
                bootPhrase()
            elif rChoice == "2":
                print()
                locationDirections()
        elif bootObtained == False and phraseObtained == False:
            print("I have nothing")
            print("1 - Continue Locations")
            rChoice = input("- ")
            if rChoice == "1":
                print()
                locationDirections()
    
# =======================================================================================================================================
# The Traveller (RETURN)
# =======================================================================================================================================
def returnTraveller():
    print()
    print("You have arrived at: The Traveller")
    time.sleep(0.5)
    print("""
    THE TRAVELLER: Nice to see you again %s, how goes the exploring? Do you have anything for me?
    """ % (characterName))
    time.sleep(2)
    bootPhrase()

# =======================================================================================================================================
# Location One (Obtain Boot)
# =======================================================================================================================================
def oarRest():
    print()
    print("You have arrived at: Oar's Rest")
    time.sleep(0.5)
    print("""
    LOCATION:

    As you pace yourself through the hollow gates of Oar's Rest, the path beneath your feet softens, 
    the sounds of livestock and shouting pierce your ears. Slowly edging your way towards a derelict 
    cottage, a rocking chair creeks to reveal an Old Man. Layered with an old plaid shirt, suspenders
    way past his torso and a long, almost fatherly grey beard.
    """)
    time.sleep(1)#Set to 15 seconds once done
    print("""
    OLD MAN: Who goes there? This is ancient land, get off it quickly before you spoil the
             riches""")
    time.sleep(2)
    print("""
    %s: The Traveller sent me on a quest and provided me with different directions,
           so here I am. Who are you?""" % (characterName.upper()))
    time.sleep(2)
    print("""
    OLD MAN: They call me the Old Man. Probably because I am old and slowly dying, but they don't care.
             And he did did he? I'm guessing this "quest" of his is to try and find the Explorer, 
             am I right?""")
    time.sleep(3)
    yesChoice = input("- ")
    if yesChoice.lower() in yResponses:
        time.sleep(0.5)
        print("""
    OLD MAN: I thought so, up to no good again he is The Traveller. Ah well, here, this may be of
             use to you.""")
        global bootObtained
        bootObtained = True
        print()
        print("Old Boot has been obtained!")
        time.sleep(1)
    elif yesChoice.lower() in nResponses:
        print("""
    OLD MAN: Well, it was nice to see you, goodbye!""")

# =======================================================================================================================================
# Boot Obtained
# =======================================================================================================================================
    def bootHasObtained():
        print("""
    DECISION:

    1 - What does this boot do?
    2 - Em, has this been washed?
    3 - Sorry, I think this was a bad choice.
        """)
        bootChoice = input("- ")
        if bootChoice == "1":
            print("""
    OLD MAN: What you are currently holding is something that was found up some mountain a
             long time ago. No one knows what it is for though. Go back to The Traveller and
             inform him of what you have found!""")
            time.sleep(1)
            print()
            rtIN = input("Would you like to go back to the Traveller? - ")
            if rtIN in yResponses:
                returnTraveller()
            elif rtIN in nResponses:
                locationDirections()
        elif bootChoice == "2":
            print("""
    OLD MAN: Does it look like it has been washed? And more importantly does that look like
             mine? I do not know whether to take that as an insult or a compliment.""")
            bootHasObtained()
        elif bootChoice == "3":
            print("""
    OLD MAN: Fair enough, give the Travelled a slap for me will you?""")
            theTraveller()
    time.sleep(0.5)

    if bootObtained == True:
        bootHasObtained()
    elif bootObtained == False:
        theTraveller()

# =======================================================================================================================================
# Location Two (Obtain Phrase)
# =======================================================================================================================================
def lockwoodVillage():
    print()
    print("You have arrived at: Lockwood Village")
    time.sleep(0.5)
    print("""
    LOCATION:

    Bells toll loudly and the shouting of men and women as a gathering is pulled together in the
    village square. Children continue playing whilst the rest casually approach the center. Clouds
    start to gather above as the sun begins to set, however one girl playing with her siblings
    draws your attention to some specific words she is saying.
    """)
    time.sleep(1)#Set to 15 seconds once done
    print("""
    YOUNG GIRL: When the sun sets the clouds appear but beware of the monster upon high.""")
    time.sleep(2)
    print("""
    %s: The Traveller sent me on a quest and provided me with different directions,
           so here I am. Who are you?""" % (characterName.upper()))
    time.sleep(2)
    print("""
    YOUNG GIRL: My name is Lisa, I was born here with my siblings, our parents are very busy and
                not around much as they are in charge of the Village! The Traveller sent a note
                that we are to be expecting someone who is looking for the Explorer, is that you?""")
    time.sleep(3)
    choiceYes = input("- ")
    if choiceYes.lower() in yResponses:
        time.sleep(0.5)
        print("""
    YOUNG GIRL: Oh wow, an adventurer! I can't believe I get to meet one! This definitely is a rare
                occurence.""")
        global phraseObtained
        phraseObtained = True
        print()
        print("Phrase has been obtained!")
        time.sleep(1)
    elif choiceYes.lower() in nResponses:
        print("YOUNG GIRL: It was nice to see you " + characterName + ", but I need to go!")

# =======================================================================================================================================
# Phrase Obtained
# =======================================================================================================================================
    def phraseHasObtained():
        print("""
    DECISION:

    1 - What was that saying you just mentioned?
    2 - What game are you playing?
    3 - Excuse me little girl.
        """)
        bootChoice = input("- ")
        if bootChoice == "1":
            print("""
    YOUNG GIRL: Oh that! It's this old saying my mama tells me and my siblings, we don't exactly
                know what it means or where it came from, but our mama says it came from this old
                adventurer who went our adventuring and got lost down a hole in the middle of 
                nowhere, maybe go back to The Traveller and teach him of the phrase! 
                """)
            time.sleep(1)
            print()
            rtIN = input("Would you like to go back to the Traveller? - ")
            if rtIN in yResponses:
                returnTraveller()
            elif rtIN in nResponses:
                locationDirections()
        elif bootChoice == "2":
            print("""
    YOUNG GIRL: It's called ipp dipp, you get a pumpkin chunk and a bale of hay and the first person
                to get the pumpkin chunk to reach the floor through the hay wins!.""")
            phraseHasObtained()
        elif bootChoice == "3":
            print("""
    YOUNG GIRL: That's ok! Sorry I couldn't help more, maybe The Traveller can give you somewhere
                else to go!""")
            locationDirections()
    time.sleep(0.5)

    if phraseObtained == True:
        phraseHasObtained()
    elif phraseObtained == False:
        theTraveller()

# =======================================================================================================================================
# Location Three (Choice Path)
# =======================================================================================================================================
def daekrahmVillage():
    print()
    print("You have arrived at: Daekrahm Village")
    time.sleep(0.5)
    print("""
    LOCATION:

    As the water spits up from all the puddles beneath your feet, you find yourself amongst these cobweb riddened settlements,
    windows all smashed in, boarded up which could only be described as as dried out cloth. Making do with what they have
    available to them and not being as wealthy or profitable as the other villages and towns within their neighbouring
    vacinity.""")
    time.sleep(1)
    print("""
    *dog barks in the distance*""")
    time.sleep(2)
    print("""
    %s: What was that?""" % (characterName.upper()))
    time.sleep(2)
    print("""
    *dog barks again but louder*""")
    time.sleep(2)
    print()
    print("Do you approach?")
    time.sleep(1)
    choiceYes = input("- ")
    if choiceYes.lower() in yResponses:
        time.sleep(0.5)
        print("""
    DISCOVERY:

    As you approach the dog barking towards the back of the Village, you find large footprints in the snow beneath
    your feet, this snow coming from the mountains ahead. The dog seems unsettled and disturbed by these footprints.
    Where do you go next?
        """)
        secondLocationDirections()
    elif choiceYes.lower() in nResponses:
        print("""
    DECISION:

    You slowly turn your back to the dog and walk away.
            """)

def gunDeath():
    global gunDamage
    print("*a gun shot sounds from a nearby building, piercing your skull* - %s Health" % (gunDamage))
    global characterHealth
    characterHealth = characterHealth - gunDamage
    time.sleep(1)
    print("Your health is currently at: %s" % (characterHealth))
    time.sleep(1)
    print("%s has died." % (characterName))
    time.sleep(1)
    print()
# =======================================================================================================================================
# Location Four (Second Choice Path)
# =======================================================================================================================================
def bryxtonTown():
    print()
    print("You have arrived at: Bryxton Town")
    time.sleep(0.5)
    print("""
    LOCATION:

    Storm clouds gather above, doors slam shut with there locks being clasped together and shutters forgotten. Anyone who
    is anyone within this gruesome town is in all black, hoods and masks on, keeping themselves to themselves. The streets cobbled,
    and littered with unwanted children.""")
    time.sleep(1)
    print("""
    BOY ONE: Excuse me Mister, are you lost?""")
    time.sleep(1)
    lostIN = input("- ")
    if lostIN.lower() in yResponses:
        time.sleep(1)
        print("""
    %s: Yes, I am, could you help me?""" % (characterName.upper()))
        time.sleep(1)
        print("""
    BOY THREE: No. You should never have come here!
        """)
        time.sleep(1)
        gunDeath()
    elif lostIN.lower() in nResponses:
        print()
        print("Your health is currently at: %s" % (characterHealth))
        time.sleep(1)
        print("""
    BOY TWO: No need to be rude""")
        time.sleep(1)
        print()
        global boy2Damage
        print("*Boy Two throws a punch at you* - %s Health" % (boy2Damage))
        time.sleep(1)
        characterHealth = characterHealth - boy2Damage
        print("Your health is now at: %s" % (characterHealth))
        time.sleep(1)
        print("""
    SITUATION:

    The boys drag you into The Black Forest neighbouring Bryxton Town and throw you down in a bush full
    of poison ivy and berries. Not only do they leave you there, but before they do, they throw a couple more
    punches and kicks in to weaken you further.
        """)
        characterHealth = characterHealth - boy1Damage
        time.sleep(1)
        print("*Boy 1 kicks you* - %s Health" % (boy1Damage))
        time.sleep(1)
        print("Your health is now at: %s" % (characterHealth))
        print()
        time.sleep(1)
        print("Do you try to get back up? ")
        time.sleep(1)
        getUp = input("- ")
        if getUp in yResponses: 
            time.sleep(1)
            print()
            print("*Boy 3 headbutts you knocking you back down to the floor knocking you unconious* - 5 Health")
            characterHealth = characterHealth - 5
            time.sleep(1)
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(1)
            print("""
    SITUATION:

    Due to the poisonous entities around you and the state of your conciousness, you are left, stranded.
    Your health starts to deplete . . .
            """)
            time.sleep(1)
            characterHealth = characterHealth - 1
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(2)
            characterHealth = characterHealth - 1
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(2)
            print("%s has died." % (characterName))
            time.sleep(0.5)
            print()
            print("Would you like to try again?")
            playAgain = input("- ")
            if playAgain in yResponses:
                theTraveller()
            elif playAgain in nResponses:
                print()
        elif getUp in nResponses:
            time.sleep(1)
            print("""
    SITUATION:

    You refuse to get up and give in to your decision.
            """)
            time.sleep(1)
            for i in range(6):
                characterHealth = characterHealth - 1
                print("Your health is now at: %s" % (characterHealth))
                time.sleep(1)
            print("%s has died." % (characterName))
            time.sleep(0.5)
            print()
            print("Would you like to try again?")
            play2Again = input("- ")
            if play2Again in yResponses:
                theTraveller()
            elif play2Again in nResponses:
                print()


# =======================================================================================================================================
# Location Five (Second Choice Path)
# =======================================================================================================================================
def azaleaVillage():
    print()
    print("You have arrived at: Azalea Village")
    time.sleep(0.5)
    print("""
    LOCATION:

    For the first time in your travels, you are met by utter bliss. Flowers blossom, homes thrive, children
    are laughing, singing, having fun. Everyone is smiling, the sun is shining down on you, and for once
    it seems as though the world has come to peace.""")
    time.sleep(1)#Set to 15 seconds once done
    print("""
    VILLAGE PERSON 1: %s, welcome! It is amazing to see you, we have been awaiting your arrival.
                      You look so much better than we anticipated after your tiresome journey!""" % (characterName))
    time.sleep(2)
    print("""
    %s: How are you? How do you know who I am? This place is absolutely stunning, for once I can
           actually breath and not be looking over my shoulder constantly.""" % (characterName.upper()))
    time.sleep(2)
    print("""
    VILLAGER PERSON 3: We are good! The Traveller wrote to us informing us we were to be expecting you 
                       within the next few days, and here you are! We do have some news though which
                       may interest you . . .""")
    time.sleep(2)
    print("""
    %s: Is that so? Please, do tell. I have been making my way around the Realm and so far I am piecing
           together a few things that are now coming together, and I am curious to know what it is you have
           for me.""" % (characterName.upper()))
    time.sleep(2)
    print("""
    VILLAGER PERSON 2: Over the past week, our food supplies have been dwindling, we did not know why until
                       one of the children saw a beast of some kind stealing food from one of our carts. When the beast saw
                       the child, it ran towards The Snowy Mountains. It's been doing this for the past month, but it has been
                       more frequent as of late.""")
    time.sleep(2)
    print("""
    YOUNG GIRL 2: Are you going to help us %s?""" % (characterName))
    time.sleep(1)
    choiceYes = input("- ")
    if choiceYes.lower() in yResponses:
        time.sleep(0.5)
        print("""
    YOUNG GIRL 2: Thank you so much %s! You are our hero!""" % (characterName.upper()))
        print()
        time.sleep(1)
        secondLocationDirections()
    elif choiceYes.lower() in nResponses:
        print()
        print("YOUNG GIRL 2: Oh . . . that's sad to hear.")
        time.sleep(1)
        print()
        gunDeath()

# =======================================================================================================================================
# Location Six (Second Choice Path)
# =======================================================================================================================================
def theSnowyMountains():
    print()

# =======================================================================================================================================
# Loading Oar's Rest Function
# =======================================================================================================================================
def loadingOarRest():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    oarRest()

# =======================================================================================================================================
# Loading Lockwood Village Function
# =======================================================================================================================================
def loadingLockwoodVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    lockwoodVillage()

# =======================================================================================================================================
# Loading Daekrahm Village Function
# =======================================================================================================================================
def loadingDaekrahmVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    daekrahmVillage()

# =======================================================================================================================================
# Loading Traveller Function
# =======================================================================================================================================
def loadingTraveller():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    theTraveller()

# =======================================================================================================================================
# Loading Bryxton Town Function
# =======================================================================================================================================
def loadingBryxtonTown():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    bryxtonTown()

# =======================================================================================================================================
# Loading Azalea Village Function
# =======================================================================================================================================
def loadingAzaleaVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    azaleaVillage()

# =======================================================================================================================================
# Loading Traveller Function
# =======================================================================================================================================
def loadingTheSnowyMountains():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+".", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    theSnowyMountains()

# =======================================================================================================================================
# Loading Traveller Choice (Start of Game)
# =======================================================================================================================================
if loadingTravellerChoice.lower() in yResponses:
    loadingTraveller()
elif loadingTravellerChoice.lower() in nResponses:
    print("I am sorry to hear that, please, excuse me")