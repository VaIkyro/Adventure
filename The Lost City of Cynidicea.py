# Bugs:
# 
# 
# 
# 
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Notes:
# Formatting currently Lockwood onwards
# 
# 
#
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Imports:
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
import os
import random
import time
bootObtained = False
phraseObtained = False
beastHeadObtained = False
yResponses = ["yes","ye","yeah","y","yea","ok","k","kk","okay","okie","oki","correct","corrct","si","sure"]
nResponses = ["no","n","nah","nein","non","pass","never"]

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Health and Damage Stat Variables
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
characterHealth = 10
characterDamage = 2
frostGiantHealth = 15
frostGiantDamage = 3
boy1Damage = 1
boy2Damage = 2
boy3Damage = 3
gunDamage = 10
arrowDamage = 10
axeDamage = frostGiantHealth
clawDamage = characterHealth

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Start of Game Introduction
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
time.sleep(1)
print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                    ADVENTURES: THE LOST EXPLORER                                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
print("""
    INTRODUCTION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔

    Welcome to The Citadel! Founded back in 1302 The Citadel is home to many residents from many lands
    who have all come here to start a new life and enhance their living. The days are long and the nights
    are longer, food is sparse, but the Citadens make do with what they have.
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    """)
time.sleep(1)#Set to 15 seconds once done
print("    To proceed, please head over to The Traveller! He can normally be found under the Old Oak Tree!")
time.sleep(1)
loadingTravellerChoice = input("    Would you like to visit The Traveller? - ")
print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Directions
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def locationDirections():
    if bootObtained == True and phraseObtained == True:
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Where would you like to go? ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➂ - Daekrahm Village")
        print()
    elif bootObtained == True and phraseObtained == False:
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Where would you like to go? ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➁ - Lockwood Village")
        print("        ➂ - Daekrahm Village")
        print()
    elif bootObtained == False and phraseObtained == True:
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Where would you like to go? ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➀ - Oar's Rest")
        print("        ➂ - Daekrahm Village")
        print()
    else:
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Where would you like to go? ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➀ - Oar's Rest")
        print("        ➁ - Lockwood Village")
        print("        ➂ - Daekrahm Village")
        print()
    choiceOne = input("- ")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if choiceOne == "1":
        loadingOarRest()
    elif choiceOne == "2":
        loadingLockwoodVillage()
    elif choiceOne == "3":
        loadingDaekrahmVillage()
    else:
        locationDirections()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Second Location Directions
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def secondLocationDirections():
    print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Where would you like to go? ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    print("        ➀ - Bryxton Town")
    print("        ➁ - Azalea Village")
    print("        ➂ - The Snowy Mountains")
    print()
    choiceTwo = input("- ")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if choiceTwo == "1":
        loadingBryxtonTown()
    elif choiceTwo == "2":
        loadingAzaleaVillage()
    elif choiceTwo == "3":
        loadingTheSnowyMountains()
    else:
        secondLocationDirections()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# The Traveller (CONTINUED)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def travellerContinued():
    print("""
    〈 THE TRAVELLER: 〉 It is lovely to meet you %s!""" % (characterName))
    time.sleep(1)
    print()
    startQuest = input(""" 
    〈 THE TRAVELLER: 〉 Do you accept my quest? - """)
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if startQuest.lower() in yResponses:
        time.sleep(1)
        print()
        print("       Excellent! Let's get this started!")
        locationDirections()
    else:
        print()
        print("I am sorry to hear that, please, excuse me")
        time.sleep(5)

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# The Traveller
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def theTraveller():
    global characterHealth
    characterHealth = 10
    print("""
    THE TRAVELLER:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    Greetings young explorer! I heard you were new around here, I hope you are finding your way
    around The Citadel alright. The people here are very kind, I am sure they would be willing to
    help you if you got lost or confused! Anyway, enough of the introductions, I have a small 
    problem, but you see, I am not an explorer, I was wondering if you would be able to help me?
    Let's start by . . .
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    """)
    time.sleep(1)#Set to 15 seconds once done
    global characterName
    characterName = input("    Enter your Characters name - ")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    travellerContinued()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Boot Phrase Head Traveller
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def bootPhraseHead():
    # ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
        if bootObtained == True and phraseObtained == True and beastHeadObtained == True:
            print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
            print("        ➀ - I have the boot")
            print("        ➁ - I have the phrase")
            print("        ➂ - I have the head")
            print("        ➃ - Continue Locations")
            print()
            rChoice = input("- ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rChoice == "1":
                time.sleep(1)
                print("""
    〈 THE TRAVELLER: 〉 Oh wow! I haven't seen this in a while! This belonged to the Explorer I have
                         you looking for. My oh my, this has aged. But do you see how it is torn? It
                         is like something with brute force broke it. Now that you have found it, do
                         you think you could go find more information? It may help us track him down!
                   """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "2":
                time.sleep(1)
                print()
                print("*Recites the Phrase to The Traveller*")
                print("""
    〈 THE TRAVELLER: 〉 I have never heard that before! But that is actually helpful, we might have a 
                         hope at finding the Explorer with that! Keep going out to different locations
                         and see what you can find! Sound good?
                    """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "3":
                time.sleep(1)
                print("""
    〈 THE TRAVELLER: 〉 Wait . . . you did it . . . he really did turn into the beast that the myth 
                         was saying. Wow, I really am going to miss him. But congratulations %s you
                         did it! You saved Haling Cove and became a legend within the Realm!
                   """)
                print()
                time.sleep(1)
                print("""
    VICTORY ENDING:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    Congratulations! You defeated the Beast, obtained every item, and presented the head to
    The Traveller!
                """)
                time.sleep(5)
                print()
            elif rChoice == "4":
                print()
                locationDirections()
    # ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
        elif bootObtained == True and phraseObtained == True and beastHeadObtained == False:
            print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
            print("        ➀ - I have the boot")
            print("        ➁ - I have the phrase")
            print("        ➂ - Continue Locations")
            print()
            rChoice = input("- ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rChoice == "1":
                time.sleep(1)
                print("""
    〈 THE TRAVELLER: 〉 Oh wow! I haven't seen this in a while! This belonged to the Explorer I have
                         you looking for. My oh my, this has aged. But do you see how it is torn? It
                         is like something with brute force broke it. Now that you have found it, do
                         you think you could go find more information? It may help us track him down!
                   """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "2":
                time.sleep(1)
                print()
                print("*Recites the Phrase to The Traveller*")
                print("""
    〈 THE TRAVELLER: 〉 I have never heard that before! But that is actually helpful, we might have a 
                         hope at finding the Explorer with that! Keep going out to different locations
                         and see what you can find! Sound good?
                    """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "3":
                print()
                locationDirections()
    # ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
        elif bootObtained == True and phraseObtained == False and beastHeadObtained == False:
            print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
            print("        ➀ - I have the boot")
            print("        ➁ - Continue Locations")
            print()
            rChoice = input("- ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rChoice == "1":
                time.sleep(1)
                print("""
    〈 THE TRAVELLER: 〉 Oh wow! I haven't seen this in a while! This belonged to the Explorer I have
                         you looking for. My oh my, this has aged. But do you see how it is torn? It
                         is like something with brute force broke it. Now that you have found it, do
                         you think you could go find more information? It may help us track him down!
                   """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "2":
                print()
                locationDirections()
    # ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
        elif bootObtained == False and phraseObtained == True and beastHeadObtained == False:
            print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
            print("        ➀ - I have the phrase")
            print("        ➁ - Continue Locations")
            print()
            rChoice = input("- ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rChoice == "1":
                time.sleep(1)
                print()
                print("*Recites the Phrase to The Traveller*")
                print("""
    〈 THE TRAVELLER: 〉 I have never heard that before! But that is actually helpful, we might have a 
                         hope at finding the Explorer with that! Keep going out to different locations
                         and see what you can find! Sound good?
                    """)
                input("- ")
                print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
                print()
                bootPhraseHead()
            elif rChoice == "2":
                print()
                locationDirections()
    # ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
        elif bootObtained == False and phraseObtained == False and beastHeadObtained == False:
            print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
            print("        I have nothing")
            print("        ➀ - Continue Locations")
            print()
            rChoice = input("- ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rChoice == "1":
                print()
                locationDirections()
    
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# The Traveller (RETURN)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def returnTraveller():
    print()
    print("    You have arrived at: The Traveller")
    time.sleep(1)
    print("""
    〈 THE TRAVELLER: 〉 Nice to see you again %s, how goes the exploring? Do you have anything for me?""" % (characterName))
    time.sleep(1)
    bootPhraseHead()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location One (Obtain Boot)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def oarRest():
    print()
    print("You have arrived at: Oar's Rest")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔

    As you pace yourself through the hollow gates of Oar's Rest, the path beneath your feet softens, 
    the sounds of livestock and shouting pierce your ears. Slowly edging your way towards a derelict 
    cottage, a rocking chair creeks to reveal an Old Man. Layered with an old plaid shirt, suspenders
    way past his torso and a long, almost fatherly grey beard.
    """)
    time.sleep(1)#Set to 15 seconds once done
    print("""
    〈 OLD MAN: 〉 Who goes there? This is ancient land, get off it quickly before you spoil the
                   riches""")
    time.sleep(1)
    print("""
    〈 %s: 〉 The Traveller sent me on a quest and provided me with different directions,
                 so here I am. Who are you?""" % (characterName.upper()))
    time.sleep(1)
    print("""
    〈 OLD MAN: 〉 They call me the Old Man. Probably because I am old and slowly dying, but they don't care.
                   And he did did he? I'm guessing this "quest" of his is to try and find the Explorer, 
                   am I right?""")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print()
    time.sleep(1)
    yesChoice = input("- ")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if yesChoice.lower() in yResponses:
        time.sleep(1)
        print("""
    〈 OLD MAN: 〉 I thought so, up to no good again he is The Traveller. Ah well, here, this may be of
                   use to you.""")
        global bootObtained
        bootObtained = True
        print("""

        ◈ Old Boot has been obtained!◈
        """)
        time.sleep(1)
    elif yesChoice.lower() in nResponses:
        print("""
    〈 OLD MAN: 〉 Well, it was nice to see you, goodbye!""")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Boot Obtained
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
    def bootHasObtained():
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃     What do you choose?     ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➀ - What does this boot do?")
        print("        ➁ - Em, has this been washed?")
        print("        ➂ - Sorry, I think this was a bad choice.")
        print()
        bootChoice = input("- ")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        if bootChoice == "1":
            time.sleep(1)
            print("""
    〈 OLD MAN: 〉 What you are currently holding is something that was found up some mountain a
                   long time ago. No one knows what it is for though. Go back to The Traveller and
                   inform him of what you have found!""")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            time.sleep(1)
            print()
            rtIN = input("    Would you like to go back to the Traveller? - ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rtIN in yResponses:
                returnTraveller()
            elif rtIN in nResponses:
                locationDirections()
        elif bootChoice == "2":
            time.sleep(1)
            print("""
    〈 OLD MAN: 〉 Does it look like it has been washed? And more importantly does that look like
                   mine? I do not know whether to take that as an insult or a compliment.""")
            time.sleep(1)
            bootHasObtained()
        elif bootChoice == "3":
            time.sleep(1)
            print("""
    〈 OLD MAN: 〉 Fair enough, give the Traveller a slap for me will you?""")
            time.sleep(1)
            returnTraveller()
    time.sleep(1)

    if bootObtained == True:
        bootHasObtained()
    elif bootObtained == False:
        theTraveller()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Two (Obtain Phrase)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def lockwoodVillage():
    print()
    print("You have arrived at: Lockwood Village")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔

    Bells toll loudly and the shouting of men and women as a gathering is pulled together in the
    village square. Children continue playing whilst the rest casually approach the center. Clouds
    start to gather above as the sun begins to set, however one girl playing with her siblings
    draws your attention to some specific words she is saying.
    """)
    time.sleep(1)#Set to 15 seconds once done
    print("""
    〈 YOUNG GIRL: 〉 When the sun sets the clouds appear but beware of the monster upon high.""")
    time.sleep(1)
    print("""
    〈 %s: 〉 The Traveller sent me on a quest and provided me with different directions,
                 so here I am. Who are you?""" % (characterName.upper()))
    time.sleep(1)
    print("""
    〈 YOUNG GIRL: 〉 My name is Lisa, I was born here with my siblings, our parents are very busy and
                      not around much as they are in charge of the Village! The Traveller sent a note
                      that we are to be expecting someone who is looking for the Explorer, is that you?""")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print()
    time.sleep(1)
    choiceYes = input("- ")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if choiceYes.lower() in yResponses:
        time.sleep(1)
        print("""
    〈 YOUNG GIRL: 〉 Oh wow, an adventurer! I can't believe I get to meet one! This definitely is a rare
                      occurence.""")
        global phraseObtained
        phraseObtained = True
        print()
        print("""

        ◈ Phrase has been obtained!◈
        """)
        time.sleep(1)
    elif choiceYes.lower() in nResponses:
        print()
        print("〈 YOUNG GIRL: 〉 It was nice to see you " + characterName + ", but I need to go!")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Phrase Obtained
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
    def phraseHasObtained():
        print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃           Options           ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        print("        ➀ - What was that saying you just mentioned?")
        print("        ➁ - What game are you playing?")
        print("        ➂ - Excuse me little girl.")
        print()
        bootChoice = input("- ")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        if bootChoice == "1":
            print("""
    〈 YOUNG GIRL: 〉 Oh that! It's this old saying my mama tells me and my siblings, we don't exactly
                      know what it means or where it came from, but our mama says it came from this old
                      adventurer who went our adventuring and got lost down a hole in the middle of 
                      nowhere, maybe go back to The Traveller and teach him of the phrase! """)
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            time.sleep(1)
            print()
            rtIN = input("Would you like to go back to the Traveller? - ")
            print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
            if rtIN in yResponses:
                returnTraveller()
            elif rtIN in nResponses:
                locationDirections()
        elif bootChoice == "2":
            print("""
    〈 YOUNG GIRL: 〉 It's called ipp dipp, you get a pumpkin chunk and a bale of hay and the first person
                      to get the pumpkin chunk to reach the floor through the hay wins!.""")
            phraseHasObtained()
        elif bootChoice == "3":
            print("""
    〈 YOUNG GIRL: 〉 That's ok! Sorry I couldn't help more, maybe The Traveller can give you somewhere
                      else to go!""")
            locationDirections()
    time.sleep(1)

    if phraseObtained == True:
        phraseHasObtained()
    elif phraseObtained == False:
        theTraveller()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Three (Choice Path)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def daekrahmVillage():
    print()
    print("You have arrived at: Daekrahm Village")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔

    As the water spits up from all the puddles beneath your feet, you find yourself amongst these cobweb
    riddened settlements, windows all smashed in, boarded up which could only be described as as dried 
    out cloth. Making do with what they have available to them and not being as wealthy or profitable 
    as the other villages and towns within their neighbouring vacinity.""")
    time.sleep(1)
    print("""
    « dog barks in the distance »""")
    time.sleep(1)
    print("""
    〈 %s: 〉 What was that?""" % (characterName.upper()))
    time.sleep(1)
    print("""
    « dog barks again but louder »""")
    time.sleep(1)
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print()
    choiceYes = input("Do you approach? - ")
    time.sleep(1)
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    if choiceYes.lower() in yResponses:
        time.sleep(1)
        print("""
    DISCOVERY:
    ▔▔▔▔▔▔▔▔▔
        
    As you approach the dog barking towards the back of the Village, you find large footprints in the 
    snow beneath your feet, this snow coming from the mountains ahead. The dog seems unsettled and 
    disturbed by these footprints. 
    
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁

             Where do you go next?
        """)
        secondLocationDirections()
    elif choiceYes.lower() in nResponses:
        print("""
    DECISION:
    ▔▔▔▔▔▔▔▔▔

    You slowly turn your back to the dog and walk away.
            """)

def gunDeath():
    global gunDamage
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print()
    print("*a gun shot sounds from a nearby building, piercing your skull* - %s Health" % (gunDamage))
    global characterHealth
    characterHealth = characterHealth - gunDamage
    time.sleep(1)
    print("Your health is currently at: %s" % (characterHealth))
    time.sleep(1)
    print("%s has died." % (characterName))
    print()
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    time.sleep(1)
    print()
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Four (Second Choice Path)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def bryxtonTown():
    print()
    print("You have arrived at: Bryxton Town")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔

    Storm clouds gather above, doors slam shut with there locks being clasped together and shutters 
    forgotten. Anyone who is anyone within this gruesome town is in all black, hoods and masks on, 
    keeping themselves to themselves. The streets cobbled, and littered with unwanted children.""")
    time.sleep(1)
    print("""
    〈 BOY ONE: 〉 Excuse me Mister, are you lost?
    """)
    time.sleep(1)
    lostIN = input("- ")
    if lostIN.lower() in yResponses:
        time.sleep(1)
        print("""
    〈 %s: 〉 Yes, I am, could you help me?""" % (characterName.upper()))
        time.sleep(1)
        print("""
    〈 BOY THREE: 〉 No. You should never have come here!
        """)
        time.sleep(1)
        gunDeath()
    elif lostIN.lower() in nResponses:
        print()
        global characterHealth
        print("Your health is currently at: %s" % (characterHealth))
        time.sleep(1)
        print("""
    〈 BOY TWO: 〉 No need to be rude""")
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
    ▔▔▔▔▔▔▔▔▔

    The boys drag you into The Black Forest neighbouring Bryxton Town and throw you down in a bush full
    of poison ivy and berries. Not only do they leave you there, but before they do, they throw a couple 
    more punches and kicks in to weaken you further.
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
            print("*Boy 3 headbutts you knocking you back down to the floor knocking you unconcious* - 5 Health")
            characterHealth = characterHealth - 5
            time.sleep(1)
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(1)
            print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔

    Due to the poisonous entities around you and the state of your conciousness, you are left, stranded.
    Your health starts to deplete . . .
            """)
            time.sleep(1)
            characterHealth = characterHealth - 1
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(1)
            characterHealth = characterHealth - 1
            print("Your health is now at: %s" % (characterHealth))
            time.sleep(1)
            print("%s has died." % (characterName))
            time.sleep(1)
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
    ▔▔▔▔▔▔▔▔▔

    You refuse to get up and give in to your decision.
            """)
            time.sleep(1)
            for i in range(6):
                characterHealth = characterHealth - 1
                print("Your health is now at: %s" % (characterHealth))
                time.sleep(1)
            print("%s has died." % (characterName))
            time.sleep(1)
            print()
            print("Would you like to try again?")
            play2Again = input("- ")
            if play2Again in yResponses:
                theTraveller()
            elif play2Again in nResponses:
                print()


# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Five (Second Choice Path)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def azaleaVillage():
    print()
    print("You have arrived at: Azalea Village")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔

    For the first time in your travels, you are met by utter bliss. Flowers blossom, homes thrive, 
    children are laughing, singing, having fun. Everyone is smiling, the sun is shining down on you, 
    and for once it seems as though the world has come to peace.""")
    time.sleep(1)#Set to 15 seconds once done
    print("""
    VILLAGE PERSON 1: %s, welcome! It is amazing to see you, we have been awaiting your arrival.
                      You look so much better than we anticipated after your tiresome journey!""" % (characterName))
    time.sleep(1)
    print("""
    %s: How are you? How do you know who I am? This place is absolutely stunning, for once I can
           actually breath and not be looking over my shoulder constantly.""" % (characterName.upper()))
    time.sleep(1)
    print("""
    VILLAGER PERSON 3: We are good! The Traveller wrote to us informing us we were to be expecting you 
                       within the next few days, and here you are! We do have some news though which
                       may interest you . . .""")
    time.sleep(1)
    print("""
    %s: Is that so? Please, do tell. I have been making my way around the Realm and so far I am piecing
           together a few things that are now coming together, and I am curious to know what it is you have
           for me.""" % (characterName.upper()))
    time.sleep(1)
    print("""
    VILLAGER PERSON 2: Over the past week, our food supplies have been dwindling, we did not know why 
                       until one of the children saw a beast of some kind stealing food from one of our 
                       carts. When the beast saw the child, it ran towards The Snowy Mountains. It's 
                       been doing this for the past month, but it has been more frequent as of late.""")
    time.sleep(1)
    print("""
    YOUNG GIRL 2: Are you going to help us %s?""" % (characterName))
    time.sleep(1)
    choiceYes = input("- ")
    if choiceYes.lower() in yResponses:
        time.sleep(1)
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

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Six (Second Choice Path)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def theSnowyMountains():
    print()
    print("You have arrived at: The Snowy Mountains")
    time.sleep(1)
    print("""
    LOCATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    As %s travereses up the snowy mountain side, their vision weakens as the snow becomes thicker.
    With the Old Boot lodged in their bag and the weather worsening, they pick up pace to find shelter.
    An old, rotten, dripping cave is dug out in the side of the cliff as they approache.""" % (characterName))
    print()
    time.sleep(1)
    if bootObtained == True and phraseObtained == True:
        print("Do you enter the cave?")
        enter = input("- ")
        if enter.lower() in yResponses:
            time.sleep(1)
            print("""
    SCENARIO:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    As you enter the cave, you find many markings lining the walls, large footprints engraved into the
    ground beneath you. Against the back wall of the cave as you approach appears to be a large rotting
    tooth, bigger than any normal mans. However, beneath this tooth appears to be a form of parchment.

    Do you read the note?
            """)
            print()
            time.sleep(1)
            read = input("- ")
            if read in yResponses:
                time.sleep(1)
                print()
                print("~~~~~~ Cove")
                time.sleep(1)
                print()
                print("""
    SCENARIO:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    Reading the note you realise something is wrong and that whatever lived within this abandoned cave
    must have made its way towards Haling Cove!

    Do you go towards Haling Cove?
                """)
                goHaling = input("- ")
                if goHaling in yResponses:
                    time.sleep(1)
                    loadingHalingCove()
                elif goHaling in nResponses:
                    time.sleep(1)
                    print()
                    print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    With all the markings you find, you decide it is better if you no longer continue with the quest
    and decide best to stay away from anyone you interacted with, you settle down in the cave and
    hope that nothing comes back.
                """)
                    time.sleep(1)
            elif enter.lower() in nResponses:
                print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    The weather worsens rapidly and the cave spooks %s way too much.
        """ % (characterName))
                print("Your health is now at: %s" % (characterHealth))
                characterHealth = characterHealth - characterHealth
                time.sleep(1)
                print("You slowly freeze to death due to your decisions")
                time.sleep(1)
                print("Your health is now at: %s" % (characterHealth))
                print("%s has died." % (characterName))
            elif read in nResponses:
                time.sleep(1)
                print()
                print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    With all the markings you find, you decide it is better if you no longer continue with the quest
    and decide best to stay away from anyone you interacted with, you settle down in the cave and
    hope that nothing comes back.
                """)
                time.sleep(1)
        elif enter.lower() in nResponses:
            print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    The weather worsens rapidly and the cave spooks %s way too much.
        """ % (characterName))
            print("Your health is now at: %s" % (characterHealth))
            characterHealth = characterHealth - characterHealth
            time.sleep(1)
            print("You slowly freeze to death due to your decisions")
            time.sleep(1)
            print("Your health is now at: %s" % (characterHealth))
            print("%s has died." % (characterName))
    else:
        print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    The weather worsens rapidly and the cave spooks %s way too much.
        """ % (characterName))
        print("Your health is now at: %s" % (characterHealth))
        characterHealth = characterHealth - characterHealth
        time.sleep(1)
        print("You slowly freeze to death due to your decisions")
        time.sleep(1)
        print("Your health is now at: %s" % (characterHealth))
        print("%s has died." % (characterName))
        time.sleep(5)

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Location Seven (Third Choice Path)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def halingCove():
    global frostGiantHealth
    global frostGiantDamage
    global characterHealth
    global arrowDamage
    global axeDamage
    global clawDamage
    print()
    print("You have arrived at: Haling Cove")
    time.sleep(1)
    print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    As %s approaches the Cove, fire can be seen billowing from the rooftops as well as the screams and
    cries of children running away, being abandoned by their parents as everyone scatters to escape
    from something.
    
    Do you help Haling Cove?""" % (characterName))
    time.sleep(1)#Set to 15 seconds once done
    helpCove = input("- ")
    if helpCove in yResponses:
        print()
        time.sleep(1)
        print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    %s charges into the Cove with residents passing by running away, fearing their life. Fury in your 
    eyes and determination to finish the quest and come to a conclusion.
        """ % (characterName))
        time.sleep(1)
        print("*you throw a punch at the beast*")
        time.sleep(1)
        print("*%s Damage Done*" % (characterDamage)) #Monster takes 2 HP
        frostGiantHealth = frostGiantHealth - characterDamage
        time.sleep(1)
        print("The Beast has %s Health Remaining" % (frostGiantHealth)) #Monster has 13 HP remaining
        time.sleep(1)
        print()
        print("*the beast slashes your back*")
        time.sleep(1)
        print("*%s Damage Done*" % (frostGiantDamage)) #Character takes 3 HP 
        characterHealth = characterHealth - frostGiantDamage
        time.sleep(1)
        print("%s has %s Health Remaining" % (characterName, characterHealth)) #Character has 7 HP remaining
        time.sleep(1)
        print()
        print("*a local rushes in and shoots the beast with an arrow*")
        time.sleep(1)
        print("*%s Damage Done*" % (arrowDamage)) #Monster takes 10 HP
        frostGiantHealth = frostGiantHealth - arrowDamage
        time.sleep(1)
        print("The Beast has %s Health Remaining" % (frostGiantHealth)) #Monster has 3 HP remaining
        time.sleep(1)
        print()
        print("*you scratch the monster with a nearby piece of wood*")
        time.sleep(1)
        print("*%s Damage Done*" % (characterDamage)) #Monster takes 2 HP
        frostGiantHealth = frostGiantHealth - characterDamage
        time.sleep(1)
        print("The Beast has %s Health Remaining" % (frostGiantHealth)) #Monster has 1 HP
        time.sleep(1)
        print()
        print("Do you finish the Beast off?")
        decisionKill = input("- ")
        if decisionKill in yResponses:
            print()
            time.sleep(1)
            print("""
    FINISHER:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    A villager charges full sprint at you screaming your name, with a full leaded silver lined axe held
    tightly in his hand. As he quickly approaches he launches the axe towards you as you grasp it within
    your hands.
            """)
            time.sleep(1)
            print("*you swing the axe at the monsters head decapitating it*")
            time.sleep(1)
            print("*%s Damage Done*" % (axeDamage)) #Monster dies
            frostGiantHealth = frostGiantHealth - axeDamage
            time.sleep(1)
            print("The Beast has been slain, dropping its head")
            global beastHeadObtained
            beastHeadObtained = True
            print()
            time.sleep(1)
            print("The Beasts Head has been obtained!")
            time.sleep(1)
            headObtained()
        elif decisionKill in nResponses:
            print()
            time.sleep(1)
            print("""
    DEATH:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    As you stare down the Beast and look into its eyes, you realise this wasn't his choice and he has 
    done this against his will. You lower your axe hoping the Beast will change and stop everything.
            """)
            time.sleep(1)
            print("*the Beast claws you face ripping your eyes out*")
            time.sleep(1)
            print("*%s Damage Done*" % (clawDamage)) #Charater dies
            characterHealth = characterHealth - clawDamage
            time.sleep(1)
            print("%s has died." % (characterName))
            time.sleep(1)
            print("""
    ENDING:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    The Traveller has heard of the fatal news and has come to see you off into the Afterlife. As he
    stares at your coffin with a tear filling his eye, noticing how close you were, yet one decision
    got you killed, fills him with emotion he doesn't know how to handle.
            """)
            time.sleep(5)
    elif helpCove in nResponses:
        print()
        time.sleep(1)
        print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    %s starts to run away from the Cove, not to abandon them, but to go and get more help as they can
    see this is too much for them to handle on their own! All of a sudden a whoosh can be heard passing
    their ear . . .
        """ % (characterName))
        time.sleep(1)
        print("Your health is now at: %s" % (characterHealth))
        time.sleep(1)
        print("*You get shot by an arrow right into their heart* - %s Health" % (arrowDamage))
        time.sleep(1)
        print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    %s begins to collapse to the floor, knees buckle beneath you and you take your final breath, the
    arrow unable to be taken out without ripping your heart out along with it.
        """ % (characterName))
        time.sleep(1)
        print("Your health is now at: %s" % (characterHealth))
        time.sleep(1)
        print("%s has died." % (characterName))
        time.sleep(5)
    else:
        print()
        time.sleep(1)
        print("""
    SITUATION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    %s begins to run away from Haling Cove without any other thoughts or doubt on the entirity of the
    situation. Looking back at the chaos you do not regret your choice and continue to run. However,
    as you are running, village people appear out of the bushes and call you a traitor and a coward.
            """ % (characterName))
        print()
        time.sleep(1)
        gunDeath()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Head Obtained
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def headObtained():
    print("""
    DECISION:
    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔

    1 - What do I do with this head?
    2 - I'll leave this head here as a trophy!
    3 - That's gross.
        """)
    headChoice = input("- ")
    if headChoice == "1":
        print("""
    VILLAGER: Maybe take it back to the Traveller and see what he has to say?""")
        time.sleep(1)
        print()
        rtIN = input("Would you like to go back to the Traveller? - ")
        if rtIN in yResponses:
            returnTraveller()
        elif rtIN in nResponses:
            headObtained()
        elif headChoice == "2":
            print("""
    VILLAGER: Thank you so much! You are amazing, what are you going to do now?""")
            headObtained()
        elif headChoice == "3":
            print("""
    VILLAGER: Tell me about it *vomits*""")
            headObtained()
    time.sleep(1)

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Oar's Rest Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingOarRest():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    oarRest()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Lockwood Village Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingLockwoodVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    lockwoodVillage()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Daekrahm Village Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingDaekrahmVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    daekrahmVillage()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Traveller Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingTraveller():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    theTraveller()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Bryxton Town Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingBryxtonTown():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    bryxtonTown()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Azalea Village Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingAzaleaVillage():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    azaleaVillage()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading The Snowy Mountains Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingTheSnowyMountains():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    theSnowyMountains()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Haling Cove Function
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
def loadingHalingCove():
    spaces = 0
    for a in range (random.randint(1,3)):
        for b in range(10):
            print("\b "*spaces+"》", end="", flush=True)
            spaces = spaces + 1
            time.sleep(0.2)
            if (spaces >= 10):
                print("\b \b"*spaces, end="")
                spaces = 0
    halingCove()

# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
# Loading Traveller Choice (Start of Game)
# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
if loadingTravellerChoice.lower() in yResponses:
    loadingTraveller()
elif loadingTravellerChoice.lower() in nResponses:
    print("I am sorry to hear that, please, excuse me")
