#Intro

print("Hello we are going to play a little game of Madlibs.")
print("But first, a few questions...")

## Get input variables for MadLibs generator

noun1 = input("Give me a noun\n")
verb1 = input("Give me a verb.\n")
noun2 = input("Give me another noun.\n")
verb2 = input("Give me another verb.\n")
noun3 = input("Give me another noun.\n")


# gather the inputs for choice of theme

while True:
    choice = input ("Choose your theme:\nA. A Cult of Death \nB.Symphonic Misery")
    # check if d1a is equal to one of the strings, specified in the list
    if choice in ['A', 'B']:
        # if it was equal - break from the while loop
        break
# process the input
if choice == "A": 
    print ("You are surrounded by your closest friends. " + noun3 + " is eveywhere. You feel the urge to " + verb2 + " You turn to your closest " + noun2 + " and" + verb1 + "into an abyss.") 
elif choice == "B": 
    print ("Jazz players are performing all around you. You have no idea where to turn. " + noun1 + " makes you trip when you walk to the bathroom. You are " + verb1 + " so hard that you " + verb2 + " up " + noun3 + " all over the place.")


